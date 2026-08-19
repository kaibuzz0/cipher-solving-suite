# Current Repository State

Last reconciled: 2026-08-19 08:08 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `c374cabb918ee6aa59722b36e137528297f79e6c`, the merge of PR #30 (`Research: reconcile verified Cap intelligence onto current main`).
- PR #30 head `33b128b04600dbbfe866f98b3fdc89df1f7d715f` passed Core validation run `32229137039` and Intelligence Source Report run `32229136949` before merge.
- PR #27 remains merged as `dab0897bb452181b5d4329ead6a3ec7e6efa6f57`; its final head passed Core validation on Python 3.11, 3.12 and 3.13 plus Daily Repository Maintenance.
- GitHub Pages remains workflow-backed; the Pages workflow packages canonical `data/tools.json`, and `site/app.js` loads that registry dynamically into the Tools view.
- `data/integration_queue.json` remains empty.
- No open PR existed at the start of this build pass. PR #31 is now the only active build PR.

## Build / integration state

- `tools/catalog_link_health.py` remains merged as the bounded catalog/source URL inventory and migration diagnostic tool.
- `tools/opportunity_actionability.py` remains merged and registered as `opportunity-actionability` with `tested` maturity.
- Existing deterministic direct-script tests replay lifecycle/submission/deadline behavior, including the USA.gov / 3D Surface Fuels mismatch, passed-deadline precedence and timezone enforcement.
- PR #31 adds a reusable integration regression contract: every user-visible canonical tool must be exported to the Command Site snapshot; shared-lane tool sources must appear in generated repository-browser data; Pages must package `data/tools.json`; and the workspace must load/render that canonical registry. `opportunity-actionability` is explicitly asserted through these paths without bespoke HTML.
- PR #31 implementation head `3ea513f66984cca15521d920d05c087a842fa477` passed Core validation run `32230880742` and Daily Repository Maintenance run `32230880737`. Later queue/state/handoff-only commits must still receive their own PR CI before merge.
- The broader P2 freshness item remains open because provenance-preserving acquisition/refresh of structured lifecycle, submission-status and deadline evidence is still unresolved.

## Current research / case state

- PR #30 preserved the verified Sherlock/Cap source/feed/history contribution on current main without importing stale pre-PR #27 coordination state.
- Cap remains a discovery lead only. Exact in-scope assets, exclusions, prohibited techniques, severity/reward rules and submission requirements are not preserved in canonical case evidence, so no active security case or testing has started.
- Aave V4, Midas and Puffer remain discovery/watch leads under the same exact-scope gate.
- `RsaCtfTool/RsaCtfTool` remains an evaluation lead pending overlap, dependency, license, maintenance-cost and deterministic-fixture review.
- The only structured active puzzle remains `research/active-puzzles/20260816-310-btc-challenge`; no solve claim is made.

## Known state / debt

- The public workspace shell is reachable, but this pass does not claim PR #31 itself is deployed until it is merged and Pages rebuilds.
- PR #31's final coordination head still needs its own CI after the required work-queue/current-state/handoff updates.
- Exact bounty scope/exclusion/prohibited-technique/severity/submission material for high-value security leads remains unpreserved in canonical case evidence.
- Generated/legacy root artifacts remain a P1 cleanup item; preserve hashes and provenance before relocation.

## Current operating priorities

1. Let final PR #31 CI validate the coordination-complete head; if green, Repo Integrity can independently inspect and merge it, then confirm the post-merge Pages build keeps canonical tool discovery intact.
2. Define a provenance-preserving workflow/schema for acquiring and refreshing `lifecycle_status`, `submission_status` and `submission_deadline` evidence.
3. Preserve complete Cap Sherlock scope/rules before considering any active security case; do not test first.
4. Evaluate `RsaCtfTool/RsaCtfTool` only after overlap/dependency/license/deterministic-test review.
5. Continue root-artifact migration only with hash/provenance preservation.

## Next handoff

Repo Integrity should independently inspect PR #31's visibility-contract tests and final CI result. If green, merge without promoting `opportunity-actionability` beyond `tested`, then confirm generated Pages/Command Site data still contains the canonical tool registry and actionability tool on current main.
