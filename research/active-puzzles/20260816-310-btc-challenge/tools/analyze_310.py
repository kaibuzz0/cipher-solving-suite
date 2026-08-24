#!/usr/bin/env python3
"""Portable, non-destructive image analysis for the 310 BTC challenge."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageStat

KNOWN_CHARS = "L3CEO275KOD899D4FA1F64"
HEX_GRID = [
    "511", "B20", "332", "328", "410", "530",
    "22B", "0FE", "52E", "D0F", "7A1", "65B",
    "52C", "7E7", "511", "2F6", "56F", "C4B",
]


class BTC310Analyzer:
    """Deterministic image statistics and legacy-hypothesis checks for case 310."""

    def __init__(self, image_path: str | Path):
        self.image_path = Path(image_path).expanduser().resolve()
        if not self.image_path.is_file():
            raise FileNotFoundError(f"image not found: {self.image_path}")
        with Image.open(self.image_path) as source:
            self.img = source.convert("RGB")
        self.arr = np.array(self.img)

    def color_distribution(self) -> dict[str, object]:
        stat = ImageStat.Stat(self.img)
        return {
            "mean": [round(value, 6) for value in stat.mean[:3]],
            "rms": [round(value, 6) for value in stat.rms[:3]],
            "extrema": [[int(low), int(high)] for low, high in stat.extrema[:3]],
        }

    def scan_for_text_patterns(self, minimum_length: int = 4) -> list[str]:
        """Return sorted unique printable byte runs from RGB sample bytes."""
        runs: list[str] = []
        current: list[str] = []
        for value in self.arr.flatten():
            number = int(value)
            if 32 <= number <= 126:
                current.append(chr(number))
            else:
                if len(current) >= minimum_length:
                    runs.append("".join(current))
                current = []
        if len(current) >= minimum_length:
            runs.append("".join(current))
        return sorted(set(runs))

    def known_pattern_summary(self) -> dict[str, object]:
        flattened_values = {int(value) for value in self.arr.flatten()}
        matched = [value for value in HEX_GRID if int(value, 16) in flattened_values]
        return {
            "known_characters": KNOWN_CHARS,
            "hex_grid": list(HEX_GRID),
            "hex_values_present_as_single_channel_samples": matched,
            "note": "Legacy hint values are hypotheses; presence in pixel samples is not evidence of a solve.",
        }

    def lsb_summary(self) -> dict[str, object]:
        channels: dict[str, object] = {}
        for index, name in enumerate(("R", "G", "B")):
            lsb = self.arr[:, :, index] & 1
            ratio = float(np.mean(lsb))
            channels[name] = {
                "ones_ratio": round(ratio, 9),
                "deviation_from_half": round(abs(ratio - 0.5), 9),
            }
        return channels

    def analysis(self) -> dict[str, object]:
        return {
            "mode": "310-image-analysis",
            "image": str(self.image_path),
            "width": int(self.img.width),
            "height": int(self.img.height),
            "color": self.color_distribution(),
            "text_patterns": self.scan_for_text_patterns(),
            "lsb": self.lsb_summary(),
            "legacy_hints": self.known_pattern_summary(),
            "claim_boundary": "Analysis output is exploratory evidence only and does not establish hidden data, a key, or a puzzle solve.",
        }

    def write_derived_images(self, output_dir: str | Path) -> list[str]:
        """Write derived channel/difference images only to an explicit directory."""
        destination = Path(output_dir).expanduser().resolve()
        destination.mkdir(parents=True, exist_ok=True)
        written: list[str] = []

        for index, name in enumerate(("r", "g", "b")):
            path = destination / f"channel_{name}.png"
            Image.fromarray(self.arr[:, :, index]).save(path)
            written.append(str(path))

        green = self.arr[:, :, 1].astype(np.int16)
        if green.shape[0] > 1 and green.shape[1] > 1:
            difference = np.abs(green[:-1, :-1] - green[1:, 1:]).astype(np.uint8)
        else:
            difference = np.zeros((1, 1), dtype=np.uint8)
        diff_path = destination / "difference.png"
        Image.fromarray(difference).save(diff_path)
        written.append(str(diff_path))
        return written


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Analyze the 310 BTC challenge image non-destructively")
    parser.add_argument("image", help="Path to an image to analyze")
    parser.add_argument("--json", action="store_true", help="Emit deterministic JSON analysis")
    parser.add_argument(
        "--output-dir",
        help="Explicit directory for derived channel/difference images; no images are written when omitted",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        analyzer = BTC310Analyzer(args.image)
        payload = analyzer.analysis()
        payload["derived_outputs"] = analyzer.write_derived_images(args.output_dir) if args.output_dir else []
    except (FileNotFoundError, OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(payload, sort_keys=True))
    else:
        print(f"Image: {payload['width']}x{payload['height']}")
        print(f"Text patterns: {len(payload['text_patterns'])}")
        for channel, summary in payload["lsb"].items():
            print(f"LSB {channel}: {summary['ones_ratio']:.6f} ones ratio")
        if payload["derived_outputs"]:
            print("Derived outputs:")
            for output in payload["derived_outputs"]:
                print(f"  {output}")
        else:
            print("Derived outputs: none (use --output-dir to write them)")
        print(payload["claim_boundary"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
