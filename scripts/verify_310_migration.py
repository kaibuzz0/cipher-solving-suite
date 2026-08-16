#!/usr/bin/env python3
"""Verify the 310 BTC challenge evidence relocation and emit SHA-256 diagnostics."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASE_ID = "20260816-310-btc-challenge"
CASE = ROOT / "research" / "active-puzzles" / CASE_ID
MANIFEST = CASE / "bitplane_duplicate_manifest.json"
REPORT = ROOT / "artifacts" / "310-migration-verification.json"
PRIMARY = ROOT / "310_challenge.png"
GENERATED = CASE / "evidence" / "generated"
OLD_PATHS = [
    ROOT / "alpha_lsb.bin",
    ROOT / "alpha_pattern.bin",
    ROOT / "alpha_2bit.bin",
    ROOT / "alpha_row310.bin",
    ROOT / "bitplanes",
    ROOT / "analyze_310.py",
    ROOT / "alpha_extract.py",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    errors: list[str] = []
    if not PRIMARY.is_file():
        errors.append("protected primary evidence missing: 310_challenge.png")
    if any(path.exists() for path in OLD_PATHS):
        errors.extend(f"legacy path still present: {path.relative_to(ROOT)}" for path in OLD_PATHS if path.exists())
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    entries = []
    for path in sorted(GENERATED.rglob("*")):
        if path.is_file():
            entries.append({
                "path": path.relative_to(ROOT).as_posix(),
                "size_bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            })
    expected_generated = 28  # 4 alpha binaries + 24 bitplanes
    if len(entries) != expected_generated:
        errors.append(f"expected {expected_generated} generated evidence files, found {len(entries)}")
    by_path = {entry["path"]: entry for entry in entries}
    duplicate_checks = []
    for group in manifest.get("duplicate_groups", []):
        paths = group.get("new_paths", [])
        if len(paths) != 2:
            errors.append(f"duplicate group {group.get('group')} does not contain two new paths")
            continue
        left = by_path.get(paths[0])
        right = by_path.get(paths[1])
        if not left or not right:
            errors.append(f"duplicate group {group.get('group')} missing relocated file")
            continue
        same = left["sha256"] == right["sha256"]
        if not same:
            errors.append(f"duplicate group {group.get('group')} SHA-256 mismatch")
        duplicate_checks.append({
            "group": group.get("group"),
            "paths": paths,
            "sha256": left["sha256"] if same else None,
            "match": same,
        })
    report = {
        "schema_version": 1,
        "case_id": CASE_ID,
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "primary_evidence": {
            "path": "310_challenge.png",
            "present": PRIMARY.is_file(),
            "sha256": sha256_file(PRIMARY) if PRIMARY.is_file() else None,
        },
        "generated_evidence_count": len(entries),
        "generated_evidence": entries,
        "duplicate_checks": duplicate_checks,
        "errors": errors,
        "status": "pass" if not errors else "fail",
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "generated": len(entries), "duplicate_groups": len(duplicate_checks), "errors": errors}, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
