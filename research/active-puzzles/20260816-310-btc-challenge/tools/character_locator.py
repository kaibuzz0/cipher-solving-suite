#!/usr/bin/env python3
"""Portable, deterministic character-region analysis for the 310 BTC challenge.

The legacy root ``char_locator.py`` mixed challenge hints, hard-coded local paths,
and root-level output side effects.  This case-local replacement keeps the useful
edge-density hypothesis while requiring explicit inputs/outputs.  P2 PGM images
are supported with the Python standard library for deterministic fixtures;
common image formats such as PNG require Pillow and are loaded lazily.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Iterable

KNOWN_CHARACTERS = "L3CEO275KOD899D4FA1F64"
HEX_VALUES = [
    "511", "B20", "332", "328", "410", "530",
    "22B", "0FE", "52E", "D0F", "7A1", "65B",
    "52C", "7E7", "511", "2F6", "56F", "C4B",
]


def legacy_hint_summary() -> dict[str, object]:
    """Return preserved legacy hints without promoting them to solve evidence."""
    return {
        "known_characters": KNOWN_CHARACTERS,
        "character_count": len(KNOWN_CHARACTERS),
        "hex_values": HEX_VALUES,
        "legacy_hypotheses": [
            "row 310 may be significant",
            "character order may contribute to a password candidate",
            "hex-grid concatenation may contribute to a password candidate",
            "character positions may contain useful ordering information",
        ],
    }


def _tokenize_p2(text: str) -> list[str]:
    tokens: list[str] = []
    for line in text.splitlines():
        line = line.split("#", 1)[0]
        tokens.extend(line.split())
    return tokens


def load_p2_pgm(path: Path) -> list[list[int]]:
    """Load an ASCII P2 PGM image using only the standard library."""
    tokens = _tokenize_p2(path.read_text(encoding="ascii"))
    if len(tokens) < 4 or tokens[0] != "P2":
        raise ValueError("PGM fixture must use ASCII P2 format")
    try:
        width = int(tokens[1])
        height = int(tokens[2])
        max_value = int(tokens[3])
        values = [int(value) for value in tokens[4:]]
    except ValueError as exc:
        raise ValueError("invalid numeric value in P2 PGM") from exc
    if width <= 0 or height <= 0:
        raise ValueError("PGM dimensions must be positive")
    if max_value <= 0 or max_value > 255:
        raise ValueError("P2 PGM max value must be between 1 and 255")
    if len(values) != width * height:
        raise ValueError(f"PGM pixel count mismatch: expected {width * height}, got {len(values)}")
    if any(value < 0 or value > max_value for value in values):
        raise ValueError("PGM pixel value outside declared range")
    if max_value != 255:
        values = [round(value * 255 / max_value) for value in values]
    return [values[row * width:(row + 1) * width] for row in range(height)]


def load_grayscale(path: Path) -> list[list[int]]:
    """Load grayscale pixels. Pillow is optional unless a non-PGM image is used."""
    if not path.is_file():
        raise FileNotFoundError(f"image not found: {path}")
    if path.suffix.lower() == ".pgm":
        return load_p2_pgm(path)
    try:
        from PIL import Image  # type: ignore
    except ImportError as exc:
        raise RuntimeError("Pillow is required for PNG/JPEG/non-PGM image input") from exc
    with Image.open(path) as image:
        gray = image.convert("L")
        width, height = gray.size
        values = list(gray.getdata())
    return [values[row * width:(row + 1) * width] for row in range(height)]


def analyze_grayscale(
    rows: list[list[int]],
    *,
    edge_threshold: int = 100,
    density_multiplier: float = 1.5,
    min_group_rows: int = 6,
) -> dict[str, object]:
    """Find consecutive rows whose horizontal edge density exceeds the baseline."""
    if not rows or not rows[0]:
        raise ValueError("image must contain at least one pixel")
    width = len(rows[0])
    if any(len(row) != width for row in rows):
        raise ValueError("image rows must have equal width")
    if edge_threshold < 0:
        raise ValueError("edge threshold must be non-negative")
    if density_multiplier <= 0:
        raise ValueError("density multiplier must be positive")
    if min_group_rows <= 0:
        raise ValueError("minimum group rows must be positive")

    edge_counts = [
        sum(1 for left, right in zip(row, row[1:]) if abs(int(right) - int(left)) > edge_threshold)
        for row in rows
    ]
    average = sum(edge_counts) / len(edge_counts)
    cutoff = average * density_multiplier
    selected = [index for index, count in enumerate(edge_counts) if count > cutoff]

    groups: list[list[int]] = []
    current: list[int] = []
    for row_index in selected:
        if not current or row_index == current[-1] + 1:
            current.append(row_index)
        else:
            if len(current) >= min_group_rows:
                groups.append(current)
            current = [row_index]
    if len(current) >= min_group_rows:
        groups.append(current)

    regions = [
        {
            "start_row": group[0],
            "end_row": group[-1],
            "row_count": len(group),
            "max_edge_count": max(edge_counts[row] for row in group),
        }
        for group in groups
    ]
    return {
        "width": width,
        "height": len(rows),
        "edge_threshold": edge_threshold,
        "density_multiplier": density_multiplier,
        "min_group_rows": min_group_rows,
        "average_edge_count": average,
        "cutoff_edge_count": cutoff,
        "selected_rows": selected,
        "regions": regions,
    }


def extract_regions(image_path: Path, regions: Iterable[dict[str, int]], output_dir: Path) -> list[str]:
    """Write region crops only when an explicit output directory is requested."""
    try:
        from PIL import Image  # type: ignore
    except ImportError as exc:
        raise RuntimeError("Pillow is required for crop extraction") from exc
    output_dir.mkdir(parents=True, exist_ok=True)
    written: list[str] = []
    with Image.open(image_path) as image:
        for index, region in enumerate(regions):
            start = int(region["start_row"])
            end = int(region["end_row"]) + 1
            crop = image.crop((0, start, image.width, end))
            destination = output_dir / f"character_region_{index:02d}_{start}-{end - 1}.png"
            crop.save(destination)
            written.append(str(destination))
    return written


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Analyze 310 challenge image rows for text-like edge density")
    parser.add_argument("image", nargs="?", help="Input image. P2 PGM works without dependencies; PNG/JPEG requires Pillow.")
    parser.add_argument("--hint-summary", action="store_true", help="Print preserved legacy character/hex hints without reading an image")
    parser.add_argument("--edge-threshold", type=int, default=100)
    parser.add_argument("--density-multiplier", type=float, default=1.5)
    parser.add_argument("--min-group-rows", type=int, default=6)
    parser.add_argument("--extract-dir", help="Optional explicit directory for PNG crops; requires Pillow")
    parser.add_argument("--output", help="Optional explicit JSON result path")
    parser.add_argument("--json", action="store_true", help="Emit compact JSON to stdout")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        if args.hint_summary:
            payload: dict[str, object] = {"mode": "legacy-hint-summary", **legacy_hint_summary()}
        else:
            if not args.image:
                parser.error("image is required unless --hint-summary is used")
            image_path = Path(args.image).expanduser().resolve()
            rows = load_grayscale(image_path)
            payload = {
                "mode": "edge-density-analysis",
                "image": str(image_path),
                **analyze_grayscale(
                    rows,
                    edge_threshold=args.edge_threshold,
                    density_multiplier=args.density_multiplier,
                    min_group_rows=args.min_group_rows,
                ),
                "legacy_hints": legacy_hint_summary(),
            }
            if args.extract_dir:
                regions = payload["regions"]
                assert isinstance(regions, list)
                payload["written_crops"] = extract_regions(
                    image_path,
                    regions,
                    Path(args.extract_dir).expanduser().resolve(),
                )
        encoded = json.dumps(payload, indent=None if args.json else 2, sort_keys=True)
        if args.output:
            output = Path(args.output).expanduser().resolve()
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(encoded + "\n", encoding="utf-8")
        print(encoded)
        return 0
    except (FileNotFoundError, RuntimeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
