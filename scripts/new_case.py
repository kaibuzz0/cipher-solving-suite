#!/usr/bin/env python3
"""Create a standardized research case directory for a puzzle or opportunity."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES_ROOT = ROOT / "research" / "active-puzzles"


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "case"


def create_case(name: str, case_type: str, source: str, url: str = "", authorization_url: str = "") -> Path:
    now = datetime.now(timezone.utc)
    case_id = f"{now.strftime('%Y%m%d')}-{slugify(name)}"
    case_dir = CASES_ROOT / case_id
    if case_dir.exists():
        raise FileExistsError(f"Case already exists: {case_dir.relative_to(ROOT)}")

    (case_dir / "evidence").mkdir(parents=True)
    metadata = {
        "case_id": case_id,
        "name": name,
        "type": case_type,
        "status": "new",
        "created_at": now.isoformat(),
        "updated_at": now.isoformat(),
        "source": source,
        "source_url": url,
        "authorization_url": authorization_url,
        "authorization_required": case_type.lower() in {"bug-bounty", "audit", "security", "pentest"},
        "owner": "unclaimed",
        "tags": [],
        "evidence": [],
        "next_action": "Triage source material and record the smallest reproducible next experiment."
    }
    (case_dir / "case.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

    readme = f"""# {name}\n\n- **Case ID:** `{case_id}`\n- **Type:** `{case_type}`\n- **Status:** `new`\n- **Source:** {source}\n- **Source URL:** {url or 'not recorded'}\n- **Authorization / scope URL:** {authorization_url or 'not recorded'}\n- **Owner:** unclaimed\n\n## Intake checklist\n\n- [ ] Confirm source and timestamp.\n- [ ] Confirm authorization/scope if security testing is involved.\n- [ ] Preserve allowed source material in `evidence/` and record hashes.\n- [ ] Record initial observations in `notes.md`.\n- [ ] Choose the smallest reproducible next experiment.\n- [ ] Append every meaningful experiment to `attempts.md`.\n- [ ] Update `case.json` status/next_action as the case changes.\n\n## Current hypothesis\n\nNot yet triaged.\n\n## Next action\n\nTriage source material and record the smallest reproducible next experiment.\n"""
    (case_dir / "README.md").write_text(readme, encoding="utf-8")
    (case_dir / "notes.md").write_text(f"# Notes — {name}\n\nAppend timestamped observations and hypotheses here.\n", encoding="utf-8")
    (case_dir / "attempts.md").write_text(
        f"# Attempts — {name}\n\nKeep failed attempts. Record timestamp, agent, tool/command, parameters, result, and interpretation.\n",
        encoding="utf-8",
    )
    (case_dir / "evidence" / ".gitkeep").write_text("", encoding="utf-8")
    return case_dir


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create a standardized challenge/opportunity case")
    parser.add_argument("--name", required=True)
    parser.add_argument("--type", required=True, dest="case_type")
    parser.add_argument("--source", required=True)
    parser.add_argument("--url", default="")
    parser.add_argument("--authorization-url", default="")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        case_dir = create_case(args.name, args.case_type, args.source, args.url, args.authorization_url)
    except FileExistsError as exc:
        print(exc)
        return 2
    print(f"Created case: {case_dir.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
