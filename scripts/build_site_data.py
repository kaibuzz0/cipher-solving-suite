#!/usr/bin/env python3
"""Build machine-readable dashboard data from repository state."""
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

from scripts.artifact_inventory import build_inventory
from scripts.source_check_history import build_report as build_collection_report

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "site-data"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_iso(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def load_cases() -> list[dict]:
    cases = []
    base = ROOT / "research" / "active-puzzles"
    if not base.exists():
        return cases
    for case_file in sorted(base.glob("*/case.json")):
        try:
            data = load_json(case_file)
        except (OSError, json.JSONDecodeError):
            continue
        data["repo_path"] = str(case_file.parent.relative_to(ROOT))
        cases.append(data)
    return cases


def source_state(source: dict, now: datetime) -> str:
    if not source.get("enabled", True):
        return "disabled"
    last = parse_iso(source.get("last_checked_at"))
    if last is None:
        return "never-checked"
    freshness = int(source.get("freshness_hours", 24))
    due = last + timedelta(hours=freshness)
    if now >= due:
        return "due"
    if due - now <= timedelta(hours=max(1, freshness // 4)):
        return "due-soon"
    return "fresh"


def build_source_status() -> dict:
    now = datetime.now(timezone.utc)
    registry = load_json(ROOT / "data" / "intelligence_sources.json")
    counts = {"fresh": 0, "due-soon": 0, "due": 0, "never-checked": 0, "disabled": 0}
    items = []
    for source in registry.get("sources", []):
        state = source_state(source, now)
        counts[state] = counts.get(state, 0) + 1
        items.append({**source, "freshness_state": state})
    items.sort(key=lambda x: (x.get("freshness_state", ""), x.get("name", "")))
    return {"generated_at": now.isoformat(), "counts": counts, "sources": items}


def build_status(cases: list[dict], source_status: dict, collection: dict, artifacts: dict) -> dict:
    tools = load_json(ROOT / "data" / "tools.json")
    opportunities = load_json(ROOT / "data" / "opportunities.json")
    prompts = load_json(ROOT / "data" / "prompts.json")
    intelligence = load_json(ROOT / "data" / "intelligence.json")
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "active_cases": len(cases),
        "tools": len(tools.get("items", [])),
        "opportunities": len(opportunities.get("items", [])),
        "prompts": len(prompts.get("prompts", [])),
        "intelligence": len(intelligence.get("items", [])),
        "intelligence_sources": len(source_status.get("sources", [])),
        "sources_due": source_status.get("counts", {}).get("due", 0) + source_status.get("counts", {}).get("never-checked", 0),
        "sources_changed": collection.get("summary", {}).get("changed_sources", 0),
        "source_history_entries": collection.get("summary", {}).get("history_entries", 0),
        "artifacts": artifacts.get("summary", {}).get("total", 0),
        "artifacts_review_before_move": artifacts.get("summary", {}).get("review_before_move", 0),
    }


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    cases = load_cases()
    source_status = build_source_status()
    collection = build_collection_report()
    artifacts = build_inventory()
    (OUT / "cases.json").write_text(json.dumps({"items": cases}, indent=2) + "\n", encoding="utf-8")
    (OUT / "sources.json").write_text(json.dumps(source_status, indent=2) + "\n", encoding="utf-8")
    (OUT / "collection-health.json").write_text(json.dumps(collection, indent=2) + "\n", encoding="utf-8")
    (OUT / "artifacts.json").write_text(json.dumps(artifacts, indent=2) + "\n", encoding="utf-8")
    (OUT / "status.json").write_text(json.dumps(build_status(cases, source_status, collection, artifacts), indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
