# 310 BTC Challenge

- **Case ID:** `20260816-310-btc-challenge`
- **Type:** `crypto-puzzle`
- **Status:** `active`
- **Source:** legacy repository research
- **Owner:** unclaimed

## Evidence map

| Repository path | Role | Current decision |
|---|---|---|
| `310_challenge.png` | Primary challenge image | **PRIMARY EVIDENCE — DO NOT MOVE YET** |
| `alpha_lsb.bin` | Alpha LSB extraction | Generated output; link then organize |
| `alpha_pattern.bin` | Alpha pattern extraction | Generated output; link then organize |
| `alpha_2bit.bin` | Alpha 2-bit extraction | Generated output; link then organize |
| `alpha_row310.bin` | Row-310 alpha extraction | Generated output; link then organize |
| `bitplanes/` | RGB bitplane analysis | Generated outputs; duplicate review required |
| `alpha_extract.py` | Reproduction script | Case tool/source code |
| `analyze_310.py` | Analysis script | Case tool/source code |
| `password_candidate_solver.py` | Candidate/decryption hypothesis tool | Case-local portable replacement for the broken root `brute_force.py`; decrypt mode remains experimental |

## Known reproduction relationships

`alpha_extract.py` explicitly writes the four `alpha_*.bin` outputs. Its current `main()` contains a legacy absolute input path (`/root/310_btc_challenge/310_challenge.png`), so that path should be repaired before claiming clean reproducibility.

`analyze_310.py` performs image/color/LSB analysis and writes channel/difference outputs when its quick-analysis path is used.

The root-level `brute_force.py` is legacy/unintegrated code and must not be treated as a working command. It hard-codes `/root/310_btc_challenge/alpha_row310.bin`, mixes `Crypto` and `Cryptodome` namespaces, contains an undefined `ciphertext` reference in its PBKDF1 fallback, and writes a root-level result file. The case-local `tools/password_candidate_solver.py` preserves its hint-derived candidate hypothesis while removing those portability assumptions.

## Password-candidate workflow

Listing the deterministic candidate set requires no third-party dependency:

```bash
python research/active-puzzles/20260816-310-btc-challenge/tools/password_candidate_solver.py --list-candidates --json
```

After the row-310 payload has been regenerated and its SHA-256 compared with preserved migrated evidence, the optional decryption hypothesis can be tested with `pycryptodomex` installed:

```bash
python research/active-puzzles/20260816-310-btc-challenge/tools/password_candidate_solver.py \
  --payload research/active-puzzles/20260816-310-btc-challenge/evidence/generated/alpha_row310.bin \
  --input-encoding base64 \
  --output workspace/310-password-candidate-result.json
```

The tool only tests the legacy PBKDF2-HMAC-SHA256 / AES-256-CBC hypothesis. A plausible plaintext is a candidate result, **not** independent evidence that the puzzle is solved.

## Duplicate observation

The repository tree proves multiple `bitplanes/bitplane_g_*.png` and `bitplanes/bitplane_b_*.png` files share the same Git blob SHA for corresponding bit indices. These are byte-identical duplicate groups and must not be auto-deleted. The migration review chooses a canonical retained representation only after references are checked.

## Next action

1. Preserve and hash the primary image in place.
2. Repair/parameterize the legacy absolute path in `alpha_extract.py` before relying on reproduction.
3. Regenerate `alpha_row310.bin` and compare its SHA-256 with preserved migrated output.
4. Run the deterministic password-candidate solver only after that evidence match.
5. Treat any plausible decrypt as a hypothesis requiring independent verification, not a solve claim.
6. Continue artifact/duplicate migration only with provenance and reference preservation.
