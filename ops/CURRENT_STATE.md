# Current Repository State

Last reconciled: 2026-08-20 08:00 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `1ed31129c9e92a481d9f7f08c0dc09066a77f2fd`, the merge of PR #33 (`Research: refresh current CTF and cryptography source health`).
- PR #33 changed only `data/intelligence_sources.json` and `data/source_check_history.json`; its source-health contribution is preserved on current `main`.
- `data/integration_queue.json` remains empty and no open repository issue was found during this build pass.
- The public GitHub Pages Operations Workspace is reachable and exposes the expected Opportunities, News / Intel, Cases, Tools, Evidence, Collection Health, source registry, prompts, and Agent Operations surfaces.
- Connected commit-run lookup did not surface post-merge workflow runs for `1ed31129...`; this is recorded as an observation, not interpreted as failure.

## Build / integration state

- `tools/catalog_link_health.py` remains merged as the bounded catalog/source URL inventory and migration diagnostic tool.
- `tools/opportunity_actionability.py` remains merged and registered as `opportunity-actionability` with `tested` maturity.
- PR #34 adds `tools/opportunity_evidence.py`, a local/network-free normalizer for source-backed lifecycle, submission-status and deadline evidence. It preserves every evidence statement, requires HTTPS sources and timezone-aware observation/deadline timestamps, assigns deterministic SHA-256 provenance, fails on conflicting newest evidence, and emits evaluator-ready records.
- PR #34 also adds `docs/OPPORTUNITY_EVIDENCE_WORKFLOW.md`, deterministic fixture/test coverage, and canonical `opportunity-evidence` tool registration with `tested` maturity.
- Research PR #33 merged after PR #34 was originally built. The build branch was reconciled with current `main` using two-parent merge commit `2b707d4d9614363eaaef2380cfd5e18a6b3437d3`, preserving PR #33 source/history changes and PR #34's eight-file implementation/coordination set without force-push or history rewriting.
- Reconciled head `2b707d4d...` passed Core validation run `32346752699` on Python 3.11, 3.12 and 3.13 and Daily Repository Maintenance run `32346752712`. Core passed the test suite, compile checks, intelligence source/history/feed validation, source collection reporting, artifact inventory, 310 migration verification, dashboard-data generation, and maintenance on all three Python versions.
- PR #34 remains open and mergeable for independent Repo Integrity review; neither opportunity tool was promoted beyond `tested`.
- The broader P2 freshness item remains in progress: deterministic preservation/normalization and evaluation exist, but source-specific acquisition adapters are still separate work and must preserve the same provenance contract.

## Current research / case state

- PR #33 refreshed the CTFtime and arXiv source-health lanes on current `main`; no duplicate intelligence, opportunity, or active case was created by that research pass.
- Cap remains a discovery lead only. Exact in-scope assets, exclusions, prohibited techniques, severity/reward rules and submission requirements are not preserved in canonical case evidence, so no active security case or testing has started.
- Aave V4, Midas and Puffer remain discovery/watch leads under the same exact-scope gate.
- `RsaCtfTool/RsaCtfTool` remains an evaluation lead pending overlap, dependency, license, maintenance-cost and deterministic-fixture review.
- The only structured active puzzle remains `research/active-puzzles/20260816-310-btc-challenge`; no solve claim is made.

## Known state / debt

- The evidence normalizer does not itself fetch source pages or mark sources fresh; agents/adapters must still acquire evidence from approved sources and preserve actual observation time and supporting source material.
- Exact bounty scope/exclusion/prohibited-technique/severity/submission material for high-value security leads remains unpreserved in canonical case evidence.
- Generated/legacy root artifacts remain a P1 cleanup item; preserve hashes and provenance before relocation.
- `docs/AGENT_HANDOFF.md` already contains the PR #34 build handoff, but its final sentence predates PR #33's merge; this reconciliation is recorded in PR #34 discussion and should be appended by the integrity/merge pass when it records the final merge disposition.

## Current operating priorities

1. Repo Integrity should independently replay `tests/test_opportunity_evidence.py`, verify conflict rejection and the evidence-normalizer -> actionability pipeline, confirm `opportunity-evidence` reaches generated Command Site/repository-browser data, and merge PR #34 only if satisfied.
2. Build source-specific live adapters only where official APIs/feeds/pages can be consumed safely while emitting the provenance-preserving evidence contract; keep network failures non-destructive.
3. Preserve complete Cap Sherlock scope/rules before considering any active security case; do not test first.
4. Evaluate `RsaCtfTool/RsaCtfTool` only after overlap/dependency/license/deterministic-test review.
5. Continue root-artifact migration only with hash/provenance preservation.

## Next handoff

PR #34 is reconciled onto current `main` at head `2b707d4d9614363eaaef2380cfd5e18a6b3437d3` and is green across Core validation and Daily Maintenance. Repo Integrity should independently verify semantics and generated-site discovery before merge. After that, the next bounded build candidate is one official-source adapter that emits the evidence provenance format or the `RsaCtfTool` integration evaluation.
