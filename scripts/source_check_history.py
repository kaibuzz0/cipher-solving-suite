#!/usr/bin/env python3
"""Record source checks, replay preserved snapshots, and build collection reports."""
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

from scripts.source_registry import REGISTRY, build_status, load_registry, mark_checked, parse_iso, write_registry

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
    parse_iso(stamp)
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


def _validate_snapshot(snapshot: dict, registry: dict) -> tuple[str, list[dict]]:
    stamp = snapshot.get("checked_at")
    if not isinstance(stamp, str) or not stamp:
        raise ValueError("snapshot missing checked_at")
    parse_iso(stamp)
    observations = snapshot.get("observations")
    if not isinstance(observations, list) or not observations:
        raise ValueError("snapshot must contain a non-empty observations list")
    source_ids = {s.get("id") for s in registry.get("sources", [])}
    seen: set[str] = set()
    normalized: list[dict] = []
    for index, observation in enumerate(observations):
        if not isinstance(observation, dict):
            raise ValueError(f"observation[{index}] must be an object")
        source_id = observation.get("source_id")
        if not source_id or source_id not in source_ids:
            raise ValueError(f"observation[{index}] unknown source_id: {source_id}")
        if source_id in seen:
            raise ValueError(f"duplicate snapshot source_id: {source_id}")
        seen.add(source_id)
        observed = observation.get("observed")
        expected_sha = observation.get("sha256")
        if not isinstance(observed, str) or not observed.strip():
            raise ValueError(f"observation[{index}] missing observed")
        actual_sha = normalize_fingerprint(observed)
        if expected_sha != actual_sha:
            raise ValueError(f"observation[{index}] fingerprint mismatch for {source_id}: expected {expected_sha}, computed {actual_sha}")
        normalized.append({
            "source_id": source_id,
            "observed": observed,
            "sha256": actual_sha,
            "note": str(observation.get("note") or ""),
        })
    return stamp, normalized


def replay_snapshot(
    snapshot_path: Path,
    history_path: Path = HISTORY,
    registry_path: Path = REGISTRY,
    *,
    write: bool = True,
) -> dict:
    """Replay one preserved source-health snapshot without inventing chronology.

    Every observation hash is recomputed from its preserved ``observed`` string.
    The latest canonical record must be older than the snapshot (or the exact same
    idempotent record). Registry timestamps may advance but are never rewound.
    All validation completes before either output file is written.
    """
    snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
    registry = load_registry(registry_path)
    history = load_history(history_path)
    stamp, observations = _validate_snapshot(snapshot, registry)
    stamp_dt = parse_iso(stamp)
    assert stamp_dt is not None

    entries: list[dict] = []
    skipped: list[str] = []
    registry_by_id = {s.get("id"): s for s in registry.get("sources", [])}

    for observation in observations:
        source_id = observation["source_id"]
        fingerprint = observation["sha256"]
        same_time = [
            check for check in history.get("checks", [])
            if check.get("source_id") == source_id and check.get("checked_at") == stamp
        ]
        if same_time:
            if len(same_time) != 1 or same_time[0].get("content_fingerprint") != fingerprint:
                raise ValueError(f"conflicting canonical record already exists for {source_id} at {stamp}")
            skipped.append(source_id)
            continue

        previous = latest_check(history, source_id)
        if previous:
            previous_dt = parse_iso(previous.get("checked_at"))
            if previous_dt is None:
                raise ValueError(f"latest canonical record for {source_id} has invalid checked_at")
            if previous_dt > stamp_dt:
                raise ValueError(
                    f"chronology violation for {source_id}: latest canonical check {previous['checked_at']} is newer than snapshot {stamp}"
                )
            previous_fingerprint = previous.get("content_fingerprint")
        else:
            previous_fingerprint = None
        state = "first-seen" if previous_fingerprint is None else ("unchanged" if previous_fingerprint == fingerprint else "changed")
        entries.append({
            "source_id": source_id,
            "checked_at": stamp,
            "content_fingerprint": fingerprint,
            "previous_fingerprint": previous_fingerprint,
            "change_state": state,
            "note": observation["note"],
        })

        source = registry_by_id[source_id]
        last_checked = parse_iso(source.get("last_checked_at"))
        if last_checked and last_checked > stamp_dt:
            raise ValueError(
                f"registry chronology violation for {source_id}: last_checked_at {source['last_checked_at']} is newer than snapshot {stamp}"
            )

    new_history = json.loads(json.dumps(history))
    new_registry = json.loads(json.dumps(registry))
    new_registry_by_id = {s.get("id"): s for s in new_registry.get("sources", [])}
    if entries:
        new_history["checks"].extend(entries)
        new_history["checks"].sort(key=lambda x: x.get("checked_at", ""), reverse=True)
        latest_history_stamp = max((c.get("checked_at", "") for c in new_history["checks"]), default=stamp)
        new_history["updated_at"] = latest_history_stamp
        for entry in entries:
            new_registry_by_id[entry["source_id"]]["last_checked_at"] = stamp
        current_registry_update = parse_iso(new_registry.get("updated_at")) if new_registry.get("updated_at") else None
        if current_registry_update is None or current_registry_update <= stamp_dt:
            new_registry["updated_at"] = stamp

    if write and entries:
        history_path.parent.mkdir(parents=True, exist_ok=True)
        history_path.write_text(json.dumps(new_history, indent=2) + "\n", encoding="utf-8")
        write_registry(new_registry, registry_path)

    return {
        "snapshot": str(snapshot_path),
        "checked_at": stamp,
        "validated_observations": len(observations),
        "replayed": entries,
        "skipped_idempotent": skipped,
        "wrote_files": bool(write and entries),
    }


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
    p = argparse.ArgumentParser(description="Record source checks, replay preserved snapshots, and build intelligence collection reports")
    sub = p.add_subparsers(dest="command", required=True)
    rec = sub.add_parser("record")
    rec.add_argument("source_id")
    rec.add_argument("--observed", required=True, help="Stable textual representation of the source state or manually-derived digest input")
    rec.add_argument("--note", default="")
    rec.add_argument("--at")
    replay = sub.add_parser("replay-snapshot", help="Validate and replay a preserved intelligence/feeds source-health snapshot")
    replay.add_argument("snapshot", type=Path)
    replay.add_argument("--history", type=Path, default=HISTORY)
    replay.add_argument("--registry", type=Path, default=REGISTRY)
    replay.add_argument("--dry-run", action="store_true", help="Validate chronology and fingerprints without writing canonical files")
    sub.add_parser("validate")
    sub.add_parser("report")
    return p


def main() -> int:
    args = parser().parse_args()
    if args.command == "record":
        print(json.dumps(record_check(args.source_id, args.observed, args.note, args.at), indent=2))
        return 0
    if args.command == "replay-snapshot":
        try:
            result = replay_snapshot(args.snapshot, args.history, args.registry, write=not args.dry_run)
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            print(f"Replay failed: {exc}", file=sys.stderr)
            return 1
        print(json.dumps(result, indent=2))
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
