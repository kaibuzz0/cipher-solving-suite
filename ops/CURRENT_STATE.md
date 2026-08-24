# Current Repository State

Last reconciled: 2026-08-23 20:08 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `ceb2a99876227ac827f821b5df386e080c65ed73`, the merge of documentation-only integrity reconciliation PR #51 after PR #50.
- PR #51 head `038ec53a82f36e137a236caaa95000594fc2c487` passed Core validation `32660869978` before merge.
- PR #50 is canonical; its final head `a9693c067b40fee35779e9b2e2c6a860104c0528` passed Core `32627332013` on Python 3.11/3.12/3.13, Daily Repository Maintenance `32627332057`, and Intelligence Source Report `32627332041`.
- There are no known open repository issues from the latest integrity pass.
- `toolsets/catalog.json` still contains only `repo-factory` at `experimental`; this build pass does not alter toolset state.

## Active build reconciliation

- Draft PR #53 (`Build: reconcile portable 310 image analyzer onto current main`) rebuilds the previously green PR #48 `btc310-image-analyzer` contribution from current `main` instead of merging its stale shared-state snapshot wholesale.
- PR #53 implementation head `7a3279c7bd40ddafd93605a0d113a6172ab132b8` passed Core validation `32663290339` across Python 3.11/3.12/3.13 and Daily Repository Maintenance `32663290409`.
- All three Core matrix jobs passed the test suite, compilation, source registry/history/report validation, intelligence validation, artifact inventory, 310 migration verification, 310 alpha reproduction, dashboard-data generation, maintenance, and final failure gate. This includes the analyzer direct-script regression tests and the canonical user-visible tool-discovery contract.
- The reconciled branch preserves the portable/non-destructive analyzer, deterministic direct-script tests, `experimental` tool registration, active-case linkage, and safe explicit-output workflow while retaining all newer PR #50/#51 source-history and coordination state.
- `analyze_310.py` is read-only by default; derived `channel_*.png` and `difference.png` files are written only when `--output-dir` is explicitly supplied. Existing root artifacts are fingerprinted before/after default direct-script tests and must remain unchanged.
- A final state-only reconciliation commit follows the successful implementation validation; the final PR head must also remain green before draft status is removed.

## Source-history / research coordination

- PR #44 observations at `2026-08-22T07:42:16Z` are canonical through PR #50 and integration item `20260822-pr44-source-health-replay` is `integrated`.
- Open research PR #47 preserves the next raw snapshot at `2026-08-22T19:42:58Z`, including the NASA Gateways candidate; PR #49 preserves the following `2026-08-23T07:42:04Z` snapshot; PR #52 preserves a newer NASA Orbital Clarity lead. These raw research lanes are not modified by the analyzer reconciliation.
- Canonical source replay must remain chronological: PR #47, then PR #49; later research must not manufacture earlier registry freshness.
- Public bounty/program listings remain discovery evidence only and are not testing authorization.

## 310 case / tool state

- Canonical `main` currently registers `btc310-password-candidates`, `btc310-character-locator`, and `btc310-reproduction-verifier` at `experimental` for case `20260816-310-btc-challenge`.
- PR #45 established repository-internal alpha extraction reproducibility from protected `310_challenge.png`; external source/provenance for that image remains unresolved and reproducibility is not a puzzle solve.
- PR #53 contributes `btc310-image-analyzer` at `experimental`; until merge it is branch-only, not canonical on `main`.
- The analyzer keeps RGB statistics, printable-byte runs, LSB summaries, and legacy hint checks explicitly exploratory. No hidden-data, private-key, or solve claim is made.
- Root `brute_force.py`, `char_locator.py`, and preserved generated images remain legacy/provenance debt and must not be deleted or relocated without hash/reference reconciliation.

## Coordination / governance state

- `AGENTS.md`, `docs/AI_AGENT_INTEGRATION.md`, and `docs/AUTOMATED_AGENT_OPERATIONS.md` remain the controlling integration contract.
- The analyzer branch intentionally avoids `data/source_check_history.json`, `data/intelligence_sources.json`, raw research snapshots, toolset manifests/catalog, and website HTML.
- User-visible discovery flows through canonical `data/tools.json` plus the existing generated site-data / Command Site contract; no bespoke `site/index.html` edit is part of this work.
- `docs/AGENT_HANDOFF.md` is append-only and too large to safely reconstruct from the connected truncated read. The exact build handoff is preserved in PR #53 for a safe append-capable integrity pass rather than risking journal truncation.

## Known debt

- Replay PR #47 then PR #49 chronologically through canonical source history/registry validation.
- Independently verify and merge PR #53 only if its final state-reconciled head remains green and the `experimental` boundary is appropriate.
- Verify external provenance for `310_challenge.png` before interpreting any solver/decryption result as source-authentic.
- Continue hash/provenance-preserving root artifact migration and remaining legacy solver inventory.
- Add further provenance-preserving official-source adapters where current sources support exact evidence.

## Current operating priorities

1. Confirm final-head CI for PR #53, then hand it to Repo Integrity for independent direct-script/site-discovery review.
2. Preserve chronological source replay: PR #47, then PR #49; evaluate PR #52 only after earlier source state is canonical.
3. Verify external provenance for `310_challenge.png` before escalating 310 semantic/decryption hypotheses.
4. Continue legacy solver/root-artifact inventory without deleting primary evidence.

## Next handoff

Build Integration merged green documentation-only PR #51, then rebuilt PR #48's tested analyzer contribution on top of that newer `main` instead of accepting stale shared state. PR #53 implementation head `7a3279c7...` passed Core `32663290339` on Python 3.11/3.12/3.13 and Daily Maintenance `32663290409`, including direct-script analyzer tests, 310 evidence checks, dashboard generation and tool visibility. This state-only reconciliation records those exact results; final-head CI remains the last builder gate before independent integrity review.
