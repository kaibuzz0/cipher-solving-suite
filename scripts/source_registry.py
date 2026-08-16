#!/usr/bin/env python3
"""Inspect, validate, and update the intelligence source registry."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "intelligence_sources.json"
ALLOWED_TYPES = {"official", "platform", "aggregator", "research-index", "feed", "other"}
ALLOWED_TIERS = {"primary", "discovery", "secondary"}
ALLOWED_CONFIDENCE = {"low", "medium", "high"}


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def parse_iso(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def iso(value: datetime) -> str:
    return value.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_registry(path: Path = REGISTRY) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data.get("sources"), list):
        raise ValueError("source registry must contain a sources list")
    return data


def source_due_state(source: dict, now: datetime | None = None) -> str:
    now = now or now_utc()
    if not source.get("enabled", True):
        return "disabled"
    last = parse_iso(source.get("last_checked_at"))
    if last is None:
        return "never-checked"
    freshness = int(source.get("freshness_hours", 24))
    due = last + timedelta(hours=freshness)
    if now >= due:
        return "due"
    remaining = due - now
    if remaining <= timedelta(hours=max(1, freshness // 4)):
        return "due-soon"
    return "fresh"


def validate_registry(data: dict) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for index, source in enumerate(data.get("sources", [])):
        sid = source.get("id")
        if not sid:
            errors.append(f"source[{index}] missing id")
        elif sid in seen:
            errors.append(f"duplicate source id: {sid}")
        seen.add(sid)
        for field in ("name", "source_type", "url", "categories", "tier", "freshness_hours", "assigned_agent", "publish_default_confidence"):
            if source.get(field) in (None, "", []):
                errors.append(f"source[{index}] missing {field}")
        if source.get("source_type") not in ALLOWED_TYPES:
            errors.append(f"source[{index}] invalid source_type")
        if source.get("tier") not in ALLOWED_TIERS:
            errors.append(f"source[{index}] invalid tier")
        if source.get("publish_default_confidence") not in ALLOWED_CONFIDENCE:
            errors.append(f"source[{index}] invalid publish_default_confidence")
        if source.get("url") and not str(source["url"]).startswith("https://"):
            errors.append(f"source[{index}] url must use https")
        try:
            if int(source.get("freshness_hours", 0)) <= 0:
                errors.append(f"source[{index}] freshness_hours must be positive")
        except (TypeError, ValueError):
            errors.append(f"source[{index}] freshness_hours must be an integer")
        try:
            parse_iso(source.get("last_checked_at"))
        except ValueError:
            errors.append(f"source[{index}] invalid last_checked_at")
    return errors


def list_sources(data: dict, due_only: bool = False, agent: str | None = None) -> None:
    sources = data.get("sources", [])
    if agent:
        sources = [s for s in sources if s.get("assigned_agent") == agent]
    rows = []
    for source in sources:
        state = source_due_state(source)
        if due_only and state not in {"due", "due-soon", "never-checked"}:
            continue
        rows.append((state, source))
    order = {"never-checked": 0, "due": 1, "due-soon": 2, "fresh": 3, "disabled": 4}
    rows.sort(key=lambda pair: (order.get(pair[0], 9), pair[1].get("name", "")))
    if not rows:
        print("No matching intelligence sources.")
        return
    for state, source in rows:
        print(f"[{state}] {source['id']} — {source['name']}")
        print(f"  agent={source['assigned_agent']} freshness={source['freshness_hours']}h tier={source['tier']}")
        print(f"  {source['url']}")


def mark_checked(data: dict, source_id: str, checked_at: str | None = None) -> dict:
    stamp = checked_at or iso(now_utc())
    parse_iso(stamp)
    for source in data.get("sources", []):
        if source.get("id") == source_id:
            source["last_checked_at"] = stamp
            data["updated_at"] = iso(now_utc())
            return source
    raise ValueError(f"unknown source id: {source_id}")


def write_registry(data: dict, path: Path = REGISTRY) -> None:
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def build_status(data: dict) -> dict:
    states = {"fresh": 0, "due-soon": 0, "due": 0, "never-checked": 0, "disabled": 0}
    items = []
    for source in data.get("sources", []):
        state = source_due_state(source)
        states[state] = states.get(state, 0) + 1
        items.append({**source, "freshness_state": state})
    return {"generated_at": iso(now_utc()), "counts": states, "sources": items}


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Manage intelligence collection sources")
    sub = p.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    ls = sub.add_parser("list")
    ls.add_argument("--due", action="store_true")
    ls.add_argument("--agent")
    check = sub.add_parser("mark-checked")
    check.add_argument("source_id")
    check.add_argument("--at")
    sub.add_parser("status-json")
    return p


def main() -> int:
    args = parser().parse_args()
    data = load_registry()
    if args.command == "validate":
        errors = validate_registry(data)
        if errors:
            print("\n".join(errors))
            return 1
        print(f"Source registry valid: {len(data['sources'])} sources")
        return 0
    if args.command == "list":
        list_sources(data, args.due, args.agent)
        return 0
    if args.command == "mark-checked":
        source = mark_checked(data, args.source_id, args.at)
        write_registry(data)
        print(f"Marked checked: {source['id']} at {source['last_checked_at']}")
        return 0
    print(json.dumps(build_status(data), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
