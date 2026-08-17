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
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
SITE_DATA = ROOT / "site-data"
MAX_REPOSITORY_FILES = 5000
MAX_REPOSITORY_DIRECTORIES = 2500


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


def repository_tree() -> dict:
    raw = git("ls-files", "-z")
    files = sorted(x for x in raw.split("\0") if x)
    directory_counts: dict[str, int] = {}
    for file_path in files:
        parts = PurePosixPath(file_path).parts
        for index in range(1, len(parts)):
            directory = "/".join(parts[:index])
            directory_counts[directory] = directory_counts.get(directory, 0) + 1
    directories = [
        {
            "path": path,
            "name": PurePosixPath(path).name,
            "depth": len(PurePosixPath(path).parts),
            "file_count": count,
        }
        for path, count in sorted(directory_counts.items())[:MAX_REPOSITORY_DIRECTORIES]
    ]
    exported_files = [
        {
            "path": path,
            "name": PurePosixPath(path).name,
            "extension": PurePosixPath(path).suffix.lower(),
        }
        for path in files[:MAX_REPOSITORY_FILES]
    ]
    return {
        "total_files": len(files),
        "total_directories": len(directory_counts),
        "files_truncated": len(files) > len(exported_files),
        "directories_truncated": len(directory_counts) > len(directories),
        "top_level": sorted({PurePosixPath(path).parts[0] for path in files if PurePosixPath(path).parts}),
        "directories": directories,
        "files": exported_files,
    }


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
        "repository_tree": repository_tree(),
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
        "repository_tree": {
            "files": snapshot["repository_tree"]["total_files"],
            "directories": snapshot["repository_tree"]["total_directories"],
        },
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
