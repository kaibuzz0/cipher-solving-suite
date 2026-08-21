# Current Repository State

Last reconciled: 2026-08-21 07:20 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `a2b015ea951b49e65d437c495948a4f586ef2c60`, the merge of PR #37 (`Build: add NIH challenge evidence adapter`).
- Repo Integrity independently inspected PR #37's adapter, deterministic fixture/tests, canonical tool registration, coordination patch, and current concurrent PR state before merge.
- Final PR head `75a0e078157bceb1d5eb644044d19b90057fcfb2` was mergeable and passed Core validation run `32412721156` plus Daily Repository Maintenance run `32412721152`.
- The public GitHub Pages Operations Workspace is reachable and exposes the expected Opportunities, News / Intel, Cases, Tools, Evidence, Collection Health, source-registry, prompts, workflow and Agent Operations surfaces.
- `data/integration_queue.json` remains empty and no open repository issues were found during this integrity pass.
- Open research PR #36 remains isolated to `data/intelligence_sources.json` and `data/source_check_history.json`; it did not overlap PR #37's implementation/coordination paths at merge time.

## Build / integration state

- PR #37 merged `tools/nih_challenge_evidence.py`, deterministic NIH fixture/tests, canonical `nih-challenge-evidence` registration at `tested` maturity, evidence-workflow documentation, queue/state coordination updates and an append-only build handoff.
- The NIH adapter reads the official NIH challenge index by default or a deterministic local HTML fixture, requires exact title matching, preserves source wording and timezone-aware observation time, and emits evidence consumed by `tools/opportunity_evidence.py`.
- It emits lifecycle/submission status only from supported status-shaped text and emits a deadline only when the matched source text contains an explicit clock time and timezone. Date-only status is preserved without inventing an end-of-day timestamp.
- The regression suite covers the NCI date-only status, LymeX explicit ET deadline normalization, TOPx `Open Data` prose preceding the real phase status, missing-title failure, timezone enforcement and adapter -> evidence-normalizer compatibility.
- Network/source-shape/timestamp failures return non-zero before writing requested output. The adapter does not mutate canonical opportunities, mark a source fresh, prove eligibility/prize entitlement or activate security testing.
- Dynamic tool discovery remains canonical through `data/tools.json` and the existing tool-visibility/site-data contract; no bespoke `site/index.html` entry was added.
- Independent current-source review found the NCI ODS registration PDF states an October 5, 2026 11:59 PM Eastern submission deadline. That does not contradict the index adapter: the adapter intentionally preserves only index evidence and does not claim complete detail-page evidence.

## Current research / case state

- Research PR #36 remains open and mergeable, with a bounded federal-challenge source-health refresh. If it merges after this reconciliation, its two-file source/history changes should be preserved without overwriting the NIH adapter state.
- NCI ODS Impact Prize remains a strong evidence-enrichment candidate: preserve exact eligibility, prize, entry/submission criteria and supporting primary-source evidence before canonical promotion.
- Cap remains a discovery lead only. Exact scope, exclusions, prohibited techniques, severity/reward rules and submission requirements are not preserved in canonical case evidence, so no active security testing should start.
- Aave V4, Midas and Puffer remain discovery/watch leads under the same exact-scope gate.
- `RsaCtfTool/RsaCtfTool` remains an evaluation lead pending overlap, dependency, license, maintenance-cost and deterministic-fixture review.
- The only structured active puzzle remains `research/active-puzzles/20260816-310-btc-challenge`; no solve claim is made.

## Known state / debt

- The NIH adapter is intentionally narrow and remains `tested`, not `live`. It does not yet preserve detail-page eligibility, prize or full submission-rule evidence.
- NIH markup/wording can change; exact-title matching and fail-closed source-shape handling reduce silent misclassification but do not eliminate source-shape maintenance risk.
- Source freshness debt remains; a source being due is collection debt rather than schema failure.
- Artifact inventory remains intentionally non-destructive; generated root artifacts still require hash/provenance-preserving relocation.
- Existing merged/topic branches remain cleanup candidates but were not deleted because they may retain useful provenance or external references.
- GitHub Actions has emitted Node.js action-runtime deprecation warnings while workflows remain green; action-version refresh remains bounded supply-chain maintenance debt.
- A fresh post-merge workflow run for merge commit `a2b015ea...` was not independently observed in this pass; the green final PR head is the implementation verification basis.
- `docs/AGENT_HANDOFF.md` should receive a post-merge integrity entry. The available connector write primitive replaces the whole file and the full append-only journal could not be safely reconstructed from the truncated read surface, so this pass did not risk truncating prior history. The exact handoff is preserved in the reconciliation PR description for safe append by the next write-capable role.

## Current operating priorities

1. Safely append the post-PR37 integrity handoff recorded in the reconciliation PR, then merge the documentation-only reconciliation after its fresh checks are green.
2. Review/reconcile PR #36 against current `main`; preserve its source/history changes and rerun its validations if its base is stale.
3. Enrich NCI ODS evidence from official detail materials with eligibility, prize and submission criteria before canonical opportunity promotion.
4. Continue other official-source adapters only where source shape, provenance and non-destructive failure behavior are bounded.
5. Continue root-artifact migration only with hash/provenance preservation and case-link reconciliation.

## Next handoff

PR #37 is merged and independently integrity-reviewed at `a2b015ea951b49e65d437c495948a4f586ef2c60`. Keep `nih-challenge-evidence` at `tested`. The next integrity/build role should first append the preserved post-merge handoff safely, then merge this state-reconciliation PR if fresh CI remains green. After that, reconcile PR #36 or enrich the NCI ODS evidence set from primary detail materials without treating index status alone as complete actionability evidence.
