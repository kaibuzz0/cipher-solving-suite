from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "research" / "active-puzzles" / "20260816-310-btc-challenge" / "tools" / "character_locator.py"


def run_locator(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def write_fixture(path: Path) -> None:
    rows = [
        [0] * 8,
        [0] * 8,
        [0, 255, 0, 255, 0, 255, 0, 255],
        [255, 0, 255, 0, 255, 0, 255, 0],
        [0, 255, 0, 255, 0, 255, 0, 255],
        [0] * 8,
        [0] * 8,
        [0] * 8,
    ]
    pixels = "\n".join(" ".join(str(value) for value in row) for row in rows)
    path.write_text(f"P2\n8 8\n255\n{pixels}\n", encoding="ascii")


def test_hint_summary_is_deterministic_and_dependency_free() -> None:
    first = run_locator("--hint-summary", "--json")
    second = run_locator("--hint-summary", "--json")
    assert first.returncode == 0, first.stderr
    assert second.returncode == 0, second.stderr
    assert first.stdout == second.stdout
    payload = json.loads(first.stdout)
    assert payload["mode"] == "legacy-hint-summary"
    assert payload["known_characters"] == "L3CEO275KOD899D4FA1F64"
    assert payload["character_count"] == 22
    assert "character positions may contain useful ordering information" in payload["legacy_hypotheses"]


def test_p2_fixture_detects_expected_region_via_direct_script(tmp_path: Path) -> None:
    fixture = tmp_path / "edge-fixture.pgm"
    write_fixture(fixture)
    result = run_locator(str(fixture), "--json", "--min-group-rows", "2")
    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    assert payload["mode"] == "edge-density-analysis"
    assert payload["width"] == 8
    assert payload["height"] == 8
    assert payload["selected_rows"] == [2, 3, 4]
    assert payload["regions"] == [
        {"end_row": 4, "max_edge_count": 7, "row_count": 3, "start_row": 2}
    ]


def test_missing_image_fails_without_creating_output(tmp_path: Path) -> None:
    output = tmp_path / "should-not-exist.json"
    result = run_locator(str(tmp_path / "missing.png"), "--json", "--output", str(output))
    assert result.returncode == 2
    assert "image not found" in result.stderr
    assert not output.exists()


def test_image_is_required_without_hint_mode() -> None:
    result = run_locator("--json")
    assert result.returncode == 2
    assert "image is required unless --hint-summary is used" in result.stderr


def test_output_is_written_only_when_explicitly_requested(tmp_path: Path) -> None:
    fixture = tmp_path / "edge-fixture.pgm"
    output = tmp_path / "analysis" / "result.json"
    write_fixture(fixture)
    result = run_locator(str(fixture), "--json", "--min-group-rows", "2", "--output", str(output))
    assert result.returncode == 0, result.stderr
    assert output.exists()
    assert json.loads(output.read_text(encoding="utf-8"))["regions"][0]["start_row"] == 2
