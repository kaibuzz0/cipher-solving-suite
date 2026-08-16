#!/usr/bin/env python3
"""Track attempts and verified earnings from challenges and freelance work."""

from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA_FILE = ROOT / "research" / "solutions" / "earnings.json"


class EarningsTracker:
    def __init__(self, data_file: Path = DEFAULT_DATA_FILE):
        self.data_file = Path(data_file)
        self.data = self._load_data()

    def _load_data(self) -> dict:
        if self.data_file.exists():
            with self.data_file.open(encoding="utf-8") as handle:
                return json.load(handle)
        return {"total_earned": 0.0, "total_attempts": 0, "successful_solves": 0, "platforms": {}, "history": []}

    def save_data(self) -> None:
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        with self.data_file.open("w", encoding="utf-8") as handle:
            json.dump(self.data, handle, indent=2)
            handle.write("\n")

    def add_earnings(self, platform: str, amount: float, work_name: str, notes: str = "") -> None:
        if amount < 0:
            raise ValueError("amount must be non-negative")
        self.data["total_earned"] += amount
        self.data["successful_solves"] += 1
        platform_data = self.data["platforms"].setdefault(platform, {"earnings": 0.0, "solves": 0, "attempts": 0})
        platform_data.setdefault("attempts", 0)
        platform_data["earnings"] += amount
        platform_data["solves"] += 1
        self.data["history"].append({"date": datetime.now(timezone.utc).isoformat(), "kind": "earning", "platform": platform, "amount": amount, "work": work_name, "notes": notes})
        self.save_data()

    def add_attempt(self, platform: str, work_name: str, notes: str = "") -> None:
        self.data["total_attempts"] += 1
        platform_data = self.data["platforms"].setdefault(platform, {"earnings": 0.0, "solves": 0, "attempts": 0})
        platform_data.setdefault("attempts", 0)
        platform_data["attempts"] += 1
        self.data["history"].append({"date": datetime.now(timezone.utc).isoformat(), "kind": "attempt", "platform": platform, "work": work_name, "notes": notes})
        self.save_data()

    def get_stats(self) -> dict:
        attempts = self.data["total_attempts"]
        solves = self.data["successful_solves"]
        return {"total_earned": self.data["total_earned"], "total_attempts": attempts, "successful_solves": solves, "success_rate": (solves / attempts * 100) if attempts else 0.0, "platforms": self.data["platforms"]}

    def display_dashboard(self) -> None:
        stats = self.get_stats()
        print(f"Total earned: ${stats['total_earned']:.2f}")
        print(f"Successful paid outcomes: {stats['successful_solves']}")
        print(f"Attempts logged: {stats['total_attempts']}")
        print(f"Paid-outcome / attempt ratio: {stats['success_rate']:.1f}%")
        if stats["platforms"]:
            print("\nBy platform:")
            for platform, data in sorted(stats["platforms"].items()):
                print(f"  {platform}: ${data.get('earnings',0):.2f} | paid={data.get('solves',0)} | attempts={data.get('attempts',0)}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Track Cipher Solving Suite attempts and earnings")
    parser.add_argument("--data-file", type=Path, default=DEFAULT_DATA_FILE, help=argparse.SUPPRESS)
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("stats")
    attempt = sub.add_parser("attempt")
    attempt.add_argument("platform")
    attempt.add_argument("work")
    attempt.add_argument("--notes", default="")
    earning = sub.add_parser("add")
    earning.add_argument("platform")
    earning.add_argument("amount", type=float)
    earning.add_argument("work")
    earning.add_argument("--notes", default="")
    args = parser.parse_args()

    tracker = EarningsTracker(args.data_file)
    if args.command in (None, "stats"):
        tracker.display_dashboard()
    elif args.command == "attempt":
        tracker.add_attempt(args.platform, args.work, args.notes)
        print("Attempt recorded.")
    elif args.command == "add":
        tracker.add_earnings(args.platform, args.amount, args.work, args.notes)
        print(f"Recorded ${args.amount:.2f} from {args.platform}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
