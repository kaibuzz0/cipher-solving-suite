#!/usr/bin/env python3
"""Build machine-readable dashboard data from repository state."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "site-data"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_cases() -> list[dict]:
    cases = []
    base = ROOT / "research" / "active-puzzles"
    if not base.exists():
        return cases
    for case_file in sorted(base.glob("*/case.json")):
        try:
            data = load_json(case_file)
        except (OSError, json.JSONDecodeError):
            continue
        data["repo_path"] = str(case_file.parent.relative_to(ROOT))
        cases.append(data)
    return cases


def build_status(cases: list[dict]) -> dict:
    tools = load_json(ROOT / "data" / "tools.json")
    opportunities = load_json(ROOT / "data" / "opportunities.json")
    prompts = load_json(ROOT / "data" / "prompts.json")
    intelligence = load_json(ROOT / "data" / "intelligence.json")
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "active_cases": len(cases),
        "tools": len(tools.get("items", [])),
        "opportunities": len(opportunities.get("items", [])),
        "prompts": len(prompts.get("prompts", [])),
        "intelligence": len(intelligence.get("items", [])),
    }


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    cases = load_cases()
    (OUT / "cases.json").write_text(json.dumps({"items": cases}, indent=2) + "\n", encoding="utf-8")
    (OUT / "status.json").write_text(json.dumps(build_status(cases), indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
