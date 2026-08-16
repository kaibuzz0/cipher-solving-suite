#!/usr/bin/env python3
"""Create a timestamped opportunity snapshot from the shared verified-link catalog.

This command intentionally does not claim to scrape or discover live programs. Network
adapters can be added later, but their output must be timestamped and distinguish live
responses from fixtures/cached data.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "data" / "opportunities.json"
FEEDS = ROOT / "intelligence" / "feeds"


def build_snapshot(category: str | None = None) -> dict:
    with CATALOG.open(encoding="utf-8") as handle:
        catalog = json.load(handle)
    items = catalog.get("items", [])
    if category:
        items = [item for item in items if item.get("category") == category]
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": "data/opportunities.json",
        "source_updated_at": catalog.get("updated_at"),
        "live_scan": False,
        "notice": "Catalog snapshot only. Verify each official link for current availability, payout, eligibility and scope.",
        "total": len(items),
        "categories": dict(sorted(Counter(item.get("category", "unknown") for item in items).items())),
        "items": items,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Snapshot the shared opportunity catalog")
    parser.add_argument("--category", help="Only include one exact category")
    parser.add_argument("--stdout", action="store_true", help="Print JSON instead of writing intelligence/feeds")
    args = parser.parse_args()
    snapshot = build_snapshot(args.category)
    if args.stdout:
        print(json.dumps(snapshot, indent=2))
        return 0
    FEEDS.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%SZ")
    target = FEEDS / f"opportunity-snapshot-{stamp}.json"
    target.write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {target.relative_to(ROOT)} ({snapshot['total']} catalog entries)")
    print("This is a catalog snapshot, not a live scrape. Verify official program pages before acting.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
