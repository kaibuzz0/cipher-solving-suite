#!/usr/bin/env python3
"""Cipher Solving Suite operations hub entry point."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VERSION = "3.1.0"
CODENAME = "HERMES-OPS"


def run_script(relative: str, *args: str) -> int:
    target = ROOT / relative
    if not target.exists():
        print(f"Unavailable: {relative} does not exist yet.", file=sys.stderr)
        return 2
    return subprocess.call([sys.executable, str(target), *args], cwd=ROOT)


def catalog_count() -> tuple[int, str]:
    path = ROOT / "data" / "opportunities.json"
    if not path.exists():
        return 0, "missing"
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    return len(data.get("items", [])), data.get("updated_at", "unknown")


def status() -> int:
    count, updated = catalog_count()
    dashboard = "site/index.html" if (ROOT / "site" / "index.html").exists() else "missing"
    handoff = "docs/AGENT_HANDOFF.md" if (ROOT / "docs" / "AGENT_HANDOFF.md").exists() else "missing"
    print(f"Cipher Solving Suite {VERSION} ({CODENAME})")
    print("Mode: research/operations hub")
    print(f"Opportunity catalog: {count} entries; updated {updated}")
    print(f"Dashboard source: {dashboard}")
    print(f"Agent handoff: {handoff}")
    print("\nCapabilities are only considered live when backed by code/data and verification.")
    print("Security work must stay inside explicit CTF/lab/audit/bug-bounty authorization and scope.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Cipher Solving Suite operations hub")
    parser.add_argument("--status", action="store_true", help="Show current local hub status")
    parser.add_argument("--opportunities", action="store_true", help="List catalogued earning/learning opportunities")
    parser.add_argument("--scan", action="store_true", help="Write a timestamped catalog snapshot (not a live scrape)")
    parser.add_argument("--earnings", action="store_true", help="Show earnings/attempt statistics")
    parser.add_argument("--maintenance", action="store_true", help="Run repository maintenance checks")
    args = parser.parse_args()

    if args.opportunities:
        return run_script("tools/opportunity_finder.py", "--list")
    if args.scan:
        return run_script("tools/scanning/opportunity_scanner.py")
    if args.earnings:
        return run_script("tools/earnings_tracker.py", "stats")
    if args.maintenance:
        return run_script("scripts/maintenance_check.py")
    return status()


if __name__ == "__main__":
    raise SystemExit(main())
