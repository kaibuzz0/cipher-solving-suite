#!/usr/bin/env python3
"""Record source checks, detect content changes, and build collection reports."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.source_registry import build_status, load_registry, mark_checked, write_registry

HISTORY = ROOT / "data" / "source_check_history.json"
REPORT = ROOT / "artifacts" / "intelligence-source-report.json"


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_history(path: Path = HISTORY) -> dict:
    if not path.exists():
        return {"schema_version": 1, "updated_at": now_iso(), "checks": []}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data.get("checks"), list):
        raise ValueError("source check history must contain a checks list")
    return data


def normalize_fingerprint(value: str) -> str:
    value = value.strip().lower()
    if not value:
        raise ValueError("fingerprint input cannot be empty")
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def latest_check(history: dict, source_id: str) -> dict | None:
    matches = [c for c in history.get("checks", []) if c.get("source_id") == source_id]
    if not matches:
        return None
    return max(matches, key=lambda c: c.get("checked_at", ""))


def record_check(source_id: str, observed_value: str, note: str = "", checked_at: str | None = None, history_path: Path = HISTORY, update_registry: bool = True) -> dict:
    registry = load_registry()
    source_ids = {s.get("id") for s in registry.get("sources", [])}
    if source_id not in source_ids:
        raise ValueError(f"unknown source id: {source_id}")
    history = load_history(history_path)
    stamp = checked_at or now_iso()
    fingerprint = normalize_fingerprint(observed_value)
    previous = latest_check(history, source_id)
    previous_fingerprint = previous.get("content_fingerprint") if previous else None
    state = "first-seen" if previous_fingerprint is None else ("unchanged" if previous_fingerprint == fingerprint else "changed")
    entry = {"source_id": source_id, "checked_at": stamp, "content_fingerprint": fingerprint, "previous_fingerprint": previous_fingerprint, "change_state": state, "note": note}
    history["checks"].append(entry)
    history["checks"].sort(key=lambda x: x.get("checked_at", ""), reverse=True)
    history["updated_at"] = stamp
    history_path.parent.mkdir(parents=True, exist_ok=True)
    history_path.write_text(json.dumps(history, indent=2) + "\n", encoding="utf-8")
    if update_registry and history_path == HISTORY:
        mark_checked(registry, source_id, stamp)
        write_registry(registry)
    return entry


def validate_history(data: dict) -> list[str]:
    errors: list[str] = []
    registry = load_registry()
    source_ids = {s.get("id") for s in registry.get("sources", [])}
    for index, check in enumerate(data.get("checks", [])):
        for field in ("source_id", "checked_at", "content_fingerprint", "change_state"):
            if not check.get(field):
                errors.append(f"check[{index}] missing {field}")
        if check.get("source_id") not in source_ids:
            errors.append(f"check[{index}] unknown source_id")
        fp = check.get("content_fingerprint", "")
        if fp and (len(fp) != 64 or any(c not in "0123456789abcdef" for c in fp)):
            errors.append(f"check[{index}] invalid content_fingerprint")
        if check.get("change_state") not in {"first-seen", "unchanged", "changed"}:
            errors.append(f"check[{index}] invalid change_state")
    return errors


def build_report() -> dict:
    registry = load_registry()
    history = load_history()
    status = build_status(registry)
    changed = []
    for source in registry.get("sources", []):
        last = latest_check(history, source["id"])
        if last and last.get("change_state") == "changed":
            changed.append({"source_id": source["id"], "name": source["name"], **last})
    due_sources = [s for s in status["sources"] if s["freshness_state"] in {"due", "due-soon", "never-checked"}]
    return {"generated_at": now_iso(), "summary": {"total_sources": len(status["sources"]), "due_sources": len(due_sources), "changed_sources": len(changed), "history_entries": len(history.get("checks", []))}, "due_sources": due_sources, "changed_sources": changed}


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Record source checks and build intelligence collection reports")
    sub = p.add_subparsers(dest="command", required=True)
    rec = sub.add_parser("record")
    rec.add_argument("source_id")
    rec.add_argument("--observed", required=True, help="Stable textual representation of the source state or manually-derived digest input")
    rec.add_argument("--note", default="")
    rec.add_argument("--at")
    sub.add_parser("validate")
    sub.add_parser("report")
    return p


def main() -> int:
    args = parser().parse_args()
    if args.command == "record":
        print(json.dumps(record_check(args.source_id, args.observed, args.note, args.at), indent=2))
        return 0
    if args.command == "validate":
        errors = validate_history(load_history())
        if errors:
            print("\n".join(errors))
            return 1
        print(f"Source check history valid: {len(load_history().get('checks', []))} checks")
        return 0
    report = build_report()
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
