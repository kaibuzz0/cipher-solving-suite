# Current Repository State

Last reconciled: 2026-08-23 20:00 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `ceb2a99876227ac827f821b5df386e080c65ed73`, the merge of documentation-only integrity reconciliation PR #51 after PR #50.
- PR #51 head `038ec53a82f36e137a236caaa95000594fc2c487` passed Core validation `32660869978` before merge.
- PR #50 is canonical; its final head `a9693c067b40fee35779e9b2e2c6a860104c0528` passed Core `32627332013` on Python 3.11/3.12/3.13, Daily Repository Maintenance `32627332057`, and Intelligence Source Report `32627332041`.
- There are no known open repository issues from the latest integrity pass.
- `toolsets/catalog.json` still contains only `repo-factory` at `experimental`; this build pass does not alter toolset state.

## Active build reconciliation

- Build Integration is reconciling the previously green PR #48 `btc310-image-analyzer` contribution onto current `main` in branch `agent/reconcile-310-analyzer-20260823` rather than merging its stale shared-state snapshot wholesale.
- The reconciled branch preserves the portable/non-destructive analyzer, deterministic direct-script tests, `experimental` tool registration, active-case linkage, and safe explicit-output workflow while retaining all newer PR #50/#51 source-history and coordination state.
- `analyze_310.py` is read-only by default; derived `channel_*.png` and `difference.png` files are written only when `--output-dir` is explicitly supplied. Existing root artifacts are fingerprinted before/after default direct-script tests and must remain unchanged.
- Final-head Core/Daily/visibility validation is still required before this reconciled contribution is ready to merge. Until then `btc310-image-analyzer` is branch-only, not canonical on `main`.

## Source-history / research coordination

- PR #44 observations at `2026-08-22T07:42:16Z` are canonical through PR #50 and integration item `20260822-pr44-source-health-replay` is `integrated`.
- Open research PR #47 preserves the next raw snapshot at `2026-08-22T19:42:58Z`, including the NASA Gateways candidate; PR #49 preserves the following `2026-08-23T07:42:04Z` snapshot; PR #52 preserves a newer NASA Orbital Clarity lead. These raw research lanes are not modified by the analyzer reconciliation.
- Canonical source replay must remain chronological: PR #47, then PR #49; later research must not manufacture earlier registry freshness.
- Public bounty/program listings remain discovery evidence only and are not testing authorization.

## 310 case / tool state

- Canonical `main` currently registers `btc310-password-candidates`, `btc310-character-locator`, and `btc310-reproduction-verifier` at `experimental` for case `20260816-310-btc-challenge`.
- PR #45 established repository-internal alpha extraction reproducibility from protected `310_challenge.png`; external source/provenance for that image remains unresolved and reproducibility is not a puzzle solve.
- The reconciled analyzer contribution keeps RGB statistics, printable-byte runs, LSB summaries, and legacy hint checks explicitly exploratory. No hidden-data, private-key, or solve claim is made.
- Root `brute_force.py`, `char_locator.py`, and preserved generated images remain legacy/provenance debt and must not be deleted or relocated without hash/reference reconciliation.

## Coordination / governance state

- `AGENTS.md`, `docs/AI_AGENT_INTEGRATION.md`, and `docs/AUTOMATED_AGENT_OPERATIONS.md` remain the controlling integration contract.
- The analyzer branch intentionally avoids `data/source_check_history.json`, `data/intelligence_sources.json`, raw research snapshots, toolset manifests/catalog, and website HTML.
- User-visible discovery is expected to flow through canonical `data/tools.json` plus the existing generated site-data / Command Site contract; no bespoke `site/index.html` edit is part of this work.
- `docs/AGENT_HANDOFF.md` is append-only and too large to safely reconstruct from the connected truncated read. The exact build handoff must be preserved in the PR description unless an append-capable integrity pass can update the journal without truncating history.

## Known debt

- Replay PR #47 then PR #49 chronologically through canonical source history/registry validation.
- Independently verify and merge the current-main analyzer reconciliation only if final Core/Daily/site visibility checks remain green.
- Verify external provenance for `310_challenge.png` before interpreting any solver/decryption result as source-authentic.
- Continue hash/provenance-preserving root artifact migration and remaining legacy solver inventory.
- Add further provenance-preserving official-source adapters where current sources support exact evidence.

## Current operating priorities

1. Finish CI and independent integrity review for the current-main `btc310-image-analyzer` reconciliation.
2. Preserve chronological source replay: PR #47, then PR #49; evaluate PR #52 only after earlier source state is canonical.
3. Verify external provenance for `310_challenge.png` before escalating 310 semantic/decryption hypotheses.
4. Continue legacy solver/root-artifact inventory without deleting primary evidence.

## Next handoff

Build Integration merged green documentation-only PR #51, then rebuilt PR #48's tested analyzer contribution on top of that newer `main` instead of accepting stale shared state. The branch preserves deterministic direct-script behavior, explicit-only derived outputs, canonical tool registration, case documentation, and newer source-history coordination. Final-head GitHub Actions validation remains the gate before the reconciled analyzer can be considered ready for independent integrity merge.
