from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "verify_310_reproduction.py"


def load_module():
    spec = importlib.util.spec_from_file_location("verify_310_reproduction", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def write_stub_extractor(path: Path, payloads: dict[str, bytes], corrupt: str | None = None) -> None:
    encoded = {name: data.hex() for name, data in payloads.items()}
    path.write_text(
        "from pathlib import Path\n"
        "import argparse\n"
        f"PAYLOADS = {encoded!r}\n"
        "p=argparse.ArgumentParser(); p.add_argument('image'); p.add_argument('--output-dir', required=True); a=p.parse_args()\n"
        "out=Path(a.output_dir); out.mkdir(parents=True, exist_ok=True)\n"
        f"corrupt={corrupt!r}\n"
        "for name, value in PAYLOADS.items():\n"
        "    data=bytes.fromhex(value)\n"
        "    if name == corrupt: data += b'X'\n"
        "    (out / name).write_bytes(data)\n",
        encoding="utf-8",
    )


def fixture_paths(tmp_path: Path):
    module = load_module()
    image = tmp_path / "challenge.png"
    image.write_bytes(b"synthetic-primary-evidence")
    expected_dir = tmp_path / "expected"
    expected_dir.mkdir()
    payloads = {name: f"payload:{name}".encode() for name in module.OUTPUT_NAMES}
    for name, data in payloads.items():
        (expected_dir / name).write_bytes(data)
    extractor = tmp_path / "extractor.py"
    report = tmp_path / "report.json"
    return module, image, expected_dir, payloads, extractor, report


def test_verify_matches_without_mutating_expected_evidence(tmp_path):
    module, image, expected_dir, payloads, extractor, report = fixture_paths(tmp_path)
    before = {name: (expected_dir / name).read_bytes() for name in payloads}
    write_stub_extractor(extractor, payloads)

    result = module.verify(image, extractor, expected_dir, report)

    assert result["status"] == "pass"
    assert not result["errors"]
    assert all(item["match"] for item in result["outputs"])
    assert before == {name: (expected_dir / name).read_bytes() for name in payloads}
    assert json.loads(report.read_text(encoding="utf-8"))["status"] == "pass"


def test_verify_fails_on_regenerated_mismatch(tmp_path):
    module, image, expected_dir, payloads, extractor, report = fixture_paths(tmp_path)
    mismatch = module.OUTPUT_NAMES[-1]
    write_stub_extractor(extractor, payloads, corrupt=mismatch)

    result = module.verify(image, extractor, expected_dir, report)

    assert result["status"] == "fail"
    assert f"reproduction mismatch: {mismatch}" in result["errors"]
    output = next(item for item in result["outputs"] if item["name"] == mismatch)
    assert output["match"] is False
    assert output["expected_sha256"] != output["regenerated_sha256"]


def test_verify_fails_closed_when_required_input_is_missing(tmp_path):
    module, image, expected_dir, payloads, extractor, report = fixture_paths(tmp_path)
    write_stub_extractor(extractor, payloads)
    image.unlink()

    result = module.verify(image, extractor, expected_dir, report)

    assert result["status"] == "fail"
    assert result["outputs"] == []
    assert any("required path missing" in error for error in result["errors"])
    assert json.loads(report.read_text(encoding="utf-8"))["status"] == "fail"
