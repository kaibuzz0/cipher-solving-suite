"""Guard GitHub Pages publication when canonical raw intelligence evidence changes."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]


def test_pages_rebuilds_on_raw_intelligence_changes():
    workflow = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
    push_paths = workflow.split("\n    paths:\n", 1)[1].split("\n  workflow_dispatch:", 1)[0]

    assert re.search(r'^\s*-\s*["\']intelligence/\*\*["\']\s*$', push_paths, re.MULTILINE)
    assert "python scripts/build_site_data.py" in workflow
    assert "python scripts/build_agent_ops.py" in workflow
