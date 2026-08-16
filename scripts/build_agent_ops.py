#!/usr/bin/env python3
"""Build structured Agent Ops data from the repository's human/machine handoff surfaces."""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "site-data" / "agent-ops.json"


def read_text(path: str) -> str:
    target = ROOT / path
    return target.read_text(encoding="utf-8") if target.exists() else ""


def section(text: str, heading: str) -> str:
    marker = f"## {heading}"
    if marker not in text:
        return ""
    body = text.split(marker, 1)[1]
    return body.split("\n## ", 1)[0].strip()


def bullets(text: str) -> list[str]:
    return [line[2:].strip() for line in text.splitlines() if line.startswith("- ")]


def numbered(text: str) -> list[str]:
    items = []
    for line in text.splitlines():
        match = re.match(r"^\d+\.\s+(.*)$", line.strip())
        if match:
            items.append(match.group(1).strip())
    return items


def parse_queue(text: str) -> dict:
    body = section(text, "Priority queue")
    items = []
    for line in body.splitlines():
        if not line.startswith("|") or "---" in line or "Priority" in line:
            continue
        cols = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cols) < 5:
            continue
        priority, state, work, owner, next_step = cols[:5]
        items.append({
            "priority": priority,
            "state": state,
            "work": work,
            "owner": owner,
            "next_step": next_step,
        })
    return {
        "items": items,
        "summary": {
            "total": len(items),
            "todo": sum(1 for item in items if item["state"].lower() == "todo"),
            "claimed": sum(1 for item in items if item["owner"].lower() not in {"", "unclaimed"}),
            "p1": sum(1 for item in items if item["priority"].upper() == "P1"),
        },
    }


def parse_handoffs(text: str) -> list[dict]:
    matches = list(re.finditer(r"^###\s+(.+?)\s+—\s+(.+?)\s*/\s*(.+?)\s*$", text, re.MULTILINE))
    entries = []
    field_map = {
        "Branch / PR": "branch_pr",
        "Objective": "objective",
        "Changed": "changed",
        "Verification": "verification",
        "Evidence / artifacts": "evidence",
        "Known risks / blockers": "risks",
        "Next action": "next_action",
    }
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[start:end]
        entry = {
            "timestamp": match.group(1).strip(),
            "agent": match.group(2).strip(),
            "task": match.group(3).strip(),
        }
        for label, key in field_map.items():
            field = re.search(rf"^- \*\*{re.escape(label)}:\*\*\s*(.*)$", body, re.MULTILINE)
            entry[key] = field.group(1).strip() if field else ""
        entries.append(entry)
    return list(reversed(entries))


def parse_current_state(text: str) -> dict:
    reconciled = re.search(r"^Last reconciled:\s*(.+)$", text, re.MULTILINE)
    branch = re.search(r"^Default branch:\s*`?([^`\n]+)`?$", text, re.MULTILINE)
    version = re.search(r"^Repository version:\s*(.+)$", text, re.MULTILINE)
    next_handoff = section(text, "Next handoff")
    return {
        "last_reconciled": reconciled.group(1).strip() if reconciled else "",
        "default_branch": branch.group(1).strip() if branch else "",
        "version": version.group(1).strip() if version else "",
        "verified_health": bullets(section(text, "Verified health")),
        "research_intelligence": bullets(section(text, "Current research/intelligence state")),
        "known_debt": bullets(section(text, "Known state / debt")),
        "priorities": numbered(section(text, "Current operating priorities")),
        "next_handoff": " ".join(line.strip() for line in next_handoff.splitlines() if line.strip()),
    }


def load_integration_queue() -> dict:
    path = ROOT / "data" / "integration_queue.json"
    if not path.exists():
        return {"items": [], "updated_at": ""}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"items": [], "updated_at": "", "error": "invalid integration_queue.json"}
    return {
        "updated_at": payload.get("updated_at", ""),
        "items": payload.get("items", []),
    }


def build_snapshot() -> dict:
    queue = parse_queue(read_text("docs/WORK_QUEUE.md"))
    handoffs = parse_handoffs(read_text("docs/AGENT_HANDOFF.md"))
    current = parse_current_state(read_text("ops/CURRENT_STATE.md"))
    integration = load_integration_queue()
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "queue_total": queue["summary"]["total"],
            "queue_p1": queue["summary"]["p1"],
            "queue_claimed": queue["summary"]["claimed"],
            "handoffs": len(handoffs),
            "integration_items": len(integration.get("items", [])),
            "known_debt": len(current.get("known_debt", [])),
        },
        "queue": queue,
        "recent_handoffs": handoffs[:12],
        "current_state": current,
        "integration_queue": integration,
    }


def main() -> int:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(build_snapshot(), indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
