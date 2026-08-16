#!/usr/bin/env python3
"""Build machine-readable dashboard data from repository state."""
from __future__ import annotations

import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.artifact_inventory import build_inventory
from scripts.source_check_history import build_report as build_collection_report

OUT = ROOT / "site-data"

SAFE_PREVIEW_SUFFIXES = {
    ".md", ".txt", ".json", ".py", ".yml", ".yaml", ".toml", ".ini", ".cfg",
    ".js", ".css", ".html", ".sh", ".ps1", ".sql", ".csv",
}
BROWSER_ROOTS = (
    "toolsets",
    "tools",
    "scripts",
    "docs",
    "research/active-puzzles",
    "data",
)
MAX_PREVIEW_BYTES = 120_000
MAX_PREVIEW_CHARS = 14_000


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_iso(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


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


def safe_preview(path: Path) -> tuple[str, bool]:
    """Return a bounded UTF-8 preview for safe public text files."""
    try:
        size = path.stat().st_size
    except OSError:
        return "", False
    if path.suffix.lower() not in SAFE_PREVIEW_SUFFIXES or size > MAX_PREVIEW_BYTES:
        return "", False
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return "", False
    truncated = len(text) > MAX_PREVIEW_CHARS
    if truncated:
        text = text[:MAX_PREVIEW_CHARS] + "\n\n… preview truncated …\n"
    return text, truncated


def build_repository_browser() -> dict:
    """Build a bounded static index used by the VS Code-style file browser.

    The repository is public, but previews are still intentionally limited to
    known text extensions and bounded sizes so Pages does not become a binary
    mirror or accidentally inline oversized generated artifacts.
    """
    generated_at = datetime.now(timezone.utc).isoformat()
    files: list[dict] = []
    directories: set[str] = set()

    for root_name in BROWSER_ROOTS:
        base = ROOT / root_name
        if not base.exists():
            continue
        directories.add(root_name)
        for path in sorted(base.rglob("*")):
            try:
                rel = path.relative_to(ROOT).as_posix()
            except ValueError:
                continue
            if path.is_dir():
                directories.add(rel)
                continue
            if not path.is_file():
                continue
            try:
                size = path.stat().st_size
            except OSError:
                size = 0
            preview, truncated = safe_preview(path)
            parent = path.parent.relative_to(ROOT).as_posix()
            files.append(
                {
                    "path": rel,
                    "name": path.name,
                    "parent": parent,
                    "suffix": path.suffix.lower(),
                    "size": size,
                    "previewable": bool(preview),
                    "preview_truncated": truncated,
                    "preview": preview,
                }
            )

    files.sort(key=lambda item: item["path"].lower())
    return {
        "generated_at": generated_at,
        "roots": list(BROWSER_ROOTS),
        "summary": {
            "files": len(files),
            "directories": len(directories),
            "previewable": sum(1 for item in files if item["previewable"]),
        },
        "directories": sorted(directories, key=str.lower),
        "files": files,
    }


def load_toolsets(repository: dict | None = None) -> dict:
    """Discover toolsets from manifests and reconcile them with the catalog.

    The website intentionally scans manifests as well as the catalog. That means a
    newly added toolset becomes visible even if an agent forgot to register it;
    the UI can then flag it as unregistered instead of silently hiding it.
    """
    now = datetime.now(timezone.utc)
    base = ROOT / "toolsets"
    catalog_path = base / "catalog.json"
    catalog = {"toolsets": []}
    if catalog_path.exists():
        try:
            catalog = load_json(catalog_path)
        except (OSError, json.JSONDecodeError):
            catalog = {"toolsets": []}

    tools = load_json(ROOT / "data" / "tools.json").get("items", [])
    repo_files = (repository or {}).get("files", [])
    catalog_by_id = {
        item.get("id"): item
        for item in catalog.get("toolsets", [])
        if isinstance(item, dict) and item.get("id")
    }
    items: dict[str, dict] = {}

    if base.exists():
        for manifest_path in sorted(base.glob("*/toolset.json")):
            try:
                manifest = load_json(manifest_path)
            except (OSError, json.JSONDecodeError):
                continue
            toolset_id = manifest.get("id") or manifest_path.parent.name
            catalog_item = catalog_by_id.get(toolset_id, {})
            repo_path = str(manifest_path.parent.relative_to(ROOT)).replace("\\", "/")
            entrypoint = manifest.get("entrypoint") or catalog_item.get("entrypoint", "")
            entrypoint_name = entrypoint.split()[-1] if entrypoint else ""
            entrypoint_path = manifest_path.parent / entrypoint_name if entrypoint_name else None
            readme = manifest_path.parent / "README.md"
            registered = toolset_id in catalog_by_id
            health = "ok"
            warnings = []
            if not registered:
                health = "needs-registration"
                warnings.append("manifest exists but toolset is missing from toolsets/catalog.json")
            if entrypoint_path and not entrypoint_path.exists():
                health = "incomplete"
                warnings.append(f"entrypoint not found: {entrypoint_name}")
            if not readme.exists():
                if health == "ok":
                    health = "incomplete"
                warnings.append("README.md is missing")

            related_files = [
                f["path"] for f in repo_files
                if f.get("path", "").startswith(repo_path + "/")
            ]
            related_tools = [
                tool for tool in tools
                if str(tool.get("path", "")).replace("\\", "/").startswith(repo_path + "/")
            ]

            items[toolset_id] = {
                **catalog_item,
                **manifest,
                "id": toolset_id,
                "path": repo_path,
                "manifest_path": str(manifest_path.relative_to(ROOT)).replace("\\", "/"),
                "readme_path": str(readme.relative_to(ROOT)).replace("\\", "/") if readme.exists() else "",
                "registered": registered,
                "health": health,
                "warnings": warnings,
                "files": related_files,
                "tools": related_tools,
            }

    for toolset_id, catalog_item in catalog_by_id.items():
        if toolset_id in items:
            continue
        repo_path = catalog_item.get("path", f"toolsets/{toolset_id}")
        items[toolset_id] = {
            **catalog_item,
            "id": toolset_id,
            "path": repo_path,
            "manifest_path": "",
            "readme_path": "",
            "registered": True,
            "health": "missing-manifest",
            "warnings": ["catalog entry exists but toolset.json was not found"],
            "files": [],
            "tools": [],
        }

    ordered = sorted(items.values(), key=lambda x: (x.get("name") or x.get("id") or "").lower())
    summary = {
        "total": len(ordered),
        "registered": sum(1 for x in ordered if x.get("registered")),
        "healthy": sum(1 for x in ordered if x.get("health") == "ok"),
        "needs_attention": sum(1 for x in ordered if x.get("health") != "ok"),
    }
    return {"generated_at": now.isoformat(), "summary": summary, "items": ordered}


def source_state(source: dict, now: datetime) -> str:
    if not source.get("enabled", True):
        return "disabled"
    last = parse_iso(source.get("last_checked_at"))
    if last is None:
        return "never-checked"
    freshness = int(source.get("freshness_hours", 24))
    due = last + timedelta(hours=freshness)
    if now >= due:
        return "due"
    if due - now <= timedelta(hours=max(1, freshness // 4)):
        return "due-soon"
    return "fresh"


def build_source_status() -> dict:
    now = datetime.now(timezone.utc)
    registry = load_json(ROOT / "data" / "intelligence_sources.json")
    counts = {"fresh": 0, "due-soon": 0, "due": 0, "never-checked": 0, "disabled": 0}
    items = []
    for source in registry.get("sources", []):
        state = source_state(source, now)
        counts[state] = counts.get(state, 0) + 1
        items.append({**source, "freshness_state": state})
    items.sort(key=lambda x: (x.get("freshness_state", ""), x.get("name", "")))
    return {"generated_at": now.isoformat(), "counts": counts, "sources": items}


def build_status(
    cases: list[dict],
    source_status: dict,
    collection: dict,
    artifacts: dict,
    toolsets: dict,
    repository: dict,
) -> dict:
    tools = load_json(ROOT / "data" / "tools.json")
    opportunities = load_json(ROOT / "data" / "opportunities.json")
    prompts = load_json(ROOT / "data" / "prompts.json")
    intelligence = load_json(ROOT / "data" / "intelligence.json")
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "active_cases": len(cases),
        "tools": len(tools.get("items", [])),
        "toolsets": toolsets.get("summary", {}).get("total", 0),
        "toolsets_needing_attention": toolsets.get("summary", {}).get("needs_attention", 0),
        "repository_files": repository.get("summary", {}).get("files", 0),
        "previewable_files": repository.get("summary", {}).get("previewable", 0),
        "opportunities": len(opportunities.get("items", [])),
        "prompts": len(prompts.get("prompts", [])),
        "intelligence": len(intelligence.get("items", [])),
        "intelligence_sources": len(source_status.get("sources", [])),
        "sources_due": source_status.get("counts", {}).get("due", 0)
        + source_status.get("counts", {}).get("never-checked", 0),
        "sources_changed": collection.get("summary", {}).get("changed_sources", 0),
        "source_history_entries": collection.get("summary", {}).get("history_entries", 0),
        "artifacts": artifacts.get("summary", {}).get("total", 0),
        "artifacts_review_before_move": artifacts.get("summary", {}).get("review_before_move", 0),
    }


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    cases = load_cases()
    repository = build_repository_browser()
    toolsets = load_toolsets(repository)
    source_status = build_source_status()
    collection = build_collection_report()
    artifacts = build_inventory()
    (OUT / "cases.json").write_text(json.dumps({"items": cases}, indent=2) + "\n", encoding="utf-8")
    (OUT / "toolsets.json").write_text(json.dumps(toolsets, indent=2) + "\n", encoding="utf-8")
    (OUT / "repository.json").write_text(json.dumps(repository, indent=2) + "\n", encoding="utf-8")
    (OUT / "sources.json").write_text(json.dumps(source_status, indent=2) + "\n", encoding="utf-8")
    (OUT / "collection-health.json").write_text(json.dumps(collection, indent=2) + "\n", encoding="utf-8")
    (OUT / "artifacts.json").write_text(json.dumps(artifacts, indent=2) + "\n", encoding="utf-8")
    (OUT / "status.json").write_text(
        json.dumps(build_status(cases, source_status, collection, artifacts, toolsets, repository), indent=2) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
