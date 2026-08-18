#!/usr/bin/env python3
"""Evaluate whether an opportunity is actionable at an explicit point in time.

This tool deliberately separates broad lifecycle labels (for example, a discovery
page saying a challenge is "active") from the narrower question of whether a
user can still enter or submit. Evaluation is deterministic because callers must
provide ``--as-of``; the tool never infers freshness from HTTP reachability and
never mutates canonical catalogs.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


CLOSED_VALUES = {"closed", "ended", "complete", "completed", "submissions-closed"}
OPEN_VALUES = {"open", "accepting", "accepting-submissions", "live"}
UPCOMING_VALUES = {"upcoming", "not-open", "not-open-yet"}


@dataclass(frozen=True)
class Evaluation:
    id: str
    lifecycle_status: str
    submission_status: str
    submission_deadline: str
    state: str
    actionable: bool
    reason: str


def parse_time(value: str) -> datetime:
    text = value.strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    dt = datetime.fromisoformat(text)
    if dt.tzinfo is None:
        raise ValueError("timestamp must include timezone information")
    return dt.astimezone(timezone.utc)


def normalize(value: Any) -> str:
    return str(value or "").strip().lower().replace("_", "-").replace(" ", "-")


def evaluate_item(item: dict[str, Any], as_of: datetime) -> Evaluation:
    item_id = str(item.get("id") or item.get("name") or "unknown")
    lifecycle_raw = str(item.get("lifecycle_status") or "")
    submission_raw = str(item.get("submission_status") or "")
    deadline_raw = str(item.get("submission_deadline") or "")
    lifecycle = normalize(lifecycle_raw)
    submission = normalize(submission_raw)

    if submission in CLOSED_VALUES:
        return Evaluation(item_id, lifecycle_raw, submission_raw, deadline_raw, "closed", False,
                          "explicit submission status is closed")

    deadline = None
    if deadline_raw:
        deadline = parse_time(deadline_raw)
        if as_of > deadline:
            return Evaluation(item_id, lifecycle_raw, submission_raw, deadline_raw, "closed", False,
                              "submission deadline has passed")

    if submission in UPCOMING_VALUES:
        return Evaluation(item_id, lifecycle_raw, submission_raw, deadline_raw, "upcoming", False,
                          "submission phase is not open yet")

    if submission in OPEN_VALUES:
        if deadline is None:
            return Evaluation(item_id, lifecycle_raw, submission_raw, deadline_raw, "verify", False,
                              "submission status says open but no deadline is preserved")
        return Evaluation(item_id, lifecycle_raw, submission_raw, deadline_raw, "open", True,
                          "submission status is open and deadline has not passed")

    if lifecycle in CLOSED_VALUES:
        return Evaluation(item_id, lifecycle_raw, submission_raw, deadline_raw, "closed", False,
                          "overall lifecycle is closed")

    if lifecycle in OPEN_VALUES or lifecycle == "active":
        return Evaluation(item_id, lifecycle_raw, submission_raw, deadline_raw, "verify", False,
                          "broad lifecycle is active but current submission phase is not proven")

    return Evaluation(item_id, lifecycle_raw, submission_raw, deadline_raw, "unknown", False,
                      "insufficient phase/deadline evidence")


def load_items(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        items = data
    elif isinstance(data, dict) and isinstance(data.get("items"), list):
        items = data["items"]
    else:
        raise ValueError("input must be a JSON list or an object containing an items list")
    if not all(isinstance(item, dict) for item in items):
        raise ValueError("every item must be a JSON object")
    return items


def build_report(items: list[dict[str, Any]], as_of: datetime) -> dict[str, Any]:
    evaluations = [evaluate_item(item, as_of) for item in items]
    counts: dict[str, int] = {}
    for item in evaluations:
        counts[item.state] = counts.get(item.state, 0) + 1
    return {
        "schema_version": 1,
        "as_of": as_of.isoformat().replace("+00:00", "Z"),
        "summary": {"total": len(evaluations), "states": dict(sorted(counts.items()))},
        "items": [asdict(item) for item in evaluations],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="JSON file containing opportunity records")
    parser.add_argument("--as-of", required=True, help="Explicit ISO-8601 timestamp used for deterministic evaluation")
    parser.add_argument("--output", help="Optional path for the JSON report")
    args = parser.parse_args(argv)

    try:
        as_of = parse_time(args.as_of)
        report = build_report(load_items(Path(args.input)), as_of)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        parser.error(str(exc))

    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
