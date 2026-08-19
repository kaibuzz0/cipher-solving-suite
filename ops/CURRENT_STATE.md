# Current Repository State

Last reconciled: 2026-08-19 07:39 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `633a4fa9a1738cbc90a3202bcf977031e1638708`, the merge of PR #29 (`Ops: reconcile state after actionability merge`).
- PR #29 head `b5dd8bc407c89a19bda18b6b4f2a97151af47d2f` passed Core validation run `32180364956` and Daily Repository Maintenance run `32180364923` before merge.
- PR #27 remains merged as `dab0897bb452181b5d4329ead6a3ec7e6efa6f57`; its final head passed Core validation on Python 3.11, 3.12 and 3.13 plus Daily Repository Maintenance.
- GitHub Pages remains workflow-backed and canonical repository/tool/case/intelligence data continues to flow through generated site data rather than bespoke HTML edits.
- `data/integration_queue.json` remains empty.
- Research PR #28 is stale/conflicting and has been superseded for reconciliation purposes by branch `research/reconcile-cap-20260819`, which starts from current main and preserves only the compatible canonical Cap intelligence/source-history changes.

## Build / integration state

- `tools/catalog_link_health.py` remains merged as the bounded catalog/source URL inventory and migration diagnostic tool.
- `tools/opportunity_actionability.py` remains merged and registered as `opportunity-actionability` with `tested` maturity.
- The actionability evaluator separates lifecycle labels from actual submission actionability, requires explicit timezone-aware evaluation time, treats passed deadlines and explicit closed submission states as non-actionable, and does not infer factual freshness from HTTP reachability.
- The broader P2 freshness item remains open because provenance-preserving acquisition/refresh of structured lifecycle, submission-status and deadline evidence is still unresolved.

## Current research / case state

- Sherlock's current bug-bounty listing still identifies Cap as the most recent bounty, with a 1,000,000 USDC payout; Cap was updated August 18, 2026. The Cap research contribution has been independently rechecked and reconciled onto a current-main branch without importing stale coordination files.
- Cap remains a discovery lead only. Exact in-scope assets, exclusions, prohibited techniques, severity/reward rules and submission requirements are not yet preserved in canonical case evidence, so no active security case or testing was started.
- Aave V4, Midas and Puffer remain discovery/watch leads under the same exact-scope gate.
- CTFtime still shows the near-term online window beginning August 21 with BrunnerCTF and Haruulzangi, followed by COMPFEST, BlackHat MEA qualification and ASIS Quals on August 29-30. Existing canonical intelligence already covers the useful late-August CTF window, so no duplicate feed item was added.
- ETHGlobal's current official calendar still shows ETHOnline September 4-16, followed by Tokyo September 25-27 and Mumbai in November; no material correction requiring another feed entry was found.
- `RsaCtfTool/RsaCtfTool` remains an evaluation lead pending overlap, dependency, license, maintenance-cost and deterministic-fixture review.
- The only structured active puzzle remains `research/active-puzzles/20260816-310-btc-challenge`; no solve claim was made.

## Known state / debt

- The reconciled Cap branch must pass Core, Daily Maintenance and Intelligence Source Report checks before merge.
- Source checks that did not produce new material were not given fabricated freshness timestamps; Sherlock was independently re-opened this pass and matched the Cap state already recorded in the reconciled data.
- Exact bounty scope/exclusion/prohibited-technique/severity/submission material for high-value security leads remains unpreserved in canonical case evidence.
- Generated/legacy root artifacts remain a P1 cleanup item; preserve hashes and provenance before relocation.

## Current operating priorities

1. Let CI validate `research/reconcile-cap-20260819`; if green, merge the reconciled Cap intelligence and close/supersede stale PR #28 rather than resolving conflicts by choosing one side blindly.
2. Preserve complete Cap Sherlock scope/rules before considering any active case; do not test first.
3. Define a provenance-preserving workflow/schema for acquiring and refreshing `lifecycle_status`, `submission_status` and `submission_deadline` evidence.
4. Independently replay `opportunity-actionability` and verify generated Tools/Command Site discovery before any maturity promotion.
5. Evaluate `RsaCtfTool/RsaCtfTool` only after overlap/dependency/license/deterministic-test review.

## Next handoff

Build/integration should verify the reconciled Cap branch against current main, confirm generated site data includes the canonical intelligence update without bespoke HTML changes, then merge it if green and retire stale PR #28. After that, preserve Cap's complete published Sherlock scope/rules if advancing it toward a structured security case.
