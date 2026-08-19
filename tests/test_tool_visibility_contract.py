from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_user_visible_tools_flow_to_command_snapshot(tmp_path):
    registry = load_json(ROOT / "data" / "tools.json")
    expected = {
        item["id"]
        for item in registry["items"]
        if item.get("user_visible", True)
    }

    output = tmp_path / "repo-snapshot.json"
    run = subprocess.run(
        [sys.executable, "scripts/export_command_site_snapshot.py", "--output", str(output)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert run.returncode == 0, run.stdout + run.stderr
    snapshot = load_json(output)
    exported = {item["id"] for item in snapshot["tools"]}

    assert expected <= exported
    assert "opportunity-actionability" in exported


def test_user_visible_tool_sources_are_discoverable_in_repository_browser():
    run = subprocess.run(
        [sys.executable, "scripts/build_site_data.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert run.returncode == 0, run.stdout + run.stderr

    registry = load_json(ROOT / "data" / "tools.json")
    repository = load_json(ROOT / "site-data" / "repository.json")
    indexed = {item["path"] for item in repository["files"]}
    browser_roots = tuple(f"{root}/" for root in repository["roots"])

    expected_paths = {
        item["path"]
        for item in registry["items"]
        if item.get("user_visible", True)
        and str(item.get("path", "")).startswith(browser_roots)
    }
    assert expected_paths <= indexed
    assert "tools/opportunity_actionability.py" in indexed


def test_pages_and_workspace_consume_canonical_tool_registry():
    pages = (ROOT / ".github" / "workflows" / "pages.yml").read_text(encoding="utf-8")
    app = (ROOT / "site" / "app.js").read_text(encoding="utf-8")

    assert "data/tools.json" in pages
    assert "'tools'" in app
    assert "state.tools=tools.items||[]" in app
    assert "renderTools" in app
