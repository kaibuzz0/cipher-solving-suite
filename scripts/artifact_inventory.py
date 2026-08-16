#!/usr/bin/env python3
"""Inventory research artifacts/evidence without moving or modifying them."""
from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "artifacts" / "artifact-inventory.json"
INCLUDE_SUFFIXES = {".bin", ".dat", ".raw", ".hex", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".zip", ".tar", ".gz", ".7z", ".pcap", ".pcapng", ".pdf"}
SKIP_PARTS = {".git", ".pytest_cache", "__pycache__", "site-data", "artifacts"}
PRIMARY_HINTS = {"challenge", "original", "source", "evidence", "capture"}
GENERATED_DIRS = {"bitplanes", "workspace"}
GENERATED_PREFIXES = ("alpha_", "bitplane_", "extract_", "decoded_", "output_", "render_")
MIGRATION_STATES = {
    "SAFE TO ORGANIZE",
    "NEEDS CASE LINK",
    "DUPLICATE",
    "UNKNOWN PROVENANCE",
    "GENERATED OUTPUT",
    "PRIMARY EVIDENCE — DO NOT MOVE YET",
}


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def classify(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp"}: return "image"
    if suffix in {".bin", ".dat", ".raw", ".hex"}: return "binary"
    if suffix in {".zip", ".tar", ".gz", ".7z"}: return "archive"
    if suffix in {".pcap", ".pcapng"}: return "capture"
    if suffix == ".pdf": return "document"
    return "artifact"


def case_hint(rel: Path) -> str:
    parts = rel.parts
    if len(parts) >= 3 and parts[0] == "research" and parts[1] == "active-puzzles": return parts[2]
    return ""


def is_primary(rel: Path) -> bool:
    stem = rel.stem.lower()
    return rel.parent == Path(".") and any(h in stem for h in PRIMARY_HINTS)


def is_generated(rel: Path) -> bool:
    return bool(rel.parts and rel.parts[0] in GENERATED_DIRS) or rel.name.lower().startswith(GENERATED_PREFIXES)


def base_state(rel: Path, related_case: str) -> str:
    if is_primary(rel): return "PRIMARY EVIDENCE — DO NOT MOVE YET"
    if is_generated(rel): return "GENERATED OUTPUT"
    if related_case: return "SAFE TO ORGANIZE"
    if rel.parent == Path("."): return "NEEDS CASE LINK"
    return "UNKNOWN PROVENANCE"


def build_inventory(root: Path = ROOT) -> dict:
    items = []
    for path in sorted(root.rglob("*")):
        if not path.is_file(): continue
        rel = path.relative_to(root)
        if any(part in SKIP_PARTS for part in rel.parts): continue
        if path.suffix.lower() not in INCLUDE_SUFFIXES: continue
        related_case = case_hint(rel)
        stat = path.stat()
        items.append({
            "path": rel.as_posix(), "name": path.name, "artifact_type": classify(path),
            "mime_type": mimetypes.guess_type(path.name)[0] or "application/octet-stream",
            "size_bytes": stat.st_size, "sha256": sha256_file(path), "related_case": related_case,
            "migration_state": base_state(rel, related_case),
            "orphaned": not bool(related_case), "duplicate_group": "", "duplicate_count": 1,
            "provenance": "tracked repository file; origin/details require case or research-note review",
        })
    by_hash = defaultdict(list)
    for item in items: by_hash[item["sha256"]].append(item)
    for digest, group in by_hash.items():
        if len(group) < 2: continue
        gid = digest[:12]
        for item in group:
            item["duplicate_group"] = gid
            item["duplicate_count"] = len(group)
            if item["migration_state"] != "PRIMARY EVIDENCE — DO NOT MOVE YET": item["migration_state"] = "DUPLICATE"
    counts = {state: sum(i["migration_state"] == state for i in items) for state in MIGRATION_STATES}
    return {"schema_version": 2, "generated_at": now_iso(), "summary": {
        "total": len(items), "bytes": sum(i["size_bytes"] for i in items),
        "duplicate_groups": sum(1 for g in by_hash.values() if len(g) > 1),
        "orphaned": sum(i["orphaned"] for i in items), "migration_states": counts,
    }, "items": items}


def validate_inventory(data: dict) -> list[str]:
    errors = []; seen_paths = set()
    for index, item in enumerate(data.get("items", [])):
        for field in ("path", "artifact_type", "size_bytes", "sha256", "migration_state"):
            if item.get(field) in (None, ""): errors.append(f"item[{index}] missing {field}")
        if item.get("path") in seen_paths: errors.append(f"duplicate path: {item.get('path')}")
        seen_paths.add(item.get("path"))
        digest = item.get("sha256", "")
        if digest and (len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest)): errors.append(f"item[{index}] invalid sha256")
        if item.get("migration_state") not in MIGRATION_STATES: errors.append(f"item[{index}] invalid migration_state")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Inventory repository artifacts/evidence without moving files")
    parser.add_argument("command", choices=["scan", "validate"]); parser.add_argument("--output", default=str(DEFAULT_OUT)); args = parser.parse_args()
    output = Path(args.output)
    if args.command == "scan":
        data = build_inventory(); output.parent.mkdir(parents=True, exist_ok=True); output.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8"); print(json.dumps(data["summary"], indent=2)); return 0
    if not output.exists(): print(f"inventory not found: {output}"); return 1
    data = json.loads(output.read_text(encoding="utf-8")); errors = validate_inventory(data)
    if errors: print("\n".join(errors)); return 1
    print(f"Artifact inventory valid: {len(data.get('items', []))} items"); return 0

if __name__ == "__main__": raise SystemExit(main())
