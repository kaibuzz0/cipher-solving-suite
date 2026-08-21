#!/usr/bin/env python3
"""Portable candidate generator/tester for the 310 BTC challenge.

This replaces the assumptions in the legacy root-level ``brute_force.py`` with a
case-local command that has deterministic candidate ordering, repository-relative
inputs, explicit OpenSSL payload validation, and an optional crypto dependency.

Listing/validation modes use only the Python standard library. Decryption mode
requires ``pycryptodomex`` (``Cryptodome`` import namespace).
"""

from __future__ import annotations

import argparse
import base64
import json
import string
import sys
from pathlib import Path
from typing import Iterable

VISIBLE_CHARS = "L3CEO275KOD899D4FA1F64"
HEX_WORDS = (
    "511", "B20", "332", "328", "410", "530",
    "22B", "0FE", "52E", "D0F", "7A1", "65B",
    "52C", "7E7", "511", "2F6", "56F", "C4B",
)
COMMON_CANDIDATES = (
    "pip", "Pip", "PIP",
    "bitcoin", "Bitcoin", "BITCOIN",
    "310", "310btc", "310BTC",
    "challenge", "Challenge",
    "theseedisplanted",
    "L3CEO275KOD899D4FA1F64",
    "L3CEO275KOD899D4FA1F64310",
)


def _dedupe(items: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            ordered.append(item)
    return ordered


def generate_candidates() -> list[str]:
    """Return the legacy hint-derived candidate set in deterministic order."""
    hex_concat = "".join(HEX_WORDS)
    items: list[str] = [
        VISIBLE_CHARS,
        VISIBLE_CHARS.lower(),
        VISIBLE_CHARS.upper(),
        hex_concat,
        hex_concat.lower(),
        VISIBLE_CHARS + hex_concat,
        hex_concat + VISIBLE_CHARS,
    ]
    for separator in ("", "_", "-", " "):
        items.append(separator.join(HEX_WORDS))
    items.extend(COMMON_CANDIDATES)
    return _dedupe(items)


def load_openssl_payload(path: Path, encoding: str) -> bytes:
    raw = path.read_bytes()
    if encoding == "base64":
        try:
            compact = b"".join(raw.split())
            raw = base64.b64decode(compact, validate=True)
        except Exception as exc:  # binascii.Error is intentionally normalized.
            raise ValueError(f"invalid base64 payload: {exc}") from exc
    if not raw.startswith(b"Salted__"):
        raise ValueError("payload is not OpenSSL Salted__ format")
    if len(raw) <= 16 or (len(raw) - 16) % 16 != 0:
        raise ValueError("OpenSSL payload ciphertext is not a non-empty AES block sequence")
    return raw


def _unpad_pkcs7(data: bytes) -> bytes | None:
    if not data:
        return None
    padding = data[-1]
    if padding < 1 or padding > 16 or data[-padding:] != bytes([padding]) * padding:
        return None
    return data[:-padding]


def _plausible_plaintext(data: bytes) -> str | None:
    unpadded = _unpad_pkcs7(data)
    if unpadded is None:
        return None
    try:
        text = unpadded.decode("utf-8")
    except UnicodeDecodeError:
        return None
    if not text:
        return None
    printable = sum(ch in string.printable for ch in text) / len(text)
    if printable < 0.95:
        return None
    lowered = text.lower()
    if "private" in lowered or "key" in lowered:
        return text
    # Legacy Bitcoin WIF prefixes. This is only a plausibility filter, not proof.
    if text[0] in {"5", "K", "L"}:
        return text
    return text if printable == 1.0 else None


def try_candidates(payload: bytes, candidates: list[str], iterations: int) -> tuple[str, str] | None:
    """Test candidates with the legacy PBKDF2-HMAC-SHA256/AES-256-CBC hypothesis."""
    try:
        from Cryptodome.Cipher import AES
        from Cryptodome.Hash import SHA256
        from Cryptodome.Protocol.KDF import PBKDF2
    except ImportError as exc:
        raise RuntimeError(
            "decryption mode requires pycryptodomex (pip install pycryptodomex)"
        ) from exc

    salt = payload[8:16]
    ciphertext = payload[16:]
    for password in candidates:
        key_iv = PBKDF2(
            password.encode("utf-8"),
            salt,
            dkLen=48,
            count=iterations,
            hmac_hash_module=SHA256,
        )
        key, iv = key_iv[:32], key_iv[32:48]
        plaintext = _plausible_plaintext(AES.new(key, AES.MODE_CBC, iv).decrypt(ciphertext))
        if plaintext is not None:
            return password, plaintext
    return None


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list-candidates", action="store_true", help="print deterministic hint-derived candidates")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    parser.add_argument("--limit", type=int, default=None, help="limit candidates tested/listed")
    parser.add_argument("--payload", type=Path, help="path to the migrated alpha_row310 payload")
    parser.add_argument("--input-encoding", choices=("base64", "raw"), default="base64")
    parser.add_argument("--iterations", type=int, default=10000, help="PBKDF2 iteration hypothesis")
    parser.add_argument("--output", type=Path, help="write a successful result as JSON")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    candidates = generate_candidates()
    if args.limit is not None:
        if args.limit < 0:
            print("error: --limit must be >= 0", file=sys.stderr)
            return 2
        candidates = candidates[: args.limit]

    if args.list_candidates:
        if args.json:
            print(json.dumps({"count": len(candidates), "candidates": candidates}, indent=2))
        else:
            for candidate in candidates:
                print(candidate)
        return 0

    if args.payload is None:
        print("error: --payload is required unless --list-candidates is used", file=sys.stderr)
        return 2
    if args.iterations <= 0:
        print("error: --iterations must be > 0", file=sys.stderr)
        return 2

    try:
        payload = load_openssl_payload(args.payload, args.input_encoding)
        result = try_candidates(payload, candidates, args.iterations)
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if result is None:
        print(f"No plausible plaintext found across {len(candidates)} candidates.")
        return 1

    password, plaintext = result
    record = {
        "status": "candidate-match",
        "password": password,
        "plaintext": plaintext,
        "iterations": args.iterations,
        "note": "Plausible decryption is not independent proof of a puzzle solve.",
    }
    rendered = json.dumps(record, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
