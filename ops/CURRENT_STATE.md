# Current Repository State

Last reconciled: 2026-08-21 20:12 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `16d62558ba7f6fae0516ab95e798b060a65e166b`, the merge of research PR #41 (`Research: refresh source health and publish Structured Totient lead`). PR #41 final head `517d8da77ebb3a7bbdfdf3af6fb921a2460881fb` passed Core validation run `32520391919` and Intelligence Source Report run `32520391918` before merge.
- PR #39 is merged as `762cf7f0fd73a49a28407c98ea74111b36ddf3c9` after independent integrity verification. `btc310-password-candidates` remains `experimental`; no puzzle solve is claimed.
- Public GitHub Pages remains reachable at `https://kaibuzz0.github.io/cipher-solving-suite/` with Opportunities, News / Intel, Cases, Tools, Evidence, Collection Health, source registry and Agent Operations surfaces.
- `data/integration_queue.json` remains empty and no open repository issues were found at the start of this build pass.
- Stale coordination PR #40 was closed without merge after PR #41 advanced `main`. Its intended PR #39 integrity handoff remains preserved in the PR body and must be appended safely to the append-only journal together with PR #41's preserved research handoff.

## Build / integration state

- Active bounded build PR: #42 on `agent/310-character-locator-20260821`.
- Root `char_locator.py` is legacy/unregistered 310-specific code. It hard-codes `/root/310_btc_challenge/310_challenge.png`, imports Pillow and NumPy at module load, writes `character_region_*.png` into the repository root, and mixes hints with analysis output.
- PR #42 adds `research/active-puzzles/20260816-310-btc-challenge/tools/character_locator.py` as a portable replacement while deliberately preserving the root legacy file for provenance/reference review.
- The replacement preserves the legacy known-character/hex hypothesis as explicitly labeled hypotheses, performs deterministic horizontal edge-density analysis, supports dependency-free ASCII P2 PGM fixtures, lazy-loads Pillow for PNG/JPEG input and crop extraction, and writes JSON/crops only when an explicit output path/directory is supplied.
- `tests/test_310_character_locator.py` exercises deterministic direct-script hint output, end-to-end P2 fixture analysis, missing-image fail-closed behavior, required-input handling and explicit-only output writing without requiring Pillow in CI.
- `btc310-character-locator` is registered in `data/tools.json` at `experimental` maturity with case linkage and its optional Pillow dependency documented. The active 310 case lists the new analysis script. Normal website discovery remains through the canonical tool registry/site-data contract; no bespoke `site/index.html` edit is required.
- `docs/WORK_QUEUE.md` advances the P2 legacy-solver inventory while retaining the root utility until provenance/reference review is complete.
- PR #42 implementation head `e9e39cf190a3d12f48536e67172374738faa028d` passed Daily Repository Maintenance run `32521975949`. Core validation run `32521976081` passed its test suite, compile, source registry/history/feed validation, source report, artifact inventory, 310 migration verification, dashboard-data generation and maintenance stages on Python 3.11, 3.12 and 3.13; all three matrix jobs completed successfully. This coordination update requires a fresh final-head CI check before the PR is marked ready.

## Current research / case state

- The only structured active puzzle remains `research/active-puzzles/20260816-310-btc-challenge`.
- The primary 310 case gate is unchanged: verify original challenge provenance, regenerate row-310 evidence with the portable alpha extractor, compare SHA-256 against preserved migrated output, and only then interpret password-candidate decrypt attempts.
- The character-position hypothesis is now testable through a portable bounded analyzer, but detected edge regions are analysis candidates only and are not solve evidence.
- PR #41 refreshed CTFtime/arXiv/Sherlock/ETHGlobal/federal challenge source state and published arXiv:2608.19191, *The Structured Totient Preimage Problem: Reconstruction, Collisions, and Cryptographic Implications*, at medium confidence. Its ancillary scripts remain an evaluation lead, not imported tooling.
- NCI ODS remains an evidence-enrichment candidate. Cap, Aave V4, Midas and Puffer remain discovery/watch leads only; no security target testing started.
- `RsaCtfTool/RsaCtfTool` remains an evaluation lead pending overlap, dependency, license, maintenance-cost and deterministic-fixture review.

## Known state / debt

- `btc310-password-candidates` and `btc310-character-locator` are `experimental`; tests can verify deterministic behavior without establishing the underlying puzzle hypotheses as correct.
- Root `brute_force.py` and `char_locator.py` remain preserved legacy code pending reference/provenance review and eventual hash-preserving migration decision.
- Generated root artifacts still require hash/provenance-preserving relocation. Primary 310 evidence remains protected in place.
- Source freshness debt remains separate from this solver pass.
- Action-runtime deprecation warnings remain bounded maintenance debt.
- `docs/AGENT_HANDOFF.md` still lacks the preserved PR #39 integrity and PR #41 research entries because the available connected file-write primitive replaces the full append-only file rather than appending atomically. PR #42 preserves both exact entries plus this build handoff in its body for a safe append-capable pass.

## Current operating priorities

1. Re-check PR #42 final-head Core validation and Daily Repository Maintenance after this coordination commit; mark ready only if green and mergeable.
2. Repo Integrity should independently verify the P2 fixture result, fail-closed behavior, lazy dependency boundary, `experimental` maturity and website discovery before integrating the locator.
3. For the 310 case, regenerate `alpha_row310.bin`, compare SHA-256 against preserved migrated evidence, and only then test candidate decrypt output.
4. Evaluate the Structured Totient ancillary scripts for deterministic-fixture value and overlap before importing external code.
5. Continue legacy solver/root-artifact inventory without deleting or moving evidence until references and hashes are reconciled.

## Next handoff

The build pass started from current `main` after PR #41, closed stale coordination PR #40 without merging its obsolete state snapshot, and preserved both PR #40 and PR #41 handoff text for safe append in PR #42. The current branch integrates a portable 310 character-region analyzer through the case, tool registry and work queue without deleting legacy code or hardcoding website HTML. Implementation-head CI is green across all supported Python versions and Daily Maintenance; final-head CI after this state update remains the last build-side readiness gate. No solve, private-key generation, security target testing or destructive evidence migration should be inferred from this work.
