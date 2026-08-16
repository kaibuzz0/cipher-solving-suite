# Reviewed Migration Plan — 310 BTC Challenge

The first generated-evidence relocation is complete. The protected primary image remains at the repository root.

## Completed relocation

| Old path | Destination | Result |
|---|---|---|
| `alpha_extract.py` | `research/active-puzzles/20260816-310-btc-challenge/tools/alpha_extract.py` | Replaced by portable CLI version; hard-coded `/root/...` input removed |
| `analyze_310.py` | `research/active-puzzles/20260816-310-btc-challenge/tools/analyze_310.py` | Relocated byte-for-byte |
| `alpha_lsb.bin` | `research/active-puzzles/20260816-310-btc-challenge/evidence/generated/alpha_lsb.bin` | Relocated byte-for-byte |
| `alpha_pattern.bin` | `research/active-puzzles/20260816-310-btc-challenge/evidence/generated/alpha_pattern.bin` | Relocated byte-for-byte |
| `alpha_2bit.bin` | `research/active-puzzles/20260816-310-btc-challenge/evidence/generated/alpha_2bit.bin` | Relocated byte-for-byte |
| `alpha_row310.bin` | `research/active-puzzles/20260816-310-btc-challenge/evidence/generated/alpha_row310.bin` | Relocated byte-for-byte |
| `bitplanes/` | `research/active-puzzles/20260816-310-btc-challenge/evidence/generated/bitplanes/` | All 24 files relocated; none deduplicated/deleted |

## Protected primary evidence

`310_challenge.png` remains at its original root path and is classified **PRIMARY EVIDENCE — DO NOT MOVE YET** until the external challenge source/provenance is verified.

## Duplicate manifest

`bitplane_duplicate_manifest.json` records all 24 bitplanes. It identifies eight exact green/blue duplicate pairs (`g_0=b_0` through `g_7=b_7`) by identical Git blob SHA and records all red bitplanes separately. Duplicate status is informational only in this pass.

## Integrity evidence

GitHub's compare view classified the four alpha binaries, all 24 bitplanes, and `analyze_310.py` as renames with **0 content changes**, because the relocation reused the exact existing Git blob objects.

CI now runs `python scripts/verify_310_migration.py`, which:

- confirms `310_challenge.png` is still present,
- confirms legacy generated paths are gone,
- confirms exactly 28 generated evidence files exist in the case,
- computes SHA-256 for the protected primary image and all relocated generated evidence,
- verifies every declared duplicate pair has matching SHA-256,
- writes `artifacts/310-migration-verification.json`.

## Remaining gates

- [x] Portable alpha extractor created.
- [x] Legacy 310 evidence linked to the structured case.
- [x] Complete bitplane duplicate manifest created.
- [x] Generated artifacts physically relocated without moving the protected original.
- [x] Git-object identity preserved for unchanged moved files.
- [ ] Latest GitHub Actions Python 3.11/3.12/3.13 matrix completes green.
- [ ] Capture the generated SHA-256 verification artifact from the green CI run.
- [ ] Verify external source/provenance for `310_challenge.png`.
- [ ] Re-run the portable extractor against the protected image and compare regenerated output SHA-256 values with the migrated legacy outputs.

## Current outcome

**Generated-evidence relocation: COMPLETE. Primary-evidence relocation: BLOCKED BY PROVENANCE, intentionally.** No duplicate files have been deleted.
