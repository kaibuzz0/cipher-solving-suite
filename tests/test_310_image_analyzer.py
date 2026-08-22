from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "research" / "active-puzzles" / "20260816-310-btc-challenge" / "tools" / "analyze_310.py"


def run_analyzer(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def write_ppm(path: Path) -> None:
    path.write_text(
        "P3\n"
        "2 2\n"
        "255\n"
        "0 0 0   255 255 255\n"
        "64 65 66   32 33 34\n",
        encoding="ascii",
    )


def test_direct_script_json_is_deterministic_and_write_free_by_default(tmp_path: Path) -> None:
    fixture = tmp_path / "fixture.ppm"
    write_ppm(fixture)

    first = run_analyzer(str(fixture), "--json")
    second = run_analyzer(str(fixture), "--json")

    assert first.returncode == 0, first.stderr
    assert second.returncode == 0, second.stderr
    assert first.stdout == second.stdout
    payload = json.loads(first.stdout)
    assert payload["mode"] == "310-image-analysis"
    assert payload["width"] == 2
    assert payload["height"] == 2
    assert payload["derived_outputs"] == []
    assert not (ROOT / "channel_r.png").exists()
    assert not (ROOT / "difference.png").exists()


def test_explicit_output_dir_contains_only_managed_derived_images(tmp_path: Path) -> None:
    fixture = tmp_path / "fixture.ppm"
    output_dir = tmp_path / "derived"
    write_ppm(fixture)

    result = run_analyzer(str(fixture), "--json", "--output-dir", str(output_dir))

    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    expected = {
        output_dir / "channel_r.png",
        output_dir / "channel_g.png",
        output_dir / "channel_b.png",
        output_dir / "difference.png",
    }
    assert {Path(path) for path in payload["derived_outputs"]} == expected
    assert all(path.is_file() for path in expected)


def test_flat_image_difference_is_safe(tmp_path: Path) -> None:
    fixture = tmp_path / "flat.ppm"
    fixture.write_text("P3\n1 1\n255\n10 10 10\n", encoding="ascii")
    output_dir = tmp_path / "derived"

    result = run_analyzer(str(fixture), "--json", "--output-dir", str(output_dir))

    assert result.returncode == 0, result.stderr
    assert (output_dir / "difference.png").is_file()


def test_missing_image_fails_non_destructively(tmp_path: Path) -> None:
    output_dir = tmp_path / "derived"
    result = run_analyzer(str(tmp_path / "missing.png"), "--json", "--output-dir", str(output_dir))

    assert result.returncode == 2
    assert "image not found" in result.stderr
    assert not output_dir.exists()


def test_claim_boundary_and_legacy_hint_are_explicit(tmp_path: Path) -> None:
    fixture = tmp_path / "fixture.ppm"
    write_ppm(fixture)

    result = run_analyzer(str(fixture), "--json")

    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    assert payload["legacy_hints"]["known_characters"] == "L3CEO275KOD899D4FA1F64"
    assert "does not establish" in payload["claim_boundary"]
    assert "not evidence of a solve" in payload["legacy_hints"]["note"]
