# Current Repository State

Last reconciled: 2026-08-18 20:05 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `dab0897bb452181b5d4329ead6a3ec7e6efa6f57`, the merge of PR #27 (`Build: add deterministic opportunity actionability evaluation`).
- PR #27 final head `60e224604c59ae16da3b9ab6eb57e313ec6834b9` passed Core validation run `32115134613` and Daily Repository Maintenance run `32115134660`. Core passed on Python 3.11, 3.12, and 3.13, including pytest, compile checks, intelligence source/history/feed validation, source collection reporting, artifact inventory, 310 evidence migration verification, dashboard-data generation, and maintenance checks.
- GitHub Pages remains publicly reachable at the Operations Workspace and exposes the expected workspace/navigation surfaces; the fetched live page still renders Tools, Cases, Evidence, Collection Health, source registry, and Agent Operations sections.
- `data/integration_queue.json` remains empty.
- Open research PR #28 is now stale/conflicting on shared coordination files because PR #27 merged first; its research data changes must be reconciled with current `main` rather than merged by choosing one side blindly.

## Build / integration state

- `tools/catalog_link_health.py` remains merged as the bounded catalog/source URL inventory and source-migration diagnostic tool.
- `tools/opportunity_actionability.py` is now merged and registered in `data/tools.json` as `opportunity-actionability` with `tested` maturity.
- The actionability evaluator requires an explicit timezone-aware `--as-of`, treats explicit closed submission state or passed deadlines as non-actionable, refuses to call broad `active` lifecycle metadata actionable without submission-phase proof, and never infers factual freshness from HTTP reachability or mutates canonical opportunity data.
- `tests/fixtures/opportunity_actionability.json` preserves the USA.gov / 3D Surface Fuels lifecycle-versus-submission mismatch plus open/upcoming/verify controls.
- `tests/test_opportunity_actionability.py` verifies documented direct-script execution, deadline precedence, lifecycle/submission separation, and timezone enforcement.
- Core validation produced dashboard-data artifacts for all three supported Python versions on the final PR head, supporting the normal registry-to-site-data path; no bespoke `site/index.html` changes were introduced.
- `toolsets/catalog.json` still contains only the reusable `repo-factory` toolset. The actionability evaluator is intentionally a standalone shared tool, not a toolset.

## Current research / case state

- The only structured active-puzzle directory remains `research/active-puzzles/20260816-310-btc-challenge`; no puzzle solve claim was made in this pass.
- Open PR #28 contains a newer Sherlock/Cap research contribution and passed its own Core, Daily Maintenance, and Intelligence Source Report workflows on head `566c89e1cb43650d2cd95eb0147355d75f0a0db9`, but its external claims remain a research contribution until merged/reconciled.
- Aave V4, Midas, Puffer, and Cap remain discovery/watch leads only until exact published scope/rules are preserved before any security testing.
- `RsaCtfTool/RsaCtfTool` remains an evaluation lead pending overlap, dependency, license, maintenance-cost, and deterministic-fixture review.

## Known state / debt

- The broader P2 catalog-freshness item remains open: the repository can now evaluate preserved structured lifecycle/submission/deadline evidence, but it does not yet define a provenance-preserving acquisition/refresh policy for those fields across arbitrary live sources.
- Post-merge workflow runs for merge commit `dab0897...` had not surfaced at this reconciliation check; do not claim the merge commit itself is independently green yet. The pre-merge final head is fully green.
- Research PR #28 requires conflict reconciliation against current `main`, preserving both its source/intelligence changes and the merged actionability state.
- Generated/legacy root artifacts remain a P1 cleanup item; preserve hashes and provenance before relocation.
- Exact bounty scope/exclusion/prohibited-technique/severity/submission material for high-value security leads remains unpreserved in canonical case evidence.

## Current operating priorities

1. Repo Integrity should independently replay the merged actionability fixture and confirm generated Tools/Command Site visibility from current `main`; keep maturity at `tested` unless that independent review supports promotion.
2. Reconcile research PR #28 with current `main`, preserving both the Sherlock/Cap research state and merged PR #27 coordination/tool state; rerun CI on the reconciled head before merge.
3. Define a provenance-preserving workflow/schema for acquiring and refreshing `lifecycle_status`, `submission_status`, and `submission_deadline` evidence before closing the broader P2 freshness item.
4. Evaluate `RsaCtfTool/RsaCtfTool` only after overlap/dependency/license/deterministic-test review.
5. Preserve exact published bounty scope/rules before activating any security case; no target testing first.

## Next handoff

Repo Integrity should independently verify `opportunity-actionability` on current `main`, including direct-script fixture replay and generated website discovery. The next build/reconciliation pass should resolve PR #28 against current main without discarding either lane, then rerun Core/maintenance/source validation before considering that research contribution mergeable.
