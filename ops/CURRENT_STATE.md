# Current Repository State

Last reconciled: 2026-08-20 19:17 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `c024c76cc99cc37c6ef8c0468f37117fa09028c6`, the merge of PR #34 (`Build: preserve opportunity status evidence provenance`).
- Repo Integrity independently reviewed PR #34 after its reconciliation with merged research PR #33 and found no blocking defect.
- Final reconciled PR head `edfc1ac917a99c097fa3de8ac1b50c5efee98ab3` passed Core validation run `32346858848` on Python 3.11, 3.12 and 3.13 plus Daily Repository Maintenance run `32346858730`.
- Python 3.11 CI reported 44/44 tests passing, including direct-script opportunity evidence normalization, conflict rejection, evidence -> actionability integration, Agent Operations data parsing, dynamic site-data generation, repository-browser discovery, and canonical tool visibility.
- Source registry validation reported 16 valid sources; source history reported 32 valid checks; intelligence feed validation reported 12 valid items; 310 migration verification passed with no errors.
- GitHub Pages Operations Workspace is publicly reachable and exposes Opportunities, News / Intel, Cases, Tools, Evidence, Collection Health, source registry, prompts, workflow, and Agent Operations surfaces.
- `data/integration_queue.json` remains empty and no open repository issue was found during this integrity pass.

## Build / integration state

- `tools/catalog_link_health.py` remains merged as the bounded catalog/source URL inventory and migration diagnostic tool.
- `tools/opportunity_actionability.py` remains merged and registered as `opportunity-actionability` with `tested` maturity.
- PR #34 merged `tools/opportunity_evidence.py`, `docs/OPPORTUNITY_EVIDENCE_WORKFLOW.md`, deterministic fixture/tests, and canonical `opportunity-evidence` registration at `tested` maturity.
- The evidence normalizer is network-free, requires absolute HTTPS source URLs, timezone-aware observation/deadline timestamps and supporting excerpts, preserves every evidence statement with deterministic SHA-256 digests, selects the newest non-conflicting evidence per supported field, and fails closed on equally-new conflicting evidence.
- PR #34 preserved PR #33's source/history refresh while reconciling the stale branch with current main; no force-push or history rewrite was used.
- Canonical website discovery remains covered by `tests/test_tool_visibility_contract.py`: user-visible tools flow from `data/tools.json` into the Command Site snapshot and generated repository-browser data, and Pages/workspace consume the canonical registry rather than bespoke tool HTML.
- Neither opportunity tool has been promoted beyond `tested`; no live source-acquisition capability is claimed.

## Current research / case state

- PR #33's CTFtime and arXiv source-health refresh remains preserved on main.
- Cap remains a discovery lead only. Exact in-scope assets, exclusions, prohibited techniques, severity/reward rules and submission requirements are not preserved in canonical case evidence, so no active security case or testing has started.
- Aave V4, Midas and Puffer remain discovery/watch leads under the same exact-scope gate.
- `RsaCtfTool/RsaCtfTool` remains an evaluation lead pending overlap, dependency, license, maintenance-cost and deterministic-fixture review.
- The only structured active puzzle remains `research/active-puzzles/20260816-310-btc-challenge`; no solve claim is made.

## Known state / debt

- The evidence normalizer does not fetch source pages or mark sources fresh. Source-specific acquisition adapters remain separate work and must preserve actual observation time, supporting evidence and non-destructive failure behavior.
- Core CI reported 15 of 16 source lanes currently due under configured freshness SLAs; this is collection debt, not schema failure.
- Artifact inventory remains intentionally non-destructive: 40 items, 10 duplicate groups and 11 orphaned items were inventoried. Maintenance continues to warn about generated root images; relocation remains gated on hash/provenance preservation.
- Existing remote merged/topic branches remain cleanup candidates but were not deleted because they may retain useful provenance or external references.
- CI logs show GitHub-hosted actions currently emit Node.js 20 deprecation warnings while being forced onto Node 24; the workflows still pass, but action-version refresh should be treated as future supply-chain/maintenance work rather than an emergency defect.
- Post-merge workflow runs for merge commit `c024c76...` were not independently observed in this pass; the final green PR merge ref is the verification basis for the merged implementation.

## Current operating priorities

1. Build one bounded official-source adapter that emits the provenance-preserving opportunity evidence contract and keeps network failures non-destructive, or perform the `RsaCtfTool` overlap/dependency/license/deterministic-fixture evaluation.
2. Refresh due source lanes through the canonical source-history workflow without promoting discovery listings into testing authorization.
3. Preserve complete Cap Sherlock scope/rules before considering any active security case; do not test first.
4. Continue root-artifact migration only with hash/provenance preservation and case-link reconciliation.
5. Review GitHub Actions versions/deprecation warnings as bounded maintenance; do not weaken validation to silence warnings.

## Next handoff

PR #34 is merged and independently verified at `c024c76cc99cc37c6ef8c0468f37117fa09028c6`. The next build/research role should either add one official-source acquisition adapter that emits `opportunity-evidence` input with preserved provenance or complete the bounded `RsaCtfTool` integration evaluation. Repo Integrity should keep both opportunity tools at `tested` until a live adapter is separately exercised and evidenced.
