from __future__ import annotations

import base64
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "research" / "active-puzzles" / "20260816-310-btc-challenge" / "tools" / "password_candidate_solver.py"


def run_solver(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def test_list_candidates_is_deterministic_and_direct_script_safe() -> None:
    first = run_solver("--list-candidates", "--json")
    second = run_solver("--list-candidates", "--json")
    assert first.returncode == 0, first.stderr
    assert second.returncode == 0, second.stderr
    assert first.stdout == second.stdout

    payload = json.loads(first.stdout)
    assert payload["count"] == len(payload["candidates"])
    assert payload["candidates"][0] == "L3CEO275KOD899D4FA1F64"
    assert len(payload["candidates"]) == len(set(payload["candidates"]))


def test_limit_preserves_order() -> None:
    result = run_solver("--list-candidates", "--json", "--limit", "3")
    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    assert payload == {
        "count": 3,
        "candidates": [
            "L3CEO275KOD899D4FA1F64",
            "l3ceo275kod899d4fa1f64",
            "511B2033232841053022B0FE52ED0F7A165B52C7E75112F656FC4B",
        ],
    }


def test_invalid_base64_fails_without_writing_output(tmp_path: Path) -> None:
    source = tmp_path / "bad.b64"
    output = tmp_path / "result.json"
    source.write_text("%%% not base64 %%%", encoding="utf-8")

    result = run_solver("--payload", str(source), "--output", str(output))
    assert result.returncode == 2
    assert "invalid base64 payload" in result.stderr
    assert not output.exists()


def test_non_openssl_payload_fails_without_writing_output(tmp_path: Path) -> None:
    source = tmp_path / "not-openssl.b64"
    output = tmp_path / "result.json"
    source.write_bytes(base64.b64encode(b"not-an-openssl-payload"))

    result = run_solver("--payload", str(source), "--output", str(output))
    assert result.returncode == 2
    assert "not OpenSSL Salted__ format" in result.stderr
    assert not output.exists()


def test_missing_payload_is_usage_error() -> None:
    result = run_solver()
    assert result.returncode == 2
    assert "--payload is required" in result.stderr
