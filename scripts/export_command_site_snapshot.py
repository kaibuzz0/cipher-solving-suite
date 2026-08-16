#!/usr/bin/env python3
"""Export a bounded repository snapshot for the central GitHub Command Site.

The snapshot is public metadata derived from canonical repository registries and
already-generated dashboard data. It intentionally excludes file bodies,
credentials, secrets, private data, and arbitrary scan output.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE_DATA = ROOT / "site-data"


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


def list_from(path: Path, key: str) -> list:
    value = load_json(path).get(key, [])
    return value if isinstance(value, list) else []


def git(*args: str) -> str:
    try:
        return subprocess.check_output(["git", *args], cwd=ROOT, text=True, stderr=subprocess.DEVNULL).strip()
    except (OSError, subprocess.CalledProcessError):
        return ""


def ensure_generated_data() -> None:
    required = [
        SITE_DATA / "status.json",
        SITE_DATA / "toolsets.json",
        SITE_DATA / "cases.json",
        SITE_DATA / "sources.json",
        SITE_DATA / "artifacts.json",
    ]
    if not all(path.exists() for path in required):
        subprocess.check_call([sys.executable, "scripts/build_site_data.py"], cwd=ROOT)
    if not (SITE_DATA / "agent-ops.json").exists():
        subprocess.check_call([sys.executable, "scripts/build_agent_ops.py"], cwd=ROOT)


def recent_activity(limit: int = 12) -> list[dict]:
    raw = git("log", f"-{limit}", "--pretty=format:%H%x1f%aI%x1f%s")
    if not raw:
        return []
    items = []
    for line in raw.splitlines():
        parts = line.split("\x1f", 2)
        if len(parts) != 3:
            continue
        sha, timestamp, title = parts
        items.append(
            {
                "id": sha,
                "type": "commit",
                "title": title,
                "timestamp": timestamp,
                "url": f"https://github.com/kaibuzz0/cipher-solving-suite/commit/{sha}",
            }
        )
    return items


def build_snapshot() -> dict:
    ensure_generated_data()
    commit = git("rev-parse", "HEAD") or "unknown-commit"
    status = load_json(SITE_DATA / "status.json")
    return {
        "schema_version": 1,
        "generated_at": now_iso(),
        "source_commit": commit,
        "repo": {
            "id": "cipher-solving-suite",
            "full_name": "kaibuzz0/cipher-solving-suite",
            "url": "https://github.com/kaibuzz0/cipher-solving-suite",
            "default_branch": "main",
            "description": "Multi-agent cipher, puzzle, research, opportunity-intelligence, and reusable toolset workspace.",
            "visibility": "public",
            "pages_url": "https://kaibuzz0.github.io/cipher-solving-suite/",
        },
        "stats": status,
        "tools": list_from(ROOT / "data" / "tools.json", "items"),
        "toolsets": list_from(SITE_DATA / "toolsets.json", "items"),
        "cases": list_from(SITE_DATA / "cases.json", "items"),
        "opportunities": list_from(ROOT / "data" / "opportunities.json", "items"),
        "intelligence": list_from(ROOT / "data" / "intelligence.json", "items"),
        "sources": list_from(SITE_DATA / "sources.json", "sources"),
        "prompts": list_from(ROOT / "data" / "prompts.json", "prompts"),
        "evidence": list_from(SITE_DATA / "artifacts.json", "items"),
        "agent_ops": load_json(SITE_DATA / "agent-ops.json"),
        "activity": recent_activity(),
        "links": [
            {"id": "github", "name": "GitHub repository", "url": "https://github.com/kaibuzz0/cipher-solving-suite"},
            {"id": "pages", "name": "Operations workspace", "url": "https://kaibuzz0.github.io/cipher-solving-suite/"},
            {"id": "actions", "name": "GitHub Actions", "url": "https://github.com/kaibuzz0/cipher-solving-suite/actions"},
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Export GitHub Command Site repository snapshot")
    parser.add_argument("--output", default="site-data/repo-snapshot.json")
    args = parser.parse_args()
    output = ROOT / args.output if not Path(args.output).is_absolute() else Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    snapshot = build_snapshot()
    output.write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")
    collections = ("tools", "toolsets", "cases", "opportunities", "intelligence", "sources", "prompts", "evidence", "activity")
    print(json.dumps({
        "output": str(output),
        "repo": snapshot["repo"]["id"],
        "source_commit": snapshot["source_commit"],
        "counts": {key: len(snapshot[key]) for key in collections},
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
