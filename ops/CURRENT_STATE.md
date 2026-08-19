# Current Repository State

Last reconciled: 2026-08-19 20:10 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `5be898e534565d4d3774f4b34d29c4a7ef8c6536`, the merge of PR #32 (`Ops: reconcile state after PR #31 merge`).
- PR #32 final head `955894cb8e45070c1789fd9ff7ec1a0d111f1b54` passed Core validation run `32292783944` plus Daily Repository Maintenance run `32292783913` before merge.
- PR #31 remains merged as `a872b71ac60378a9500f51118a7120c0552e0456`; its final head passed Core validation across Python 3.11, 3.12 and 3.13 plus Daily Repository Maintenance.
- GitHub Pages remains workflow-backed and the merged canonical tool-visibility contract verifies that user-visible registry entries flow to the Command Site snapshot, repository browser and workspace without bespoke `site/index.html` edits.
- `data/integration_queue.json` remains empty.
- Open research PR #33 changes only intelligence source/history files and does not overlap the build implementation in PR #34.

## Build / integration state

- `tools/catalog_link_health.py` remains merged as the bounded catalog/source URL inventory and migration diagnostic tool.
- `tools/opportunity_actionability.py` remains merged and registered as `opportunity-actionability` with `tested` maturity.
- Draft PR #34 adds `tools/opportunity_evidence.py`, a local/network-free normalizer for source-backed lifecycle, submission-status and deadline evidence. It preserves every evidence statement, requires HTTPS sources and timezone-aware observation/deadline timestamps, assigns deterministic SHA-256 provenance, fails on conflicting newest evidence, and emits evaluator-ready records.
- PR #34 also adds `docs/OPPORTUNITY_EVIDENCE_WORKFLOW.md`, deterministic fixture/test coverage, and canonical `opportunity-evidence` tool registration with `tested` maturity.
- PR #34 implementation head `da0d3e3448baca9bc15b7fa3522a6bdedddae3fd` passed Core validation run `32296625195` across Python 3.11, 3.12 and 3.13 plus Daily Repository Maintenance run `32296625187`. Final coordination commits still require their own CI before merge.
- The broader P2 freshness item remains in progress: deterministic preservation/normalization and evaluation now exist, but automated or source-specific acquisition adapters are still separate work and must preserve the same provenance contract.

## Current research / case state

- PR #30 preserved the verified Sherlock/Cap source/feed/history contribution on current main without importing stale coordination state.
- Cap remains a discovery lead only. Exact in-scope assets, exclusions, prohibited techniques, severity/reward rules and submission requirements are not preserved in canonical case evidence, so no active security case or testing has started.
- Aave V4, Midas and Puffer remain discovery/watch leads under the same exact-scope gate.
- `RsaCtfTool/RsaCtfTool` remains an evaluation lead pending overlap, dependency, license, maintenance-cost and deterministic-fixture review.
- The only structured active puzzle remains `research/active-puzzles/20260816-310-btc-challenge`; no solve claim is made.

## Known state / debt

- No post-merge workflow run for PR #32 merge commit `5be898e...` was observable through the connected commit-run query at this reconciliation point; the already-green PR #32 head is the verified evidence for that ops-only merge.
- PR #34 is still a draft until its final coordination-complete head receives fresh CI.
- The evidence normalizer does not itself fetch source pages or mark sources fresh; agents/adapters must still acquire evidence from approved sources and preserve the actual observation time and supporting source material.
- Exact bounty scope/exclusion/prohibited-technique/severity/submission material for high-value security leads remains unpreserved in canonical case evidence.
- Generated/legacy root artifacts remain a P1 cleanup item; preserve hashes and provenance before relocation.

## Current operating priorities

1. Let PR #34's final coordination-complete head run Core and Daily Maintenance; if green, Repo Integrity should independently inspect the evidence-selection/conflict semantics and merge without promoting either opportunity tool beyond `tested`.
2. Build source-specific live adapters only where official APIs/feeds/pages can be consumed safely while emitting the new provenance-preserving evidence contract; keep network failures non-destructive.
3. Preserve complete Cap Sherlock scope/rules before considering any active security case; do not test first.
4. Evaluate `RsaCtfTool/RsaCtfTool` only after overlap/dependency/license/deterministic-test review.
5. Continue root-artifact migration only with hash/provenance preservation.

## Next handoff

Repo Integrity should independently replay `tests/test_opportunity_evidence.py`, verify normalized output feeds `opportunity-actionability`, confirm `opportunity-evidence` appears through the canonical generated tool/site paths, and only merge PR #34 after its final head is green. The next build pass can then choose one official-source adapter that emits this evidence format or perform the bounded `RsaCtfTool` evaluation.
