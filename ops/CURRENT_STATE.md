# Current Repository State

Last reconciled: 2026-08-23 07:18 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `89584da98ada2101ced7bab8d480255c8d75b20f`, the merge of PR #45 after PR #44 had already merged.
- PR #44 (`Research: record Code4rena wind-down and source-health changes`) merged as `bf6de08f1daee1c1ceb82cf20a4d85af53dcc9de` and its two-file research lane is present on current `main`.
- PR #45 (`Build: verify 310 evidence reproduction non-destructively`) merged as `89584da98ada2101ced7bab8d480255c8d75b20f`. Its final head `f7415d849dbe90034b5da37ced4a7c1ec2540720` passed Core validation `32561434523` on Python 3.11/3.12/3.13 plus Daily Repository Maintenance `32561434467` before merge.
- Open coordination PR #46 is based directly on current `main` and owns `ops/CURRENT_STATE.md` plus `data/integration_queue.json`. Its prior head `d6977f05f7eccde6bb57a6ee0879811003fc13c1` passed Core validation `32593468443` on Python 3.11/3.12/3.13, including tests, compilation, source/history/feed validation, artifact inventory, 310 migration/reproduction verification, dashboard generation, and maintenance.
- Open research PR #47 is mergeable, adds only `intelligence/feeds/2026-08-22-afternoon-source-health.json`, and deliberately leaves canonical source history/registry untouched until PR #44's earlier observations are replayed. Its head `de3d559ab7eefc63895a564fd364a61d22ef1ea3` passed Core validation `32594783145`.
- Open build PR #48 is mergeable and does not touch PR #46's coordination files or PR #47's research snapshot. Its head `9f956d43c4859ba1fb8436e344281563a51d5547` passed Core validation `32595547270` across Python 3.11/3.12/3.13 plus Daily Repository Maintenance `32595547273`.
- There are no open repository issues.
- The public GitHub Pages Operations Workspace has been independently reachable with Opportunities, News / Intel, Cases, Tools, Evidence, Collection Health, source registry, prompts/workflow and Agent Operations surfaces; deployed-state recheck remains part of this integrity pass.
- `toolsets/catalog.json` still contains only `repo-factory` at `experimental`.

## 310 case / tool state

- `btc310-reproduction-verifier` is integrated through canonical `data/tools.json` at `experimental`, linked to case `20260816-310-btc-challenge`, and uses the existing registry/site-data discovery contract rather than bespoke website HTML.
- PR #45's verified artifact recorded exact regenerated/migrated matches for all four alpha outputs. `alpha_row310.bin` remains 368 bytes with SHA-256 `cffcecf0fc90fb313b58e90ee452427f94204c86970afd297606a0ca46d3f2f8`.
- This establishes repository-internal extraction reproducibility only. External provenance/authenticity for `310_challenge.png` remains unresolved, so password/decrypt/character hypotheses and any solve claim remain unverified/experimental.
- PR #48 contributes a repaired deterministic `btc310-image-analyzer` at `experimental` maturity through canonical `data/tools.json`, with direct-script regression coverage and explicit-output-only behavior. It must still receive independent integrity review before merge.
- Root `brute_force.py`, `char_locator.py`, and preserved generated image artifacts remain legacy/provenance debt; do not delete or relocate them without hash/reference reconciliation.

## Research / source-health state

- PR #44 updated canonical `data/opportunities.json` to reflect Code4rena's wind-down and added `intelligence/feeds/2026-08-22-source-health.json` with timestamped observations for `code4rena-contests`, `sherlock-bounties`, and `ctftime-upcoming`.
- The three stored fingerprints were independently recomputed with the repository normalization rule and match the raw snapshot exactly.
- Those observations have **not** yet been replayed into canonical `data/source_check_history.json` / `data/intelligence_sources.json`; the raw snapshot itself says replay is pending. PR #46 tracks this explicitly in `data/integration_queue.json` rather than allowing it to drift silently.
- PR #47 preserves later observations at `2026-08-22T19:42:58Z` plus a NASA Gateways candidate, but intentionally does not advance canonical source history ahead of the earlier PR #44 replay. Preserve that sequence when integrating.
- Do not manufacture freshness by copying timestamps alone. Replay the exact PR #44 observed strings through `scripts/source_check_history.py record ... --at 2026-08-22T07:42:16Z`, preserve notes, validate history/registry/report/site data, then replay the later PR #47 observations in timestamp order.

## Coordination / governance state

- `AGENTS.md`, `docs/AI_AGENT_INTEGRATION.md`, and `docs/AUTOMATED_AGENT_OPERATIONS.md` remain mutually consistent on current-main authority, canonical registries/site-data discovery, evidence preservation, independent verification, collision avoidance, and bounded PR-based changes.
- PR #46 owns current-state/integration-queue reconciliation; PR #47 owns a one-file later research snapshot; PR #48 owns the 310 analyzer/tool-registration lane. Their current changed-file scopes do not collide.
- Numerous historical `agent/*` branches remain on the remote. Many correspond to merged work; retain them unless provenance/reference review makes branch cleanup explicitly safe.
- `docs/AGENT_HANDOFF.md` is append-only. The connected write primitive available in this pass replaces whole files; because the journal is long and prior history must not be truncated, exact missing handoffs are preserved in PR descriptions until a safe append-capable pass reconstructs/appends them.
- A bounded indexed repository search for `subprocess` returned no matches in this pass. This is not represented as a complete security audit.

## Known debt

- External provenance for `310_challenge.png` remains the primary 310 evidence gate.
- PR #44 source-health observations still need canonical replay and registry freshness reconciliation; PR #47 later observations must follow that sequence if merged.
- Generated root artifacts still require hash/provenance-preserving relocation.
- Broader official-source opportunity/news adapters, catalog freshness, and legacy solver inventory remain incomplete.
- Several historical handoff entries remain preserved in PR descriptions/current-state history rather than the append-only journal because of connector-safe-append limitations.

## Current operating priorities

1. Re-run PR #46 validation after this concurrency reconciliation and merge it only if the refreshed head remains green and mergeable.
2. Replay the three PR #44 source-health observations through the canonical source-history command, validate source/history/report/site-data output, then process any later PR #47 observations in timestamp order before marking the integration item complete.
3. Independently review PR #48's analyzer direct-script behavior, non-mutation guarantees, canonical tool visibility, and `experimental` claim boundary before merge.
4. Independently verify external provenance for `310_challenge.png` before interpreting solver/decryption output as source-authentic.
5. Continue legacy solver/root-artifact inventory only with evidence and hash preservation.

## Next handoff

Repo Integrity reconciled current `main` after PRs #44 and #45 merged in sequence and then re-reconciled active concurrency after PRs #47 and #48 opened. PR #46 remains the sole owner of shared current-state/integration-queue coordination; PR #47 and PR #48 intentionally avoid those files, so no shared-file conflict is present. The material integration defect remains PR #44's merged raw source-health observations not yet replayed into canonical source history/registry. PR #47 adds a later replay-ready observation set that must follow PR #44 chronologically if merged. PR #48 is a separate experimental 310 analyzer contribution with green final-head Core/Daily CI but still requires independent integrity review. This state update intentionally does not rewrite source history, manufacture freshness, delete evidence, promote maturity, or claim a puzzle solve.