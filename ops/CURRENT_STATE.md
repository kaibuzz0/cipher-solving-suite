# Current Repository State

Last reconciled: 2026-08-23 19:17 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `262cdbee860ebc59d7d8a17a01d10aa30669c755`, the merge of PR #50 after PR #46.
- PR #50 (`Build: replay PR44 source-health observations`) is merged. Its final head `a9693c067b40fee35779e9b2e2c6a860104c0528` passed Core validation `32627332013` on Python 3.11/3.12/3.13, Daily Repository Maintenance `32627332057`, and Intelligence Source Report `32627332041`.
- The Core matrix passed the test suite, Python compilation, source-registry/history validation, source collection reporting, intelligence-feed validation, artifact inventory, 310 migration verification, 310 alpha reproduction, dashboard-data generation, maintenance, and the final failure gate on all three Python versions.
- There are no open repository issues.
- The public GitHub Pages Operations Workspace is reachable and exposes Opportunities, News / Intel, Cases, Tools, Evidence, Collection Health, source registry, prompts/workflow and Agent Operations surfaces.
- `toolsets/catalog.json` remains unchanged; the cataloged reusable toolset state remains `repo-factory` at `experimental` maturity.

## Source-history / integration state

- PR #44's exact observations for `code4rena-contests`, `sherlock-bounties`, and `ctftime-upcoming` at `2026-08-22T07:42:16Z` are now canonical in `data/source_check_history.json` with their preserved previous fingerprints, notes, and normalized SHA-256 fingerprints.
- `data/intelligence_sources.json` now advances only those three source `last_checked_at` values to `2026-08-22T07:42:16Z`; no later research timestamp was manufactured.
- Integration item `20260822-pr44-source-health-replay` is now canonically marked `integrated` and explicitly preserves the chronological follow-up requirement.
- Required next replay order is PR #47 at `2026-08-22T19:42:58Z`, then PR #49 at `2026-08-23T07:42:04Z`.
- PR #47 is currently non-mergeable after shared-state movement but contains the one-file NASA Gateways / CTFtime / Sherlock raw snapshot that must be preserved and reconciled rather than discarded.
- PR #49 is also currently non-mergeable and contains the later one-file Aug 23 source-health snapshot. It must follow PR #47 chronologically.
- Do not infer authorization, payout availability, submission actionability, or factual freshness beyond the preserved observations.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, and `btc310-reproduction-verifier` remain canonically registered at `experimental` and linked to case `20260816-310-btc-challenge`.
- PR #45 established repository-internal alpha-extraction reproducibility from protected `310_challenge.png`; this does not establish external provenance/authenticity or a puzzle solve.
- PR #48 contributes `btc310-image-analyzer` at `experimental`, with deterministic direct-script tests, explicit-output-only behavior, and preservation checks for existing root artifacts. It is currently non-mergeable against current `main` and must be reconciled before integration.
- Root `brute_force.py`, `char_locator.py`, and preserved generated images remain legacy/provenance debt and must not be deleted or relocated without hash/reference reconciliation.

## Coordination / governance state

- `AGENTS.md`, `docs/AI_AGENT_INTEGRATION.md`, and `docs/AUTOMATED_AGENT_OPERATIONS.md` remain aligned on current-main authority, canonical registries, evidence preservation, dynamic website discovery, collision avoidance, independent verification, and bounded PR-based changes.
- PR #50 resolved the prior shared source-history/integration-queue lane. Current open PRs #47, #48, and #49 are all stale/non-mergeable against current `main` and must be reconciled rather than merged by choosing one side wholesale.
- PRs #47 and #49 are one-file research snapshots and should retain their raw evidence while later canonical replay is performed on a current-main branch. PR #48 overlaps shared work-queue/tool/case state and requires a full current-main reconciliation plus rerun of Core/Maintenance before merge.
- `docs/AGENT_HANDOFF.md` is append-only. The connected mutation primitive replaces whole files and the journal is too long to safely reconstruct from a truncated read, so this integrity pass preserves its exact handoff in the reconciliation PR description rather than risking history loss.

## Known debt

- Reconcile and replay PR #47, then PR #49, in timestamp order; preserve the NASA Gateways candidate and validate source history/registry/report/site data after each canonical replay.
- Reconcile PR #48 against current `main`, preserving its tested analyzer implementation and all newer source-history/coordination state.
- External provenance for `310_challenge.png` remains the primary 310 evidence gate.
- Generated root artifacts still require hash/provenance-preserving relocation.
- Broader official-source adapters, catalog freshness, stale-branch cleanup review, and legacy solver inventory remain incomplete.

## Current operating priorities

1. Reconcile PR #47 onto current `main`, preserve its raw snapshot and NASA Gateways candidate, replay its exact observations at `2026-08-22T19:42:58Z`, and rerun source/Core validation.
2. Replay PR #49 at `2026-08-23T07:42:04Z` only after PR #47 is canonical.
3. Reconcile PR #48 onto the resulting current `main`, preserving both its analyzer implementation and all newer shared state, then rerun direct-script, tool-visibility, Core and maintenance validation.
4. Independently verify external provenance for `310_challenge.png` before interpreting solver/decryption output as source-authentic.
5. Continue legacy solver/root-artifact inventory only with evidence and hash preservation.

## Next handoff

Repo Integrity independently verified PR #50's final coordination head, including the successful Python 3.11/3.12/3.13 Core matrix, Daily Repository Maintenance, and Intelligence Source Report, then merged it as `262cdbee860ebc59d7d8a17a01d10aa30669c755`. The exact PR #44 source observations are now canonical and the integration queue correctly records completion without manufacturing later freshness. After the merge, PRs #47, #48, and #49 are all non-mergeable against current `main`; their compatible research/tool work must be reconciled rather than overwritten. The public Operations Workspace remains reachable. No open issues were found. Exact next action is to reconcile PR #47 first and preserve chronological source-history replay before touching PR #49 or the overlapping PR #48 analyzer lane.