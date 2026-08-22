#!/usr/bin/env python3
"""Reproduce 310 alpha evidence in a temporary workspace and compare it safely.

This verifier never overwrites canonical evidence. It runs the case-local portable
alpha extractor into a temporary directory, hashes the regenerated outputs, and
compares them byte-for-byte with the migrated evidence already tracked by the
case. A JSON report is written to a managed artifact path.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CASE_ROOT = ROOT / "research" / "active-puzzles" / "20260816-310-btc-challenge"
DEFAULT_IMAGE = ROOT / "310_challenge.png"
DEFAULT_EXTRACTOR = CASE_ROOT / "tools" / "alpha_extract.py"
DEFAULT_EXPECTED_DIR = CASE_ROOT / "evidence" / "generated"
DEFAULT_REPORT = ROOT / "artifacts" / "310-reproduction-verification.json"
OUTPUT_NAMES = (
    "alpha_lsb.bin",
    "alpha_pattern.bin",
    "alpha_2bit.bin",
    "alpha_row310.bin",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def compare_file(expected: Path, regenerated: Path) -> dict[str, Any]:
    expected_exists = expected.is_file()
    regenerated_exists = regenerated.is_file()
    record: dict[str, Any] = {
        "name": expected.name,
        "expected_path": str(expected.relative_to(ROOT)) if expected.is_relative_to(ROOT) else str(expected),
        "regenerated_path": regenerated.name,
        "expected_exists": expected_exists,
        "regenerated_exists": regenerated_exists,
        "match": False,
    }
    if not expected_exists or not regenerated_exists:
        return record

    expected_size = expected.stat().st_size
    regenerated_size = regenerated.stat().st_size
    expected_hash = sha256_file(expected)
    regenerated_hash = sha256_file(regenerated)
    record.update(
        {
            "expected_size_bytes": expected_size,
            "regenerated_size_bytes": regenerated_size,
            "expected_sha256": expected_hash,
            "regenerated_sha256": regenerated_hash,
            "match": expected_size == regenerated_size and expected_hash == regenerated_hash,
        }
    )
    return record


def verify(
    image: Path,
    extractor: Path,
    expected_dir: Path,
    report_path: Path,
) -> dict[str, Any]:
    image = image.expanduser().resolve()
    extractor = extractor.expanduser().resolve()
    expected_dir = expected_dir.expanduser().resolve()
    report_path = report_path.expanduser().resolve()

    missing = [str(path) for path in (image, extractor, expected_dir) if not path.exists()]
    if missing:
        report = {
            "schema_version": 1,
            "case_id": "20260816-310-btc-challenge",
            "status": "fail",
            "errors": [f"required path missing: {path}" for path in missing],
            "outputs": [],
        }
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        return report

    with tempfile.TemporaryDirectory(prefix="btc310-reproduction-") as tmp:
        regenerated_dir = Path(tmp)
        command = [sys.executable, str(extractor), str(image), "--output-dir", str(regenerated_dir)]
        proc = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
        outputs = [
            compare_file(expected_dir / name, regenerated_dir / name)
            for name in OUTPUT_NAMES
        ]

    errors: list[str] = []
    if proc.returncode != 0:
        errors.append(f"extractor exited with status {proc.returncode}")
    for item in outputs:
        if not item["match"]:
            errors.append(f"reproduction mismatch: {item['name']}")

    report = {
        "schema_version": 1,
        "case_id": "20260816-310-btc-challenge",
        "purpose": "non-destructive regeneration comparison; not solve evidence",
        "primary_evidence": {
            "path": str(image.relative_to(ROOT)) if image.is_relative_to(ROOT) else str(image),
            "size_bytes": image.stat().st_size,
            "sha256": sha256_file(image),
        },
        "extractor": {
            "path": str(extractor.relative_to(ROOT)) if extractor.is_relative_to(ROOT) else str(extractor),
            "returncode": proc.returncode,
            "stdout_tail": proc.stdout[-4000:],
            "stderr_tail": proc.stderr[-4000:],
        },
        "outputs": outputs,
        "errors": errors,
        "status": "pass" if not errors else "fail",
    }
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Regenerate 310 alpha outputs in a temporary directory and compare with preserved migrated evidence"
    )
    parser.add_argument("--image", type=Path, default=DEFAULT_IMAGE, help="Protected challenge image path")
    parser.add_argument("--extractor", type=Path, default=DEFAULT_EXTRACTOR, help="Portable alpha extractor path")
    parser.add_argument("--expected-dir", type=Path, default=DEFAULT_EXPECTED_DIR, help="Migrated evidence directory")
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT, help="Managed JSON verification report path")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    report = verify(args.image, args.extractor, args.expected_dir, args.report)
    print(json.dumps({"status": report["status"], "report": str(args.report)}, sort_keys=True))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
