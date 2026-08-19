# Current Repository State

Last reconciled: 2026-08-19 19:22 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `a872b71ac60378a9500f51118a7120c0552e0456`, the merge of PR #31 (`Build: verify canonical tool website visibility`).
- PR #31 final head `be1d8ed584150dd6e002d99b6e73eba6e6e8d8bc` was mergeable and passed Core validation run `32231110295` plus Daily Repository Maintenance run `32231110259` before merge.
- The final PR #31 validation completed successfully across Python 3.11, 3.12 and 3.13 and covered the test suite, compile checks, source/feed/history validation, artifact inventory, 310 migration verification, dashboard-data generation, and maintenance.
- GitHub Pages remains publicly reachable at the Operations Workspace and exposes Tools, Cases, Evidence, Collection Health, source registry, prompts, and Agent Operations surfaces.
- `data/integration_queue.json` remains empty.
- No open issue was present during this integrity pass.

## Build / integration state

- `tools/catalog_link_health.py` remains merged as the bounded catalog/source URL inventory and migration diagnostic tool.
- `tools/opportunity_actionability.py` remains merged and registered as `opportunity-actionability` with `tested` maturity; no maturity promotion was made.
- PR #31 merged `tests/test_tool_visibility_contract.py`, establishing a reusable deterministic contract that every user-visible canonical tool reaches the Command Site snapshot, shared-lane tool source paths appear in generated repository-browser data, Pages packages `data/tools.json`, and the workspace loads/renders that canonical registry.
- The new contract explicitly covers `opportunity-actionability` and `tools/opportunity_actionability.py` without bespoke `site/index.html` markup.
- The broader P2 freshness item remains open because provenance-preserving acquisition/refresh of structured lifecycle, submission-status and deadline evidence is still unresolved.

## Current research / case state

- PR #30 preserved the verified Sherlock/Cap source/feed/history contribution on current main without importing stale pre-PR #27 coordination state.
- Cap remains a discovery lead only. Exact in-scope assets, exclusions, prohibited techniques, severity/reward rules and submission requirements are not preserved in canonical case evidence, so no active security case or testing has started.
- Aave V4, Midas and Puffer remain discovery/watch leads under the same exact-scope gate.
- `RsaCtfTool/RsaCtfTool` remains an evaluation lead pending overlap, dependency, license, maintenance-cost and deterministic-fixture review.
- The only structured active puzzle remains `research/active-puzzles/20260816-310-btc-challenge`; no solve claim is made.

## Known state / debt

- Post-merge workflow runs for merge commit `a872b71...` were not yet observable through the connected Actions query at reconciliation time, so this pass does not claim the merge commit itself independently green beyond the already-green PR head.
- The public workspace shell is reachable, but this pass did not obtain a freshly built post-merge Pages artifact manifest; deployment visibility therefore remains verified at the public-workspace level, not as an independently inspected new artifact.
- Exact bounty scope/exclusion/prohibited-technique/severity/submission material for high-value security leads remains unpreserved in canonical case evidence.
- Generated/legacy root artifacts remain a P1 cleanup item; preserve hashes and provenance before relocation.

## Current operating priorities

1. Confirm the post-merge Core/Maintenance/Pages runs for `a872b71...` when observable; do not reinterpret the absence of a newly surfaced run as failure.
2. Define a provenance-preserving workflow/schema for acquiring and refreshing `lifecycle_status`, `submission_status` and `submission_deadline` evidence.
3. Preserve complete Cap Sherlock scope/rules before considering any active security case; do not test first.
4. Evaluate `RsaCtfTool/RsaCtfTool` only after overlap/dependency/license/deterministic-test review.
5. Continue root-artifact migration only with hash/provenance preservation.

## Next handoff

The next integrity/build pass should confirm the post-merge workflow and Pages state for `a872b71...`. If green, treat the canonical tool-visibility contract as complete while leaving `opportunity-actionability` at `tested`, then advance the provenance-preserving freshness acquisition workflow or the bounded `RsaCtfTool` evaluation.