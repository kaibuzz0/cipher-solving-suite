# Reviewed Migration Plan — 310 BTC Challenge

This is the first reviewed move plan. **This document authorizes no automatic deletion and does not itself move files.** Hashes and references must be rechecked immediately before and after any later relocation commit.

## Decision table

| Current path | Classification | Proposed destination | Review decision |
|---|---|---|---|
| `310_challenge.png` | Primary evidence | remain at current path for now | **HOLD — DO NOT MOVE** until external provenance/source and all references are recorded |
| `alpha_extract.py` | Reproduction/analysis script | `research/active-puzzles/20260816-310-btc-challenge/tools/alpha_extract.py` | **READY AFTER PATH FIX**; replace hard-coded `/root/...` input with CLI argument before move |
| `analyze_310.py` | Analysis script | `research/active-puzzles/20260816-310-btc-challenge/tools/analyze_310.py` | **SAFE TO ORGANIZE** after repository references are checked |
| `alpha_lsb.bin` | Generated output | `research/active-puzzles/20260816-310-btc-challenge/evidence/generated/alpha_lsb.bin` | **SAFE AFTER HASH CAPTURE** |
| `alpha_pattern.bin` | Generated output | `research/active-puzzles/20260816-310-btc-challenge/evidence/generated/alpha_pattern.bin` | **SAFE AFTER HASH CAPTURE** |
| `alpha_2bit.bin` | Generated output | `research/active-puzzles/20260816-310-btc-challenge/evidence/generated/alpha_2bit.bin` | **SAFE AFTER HASH CAPTURE** |
| `alpha_row310.bin` | Generated output | `research/active-puzzles/20260816-310-btc-challenge/evidence/generated/alpha_row310.bin` | **SAFE AFTER HASH CAPTURE** |
| `bitplanes/` | Generated output collection with duplicate groups | `research/active-puzzles/20260816-310-btc-challenge/evidence/generated/bitplanes/` | **REVIEW DUPLICATES FIRST**; preserve all copies until canonical/reference review is complete |

## Duplicate-group review

The current Git tree proves at least the green/blue bitplanes for indices 0–7 are paired byte-identical groups: each corresponding `bitplane_g_N.png` and `bitplane_b_N.png` has the same Git blob SHA. Treat these as duplicate groups, not deletion candidates.

Canonicalization policy for a later pass:

1. Inventory SHA-256 for every bitplane.
2. Record every path in each duplicate group.
3. Search notes/scripts for path-specific references.
4. If no semantic distinction is required, retain one canonical generated file plus a manifest recording aliases/old paths.
5. Delete a duplicate only in a separate reviewed commit after the manifest and tests exist.

## Required pre-move gates

- [ ] Current inventory validates.
- [ ] Primary image SHA-256 recorded in the case evidence manifest.
- [ ] `alpha_extract.py` accepts an explicit image path instead of its legacy absolute path.
- [ ] Repository search finds and updates references to proposed moved paths.
- [ ] Duplicate manifest covers every byte-identical bitplane group.
- [ ] CI is green before the relocation commit.

## Required post-move gates

- [ ] Rebuild artifact inventory.
- [ ] Compare pre/post SHA-256 values for every moved artifact.
- [ ] Run full test matrix.
- [ ] Confirm website evidence browser resolves the case linkage.
- [ ] Append exact migration commit and any exceptions to `notes.md`.

## Current outcome

**Metadata/linkage phase: APPROVED. Physical relocation: NOT YET APPROVED.** The next implementation pass should fix the reproduction path, teach the inventory to map these legacy paths to this case, generate a duplicate manifest, and only then perform the generated-output move.
