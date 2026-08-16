#!/usr/bin/env python3
"""Portable alpha-channel extraction for the 310 BTC challenge."""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from PIL import Image

CASE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_DIR = CASE_ROOT / "evidence" / "generated"


class AlphaExtractor:
    """Extract candidate hidden data from an RGBA image alpha channel."""

    def __init__(self, image_path: str | Path):
        self.image_path = Path(image_path).expanduser().resolve()
        if not self.image_path.is_file():
            raise FileNotFoundError(f"image not found: {self.image_path}")
        self.img = Image.open(self.image_path)
        self.arr = np.array(self.img)
        self.height, self.width = self.arr.shape[:2]
        if self.arr.ndim < 3 or self.arr.shape[2] < 4:
            raise ValueError("image has no alpha channel")
        self.alpha = self.arr[:, :, 3]
        print(f"Image: {self.image_path} ({self.width}x{self.height})")
        print(f"Alpha unique values: {np.unique(self.alpha)}")

    @staticmethod
    def _pack_bits(bits) -> bytes:
        output = []
        for i in range(0, len(bits) - 7, 8):
            byte = 0
            for j in range(8):
                byte = (byte << 1) | int(bits[i + j])
            output.append(byte)
        return bytes(output)

    def extract_alpha_lsb(self) -> bytes:
        return self._pack_bits((self.alpha & 1).flatten())

    def extract_alpha_pattern(self) -> bytes:
        mapping = {253: 0, 254: 1}
        bits = [mapping[int(value)] for value in self.alpha.flatten() if int(value) in mapping]
        return self._pack_bits(bits)

    def extract_2bit_alpha(self) -> bytes:
        vals = (self.alpha & 0b11).flatten()
        print(f"2-bit pattern unique values: {np.unique(vals)}")
        output = []
        for i in range(0, len(vals) - 3, 4):
            byte = (int(vals[i]) << 6) | (int(vals[i + 1]) << 4) | (int(vals[i + 2]) << 2) | int(vals[i + 3])
            output.append(byte)
        return bytes(output)

    def extract_row_310_alpha(self) -> bytes:
        row = 310
        if row >= self.height:
            return b""
        row_alpha = self.alpha[row, :]
        print(f"Row 310 alpha values: {np.unique(row_alpha)}")
        return self._pack_bits((row_alpha & 1).flatten())

    def analyze_alpha_structure(self) -> None:
        print("\n=== ALPHA CHANNEL ANALYSIS ===")
        for row in [0, 100, 200, 310, 500, 1000]:
            if row < self.height:
                values = np.unique(self.alpha[row, :])
                print(f"Row {row}: {len(values)} unique values - {values[:10]}")

    @staticmethod
    def check_for_patterns(data: bytes) -> None:
        printable = bytes(value for value in data if 32 <= value < 127)
        if len(printable) > 10:
            print(f"  Printable ASCII found: {printable[:100]}")
        hex_chars = set("0123456789abcdefABCDEF")
        hex_count = sum(1 for value in data if chr(value) in hex_chars or 32 <= value < 127)
        if data and hex_count > len(data) * 0.8:
            print(f"  High hex-like content: {hex_count}/{len(data)}")
        if len(data) > 32:
            first_32 = data[:32]
            repeats = data.count(first_32)
            if repeats > 1:
                print(f"  Repeating pattern found: {repeats} times")

    def try_all_extracts(self, output_dir: str | Path = DEFAULT_OUTPUT_DIR) -> dict[str, Path]:
        output_dir = Path(output_dir).expanduser().resolve()
        output_dir.mkdir(parents=True, exist_ok=True)
        datasets = {
            "alpha_lsb.bin": self.extract_alpha_lsb(),
            "alpha_pattern.bin": self.extract_alpha_pattern(),
            "alpha_2bit.bin": self.extract_2bit_alpha(),
            "alpha_row310.bin": self.extract_row_310_alpha(),
        }
        written: dict[str, Path] = {}
        for name, data in datasets.items():
            print(f"\n{name}: {len(data)} bytes")
            self.check_for_patterns(data)
            path = output_dir / name
            path.write_bytes(data)
            written[name] = path
        print("\nSaved outputs:")
        for path in written.values():
            print(f"  {path}")
        return written


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Extract alpha-channel candidates from a 310 challenge image")
    parser.add_argument("image", help="Path to the RGBA challenge image")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR), help="Directory for generated .bin outputs")
    parser.add_argument("--analyze-only", action="store_true", help="Inspect alpha structure without writing extracted files")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    extractor = AlphaExtractor(args.image)
    extractor.analyze_alpha_structure()
    if not args.analyze_only:
        extractor.try_all_extracts(args.output_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
