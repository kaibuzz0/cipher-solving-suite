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
| `alpha_extract.py` | Reproduction script | Portable case tool; takes the image path and writes under case evidence by default |
| `analyze_310.py` | Analysis script | Portable deterministic RGB/LSB/text/hint analyzer; writes derived images only to an explicit output directory |
| `password_candidate_solver.py` | Candidate/decryption hypothesis tool | Case-local portable replacement for the broken root `brute_force.py`; decrypt mode remains experimental |
| `scripts/verify_310_reproduction.py` | Reproduction verifier | Regenerates alpha outputs in a temporary directory, compares hashes/bytes with migrated evidence, and never overwrites canonical evidence |

## Known reproduction relationships

`alpha_extract.py` explicitly writes the four `alpha_*.bin` outputs. It is already parameterized: the input image is a required command-line path and generated outputs default to this case's `evidence/generated/` directory.

`verify_310_reproduction.py` is the safe default for proving that relationship. It runs the extractor against the protected root image in a temporary directory, computes SHA-256 for the primary image and every regenerated alpha output, compares the regenerated files with the migrated evidence, and writes only `artifacts/310-reproduction-verification.json`. A passing report validates reproducibility of the extraction relationship; it is not evidence that any hidden-data or password hypothesis is correct.

`analyze_310.py` performs deterministic image/color, printable-byte, RGB-LSB, and legacy-hint analysis. By default it is read-only and emits no derived images. Derived channel/difference images are created only when an explicit `--output-dir` is supplied, so generated outputs can stay under `workspace/` or another managed artifact lane instead of reappearing in the repository root.

The root-level `brute_force.py` is legacy/unintegrated code and must not be treated as a working command. It hard-codes `/root/310_btc_challenge/alpha_row310.bin`, mixes `Crypto` and `Cryptodome` namespaces, contains an undefined `ciphertext` reference in its PBKDF1 fallback, and writes a root-level result file. The case-local `tools/password_candidate_solver.py` preserves its hint-derived candidate hypothesis while removing those portability assumptions.

## Reproduction and analysis workflow

Verify migrated evidence and reproduce the alpha outputs without moving or overwriting the primary evidence:

```bash
python scripts/verify_310_migration.py
python scripts/verify_310_reproduction.py
```

The reproduction verifier requires the same image dependencies as `alpha_extract.py`: NumPy and Pillow. Core CI installs bounded versions and runs this command on Python 3.11, 3.12, and 3.13.

Run the deterministic read-only image analyzer:

```bash
python research/active-puzzles/20260816-310-btc-challenge/tools/analyze_310.py 310_challenge.png --json
```

To intentionally write derived channel/difference images, choose a managed output directory explicitly:

```bash
python research/active-puzzles/20260816-310-btc-challenge/tools/analyze_310.py \
  310_challenge.png \
  --json \
  --output-dir workspace/310-image-analysis
```

The analyzer preserves the legacy character/hex hints only as hypotheses. RGB sample matches, text-like byte runs, LSB ratios, or derived images are exploratory evidence and are not proof of a hidden key or puzzle solve.

Listing the deterministic password-candidate set requires no third-party dependency:

```bash
python research/active-puzzles/20260816-310-btc-challenge/tools/password_candidate_solver.py --list-candidates --json
```

Only after reproduction is independently confirmed should the optional decryption hypothesis be interpreted. With `pycryptodomex` installed:

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

1. Independently verify the registered `btc310-image-analyzer` direct-script behavior, deterministic JSON, and explicit-output boundary.
2. Verify external source/provenance for `310_challenge.png`; reproducibility does not establish provenance.
3. Only after those evidence gates are understood should the password/decryption hypothesis be interpreted.
4. Treat any plausible decrypt, text pattern, LSB anomaly, or character region as a hypothesis requiring independent verification, not a solve claim.
5. Continue artifact/duplicate migration only with provenance and reference preservation.
