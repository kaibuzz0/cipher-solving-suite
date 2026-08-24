# Current Repository State

Last reconciled: 2026-08-24 08:18 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `73fa9fa5314d476829c8b3bdbc0915203ba6df2e`, the merge of PR #53 (`Build: reconcile portable 310 image analyzer onto current main`).
- PR #53 final head `3f8ac5466a25506e40bcd736baf9789355257525` was mergeable, had no unresolved review threads, and passed Core validation `32663349865` on Python 3.11/3.12/3.13 plus Daily Repository Maintenance `32663349853`.
- All three Core matrix jobs passed the test suite, compilation, source-registry/history/report validation, intelligence-feed validation, artifact inventory, 310 migration verification, 310 alpha reproduction, dashboard-data generation, maintenance, and the final failure gate.
- Post-merge workflow/Pages execution for merge commit `73fa9fa...` was not independently observed in this run. The repository remains Pages-configured, and PR #53's final-head Core run successfully generated the dashboard/site data and passed the canonical tool-visibility contract.
- No open repository issues were found in the latest reconciled state.
- `toolsets/catalog.json` still contains only `repo-factory` at `experimental`; PR #53 did not alter reusable toolset state.

## Build / integration state

- `btc310-image-analyzer` is now canonical on `main` at `experimental` maturity and linked to case `20260816-310-btc-challenge`.
- The analyzer runs directly as `python research/active-puzzles/20260816-310-btc-challenge/tools/analyze_310.py 310_challenge.png --json`, emits deterministic RGB/text/LSB/legacy-hint analysis, is read-only by default, and writes derived `channel_*.png` / `difference.png` only when `--output-dir` is explicitly supplied.
- `tests/test_310_image_analyzer.py` fingerprints any pre-existing root channel/difference artifacts before and after default direct-script execution and requires exact non-mutation; it also covers explicit managed output, a tiny/flat image, missing-input fail-closed behavior, and claim-boundary text.
- Integration queue item `20260824-pr48-310-image-analyzer-integration` records the PR #48 contribution origin, PR #53 reconciliation, final validation, merge commit, risks, and exact independent-verification next action.
- The shared work queue now treats the analyzer reconciliation as completed and redirects further 310 work toward external provenance or another hash-preserving legacy/root-artifact item rather than duplicate analyzer work.

## Source-history / research coordination

- PR #44 observations at `2026-08-22T07:42:16Z` are canonical through PR #50 and integration item `20260822-pr44-source-health-replay` remains `integrated`.
- Open research PR #47 preserves the next raw snapshot at `2026-08-22T19:42:58Z`, including the NASA Gateways candidate; PR #49 preserves the following `2026-08-23T07:42:04Z` snapshot; PR #52 preserves the newer NASA Orbital Clarity lead.
- Required canonical replay order remains PR #47, then PR #49. PR #52 must not be used to manufacture earlier registry freshness.
- The analyzer merge did not modify source history, registry timestamps, research raw snapshots, opportunities, or bounty authorization state.
- Public bounty/program listings remain discovery evidence only and are not authorization to test a target.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` are now canonically registered at `experimental` and linked to case `20260816-310-btc-challenge`.
- PR #45 established repository-internal alpha extraction reproducibility from protected `310_challenge.png`; this does not establish external provenance/authenticity or a puzzle solve.
- The image analyzer's statistics, printable-byte runs, LSB summaries, and legacy-hint checks remain exploratory. No hidden-data, private-key, or solve claim is made.
- External provenance/authenticity for `310_challenge.png` remains the primary semantic evidence gate before interpreting solver/decryption output as source-authentic.
- Root `brute_force.py`, `char_locator.py`, and preserved generated images remain legacy/provenance debt and must not be deleted or relocated without hash/reference reconciliation.

## Coordination / governance state

- `AGENTS.md`, `docs/AI_AGENT_INTEGRATION.md`, and `docs/AUTOMATED_AGENT_OPERATIONS.md` remain aligned on current-main authority, evidence preservation, canonical registration, bounded PR work, dynamic website discovery, collision avoidance, and independent verification.
- PR #53 was rebuilt from the then-current main instead of accepting PR #48's stale shared-state snapshot wholesale; this preserved PR #50/#51 source-history and coordination state.
- Open PRs #47, #49, and #52 remain separate research lanes. No analyzer integration path overlaps their raw snapshot files.
- Normal user-facing discovery continues through canonical `data/tools.json` and generated site-data / Command Site paths; no bespoke `site/index.html` edit was needed for `btc310-image-analyzer`.
- `docs/AGENT_HANDOFF.md` is append-only. This post-merge sync appends a new evidence-backed handoff rather than rewriting or deleting previous entries.

## Known debt

- Reconcile/replay PR #47 then PR #49 chronologically through canonical source history/registry validation; preserve the NASA Gateways candidate.
- Evaluate PR #52 only after earlier source state is canonical and preserve exact eligibility/prize/submission evidence before promotion.
- Independently confirm merged-main generated discovery for `btc310-image-analyzer` and keep its `experimental` boundary unless stronger evidence exists.
- Verify external provenance for `310_challenge.png` before escalating 310 semantic/decryption hypotheses.
- Continue hash/provenance-preserving root artifact migration and remaining legacy solver inventory.
- Add further provenance-preserving official-source adapters where current sources support exact evidence.

## Current operating priorities

1. Repo Integrity: independently confirm `btc310-image-analyzer` on merged main through generated Tools/Command Site/repository-browser data and retain the `experimental` claim boundary unless independently justified otherwise.
2. Research/integration: preserve chronological source replay by reconciling PR #47 first, then PR #49; only then evaluate the later PR #52 lead for canonical promotion.
3. 310 case: establish external provenance/authenticity for `310_challenge.png` before interpreting password/decryption or hidden-data hypotheses as source-authentic.
4. Continue legacy solver/root-artifact inventory without deleting or moving primary evidence before hashes/references are reconciled.

## Next handoff

Build Integration independently re-read the current operating contract, current state, work/integration queues, tool/toolset registries, active 310 case, open PRs and PR #53 final CI. PR #53 final head `3f8ac546...` passed Core `32663349865` on Python 3.11/3.12/3.13 and Daily Maintenance `32663349853`, had no unresolved review threads, and was mergeable. It was merged as `73fa9fa5314d476829c8b3bdbc0915203ba6df2e`. Canonical `main` now contains `btc310-image-analyzer` at `experimental`, with deterministic direct-script tests, read-only default behavior, explicit managed outputs, active-case linkage and generated discovery coverage. No source-history timestamps, research raw snapshots, target authorization state, primary evidence, or bespoke website HTML were changed. Exact next independent check is merged-main generated discovery plus preservation of the analyzer's non-solve/experimental boundary; chronological research replay remains PR #47 then PR #49.
