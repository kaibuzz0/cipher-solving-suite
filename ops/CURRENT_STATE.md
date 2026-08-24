# Current Repository State

Last reconciled: 2026-08-24 19:21 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `73fa9fa5314d476829c8b3bdbc0915203ba6df2e`, the merge of PR #53 (`Build: reconcile portable 310 image analyzer onto current main`).
- PR #53 final head `3f8ac5466a25506e40bcd736baf9789355257525` was mergeable, had no unresolved review threads, and passed Core validation `32663349865` on Python 3.11/3.12/3.13 plus Daily Repository Maintenance `32663349853`.
- All three Core matrix jobs passed the test suite, compilation, source-registry/history/report validation, intelligence-feed validation, artifact inventory, 310 migration verification, 310 alpha reproduction, dashboard-data generation, maintenance, and the final failure gate.
- Public GitHub Pages is reachable and exposes the canonical workspace surfaces including Opportunities, News / Intel, Cases, Tools, Evidence, Collection Health, source registry, prompts/workflow, and Agent Operations.
- No open repository issues were found in the latest integrity pass.
- `toolsets/catalog.json` still contains only `repo-factory` at `experimental`; PR #53 did not alter reusable toolset state.

## Build / integration state

- `btc310-image-analyzer` is now canonical on `main` at `experimental` maturity and linked to case `20260816-310-btc-challenge`.
- The analyzer runs directly as `python research/active-puzzles/20260816-310-btc-challenge/tools/analyze_310.py 310_challenge.png --json`, emits deterministic RGB/text/LSB/legacy-hint analysis, is read-only by default, and writes derived `channel_*.png` / `difference.png` only when `--output-dir` is explicitly supplied.
- `tests/test_310_image_analyzer.py` fingerprints any pre-existing root channel/difference artifacts before and after default direct-script execution and requires exact non-mutation; it also covers explicit managed output, a tiny/flat image, missing-input fail-closed behavior, and claim-boundary text.
- Integration queue item `20260824-pr48-310-image-analyzer-integration` records the PR #48 contribution origin, PR #53 reconciliation, final validation, merge commit, risks, and exact independent-verification next action.
- The shared work queue treats the analyzer reconciliation as completed and redirects further 310 work toward external provenance or another hash-preserving legacy/root-artifact item rather than duplicate analyzer work.

## Source-history / research coordination

- PR #44 observations at `2026-08-22T07:42:16Z` are canonical through PR #50 and integration item `20260822-pr44-source-health-replay` remains `integrated`.
- Open research PR #47 preserves the next raw snapshot at `2026-08-22T19:42:58Z`, including the NASA Gateways candidate; PR #49 preserves the following `2026-08-23T07:42:04Z` snapshot; PR #52 preserves the newer NASA Orbital Clarity lead.
- The machine-readable integration queue now explicitly records PR #47 as `needs-integration`, PR #49 as blocked on #47, and PR #52 as blocked pending earlier replay plus complete official-rules verification.
- Required canonical replay order remains PR #47, then PR #49. PR #52 must not be used to manufacture earlier registry freshness.
- The analyzer merge did not modify source history, registry timestamps, research raw snapshots, opportunities, or bounty authorization state.
- Public bounty/program listings remain discovery evidence only and are not authorization to test a target.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` are canonically registered at `experimental` and linked to case `20260816-310-btc-challenge`.
- PR #45 established repository-internal alpha extraction reproducibility from protected `310_challenge.png`; this does not establish external provenance/authenticity or a puzzle solve.
- The image analyzer's statistics, printable-byte runs, LSB summaries, and legacy-hint checks remain exploratory. No hidden-data, private-key, or solve claim is made.
- External provenance/authenticity for `310_challenge.png` remains the primary semantic evidence gate before interpreting solver/decryption output as source-authentic.
- Root `brute_force.py`, `char_locator.py`, and preserved generated images remain legacy/provenance debt and must not be deleted or relocated without hash/reference reconciliation.

## Coordination / governance state

- `AGENTS.md`, `docs/AI_AGENT_INTEGRATION.md`, and `docs/AUTOMATED_AGENT_OPERATIONS.md` remain aligned on current-main authority, evidence preservation, canonical registration, bounded PR work, dynamic website discovery, collision avoidance, and independent verification.
- PR #53 was rebuilt from the then-current main instead of accepting PR #48's stale shared-state snapshot wholesale; this preserved PR #50/#51 source-history and coordination state.
- PRs #54 and #55 independently opened on the same post-PR53 coordination objective. Their compatible work was reconciled onto PR #55: #54's machine-readable PR #47/#49/#52 queue records were preserved, while #55 retains the safe append-only handoff, work-queue update, analyzer integration record, and current-state sync. PR #54 was closed as superseded rather than allowing duplicate shared-file coordination branches to continue.
- PR #55 reconciled head `bcf32b0dc1bf9a4106dbab29b8133a8b0f8979d5` has green Daily Repository Maintenance run `32767764522`; fresh Core validation run `32767764644` is still in progress and must pass before merge/readiness.
- Open research PRs #47, #49, and #52 remain separate research lanes. No analyzer integration path overlaps their raw snapshot files.
- Normal user-facing discovery continues through canonical `data/tools.json` and generated site-data / Command Site paths; no bespoke `site/index.html` edit was needed for `btc310-image-analyzer`.
- `docs/AGENT_HANDOFF.md` is append-only. PR #55 preserves the post-PR53 handoff as additions only; this pass did not rewrite historical journal content.

## Known debt

- Merge PR #55 only if its reconciled head completes fresh Core validation successfully; do not bypass the draft/review gate while CI is running.
- Reconcile/replay PR #47 then PR #49 chronologically through canonical source history/registry validation; preserve the NASA Gateways candidate.
- Evaluate PR #52 only after earlier source state is canonical and preserve exact eligibility/prize/submission evidence before promotion.
- Independently confirm merged-main generated discovery for `btc310-image-analyzer` and keep its `experimental` boundary unless stronger evidence exists.
- Verify external provenance for `310_challenge.png` before escalating 310 semantic/decryption hypotheses.
- Continue hash/provenance-preserving root artifact migration and remaining legacy solver inventory.
- Add further provenance-preserving official-source adapters where current sources support exact evidence.

## Current operating priorities

1. Repo Integrity: wait for PR #55 reconciled-head Core validation; if green, mark it ready/review and merge the single surviving coordination PR rather than reviving #54.
2. Research/integration: preserve chronological source replay by reconciling PR #47 first, then PR #49; only then evaluate the later PR #52 lead for canonical promotion.
3. 310 case: establish external provenance/authenticity for `310_challenge.png` before interpreting password/decryption or hidden-data hypotheses as source-authentic.
4. Continue legacy solver/root-artifact inventory without deleting or moving primary evidence before hashes/references are reconciled.

## Next handoff

Repo Integrity re-read current repository governance and live state, detected duplicate overlapping post-PR53 coordination PRs #54/#55, and reconciled their compatible contributions onto PR #55 rather than choosing one side wholesale. PR #54's missing machine-readable PR #47/#49/#52 integration records were copied into PR #55; PR #55's safe append-only handoff, work-queue update, analyzer integration record, and post-merge current-state synchronization were preserved. PR #54 was then closed as superseded. Public Pages remains reachable, there are no open issues, Daily Maintenance is green on reconciled PR #55 head `bcf32b0d...`, and Core run `32767764644` is still in progress. Exact next action: merge PR #55 only after that fresh Core run is green, then continue research replay PR #47 -> PR #49 and evaluate PR #52 afterward.
