#!/usr/bin/env python3
"""Build machine-readable dashboard data from repository state."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "site-data"


def load_cases() -> list[dict]:
    cases = []
    base = ROOT / "research" / "active-puzzles"
    if not base.exists():
        return cases
    for case_file in sorted(base.glob("*/case.json")):
        try:
            data = json.loads(case_file.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        data["repo_path"] = str(case_file.parent.relative_to(ROOT))
        cases.append(data)
    return cases


def build_status(cases: list[dict]) -> dict:
    tools = json.loads((ROOT / "data" / "tools.json").read_text(encoding="utf-8"))
    opportunities = json.loads((ROOT / "data" / "opportunities.json").read_text(encoding="utf-8"))
    prompts = json.loads((ROOT / "data" / "prompts.json").read_text(encoding="utf-8"))
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "active_cases": len(cases),
        "tools": len(tools.get("items", [])),
        "opportunities": len(opportunities.get("items", [])),
        "prompts": len(prompts.get("prompts", [])),
    }


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    cases = load_cases()
    (OUT / "cases.json").write_text(json.dumps({"items": cases}, indent=2) + "\n", encoding="utf-8")
    (OUT / "status.json").write_text(json.dumps(build_status(cases), indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
