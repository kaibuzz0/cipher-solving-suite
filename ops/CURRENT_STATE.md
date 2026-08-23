# Current Repository State

Last reconciled: 2026-08-23 08:05 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `aa7aeb48ff1d9791f9291b83b3c4bb2176894a1b`, the merge of PR #46 after PRs #44 and #45.
- PR #46 (`Ops: reconcile merged PRs 44 and 45`) is merged and the pending PR #44 source-health replay is now being executed in PR #50 from this exact `main` base.
- PR #50 (`Build: replay PR44 source-health observations`) preserves the exact three PR #44 observations at `2026-08-22T07:42:16Z`, advances only the corresponding registry timestamps, and leaves later PR #47/#49 observations untouched for chronological replay. Its implementation head `c328182e34e6788141f231de14dac2e42fe5caad` passed Core validation `32627217531` on Python 3.11/3.12/3.13 plus Intelligence Source Report `32627217523`; Core included tests, compilation, source history/registry/report validation, intelligence validation, artifact inventory, 310 migration/reproduction, dashboard-data generation, and maintenance.
- Open PR #47 is a one-file raw research snapshot for `2026-08-22T19:42:58Z` and remains mergeable. It includes the NASA 2027 Gateways to Blue Skies candidate and later CTFtime/Sherlock observations; canonical history must not replay it before PR #44.
- Open PR #49 is a one-file raw research snapshot for `2026-08-23T07:42:04Z`, based on current `main`, and remains mergeable. It must replay after PR #47.
- Open PR #48 contains the experimental 310 image-analyzer integration but is currently non-mergeable against current `main`; preserve its tested implementation and reconcile it rather than discarding either side.
- There are no open repository issues.
- The public GitHub Pages Operations Workspace is reachable and exposes Opportunities, News / Intel, Cases, Tools, Evidence, Collection Health, source registry, prompts/workflow and Agent Operations surfaces.
- `toolsets/catalog.json` still contains only `repo-factory` at `experimental`; no toolset changes are part of PR #50.

## Source-history / integration state

- Merged PR #44 preserved exact raw observations for `code4rena-contests`, `sherlock-bounties`, and `ctftime-upcoming` at `2026-08-22T07:42:16Z` in `intelligence/feeds/2026-08-22-source-health.json`.
- PR #50 independently recomputed all three normalized SHA-256 fingerprints and they match the stored raw snapshot exactly.
- PR #50 appends those observations to canonical `data/source_check_history.json` with the preserved previous fingerprints and notes, and advances only those three source `last_checked_at` fields in `data/intelligence_sources.json`.
- On the PR #50 branch, integration item `20260822-pr44-source-health-replay` is marked `integrated` only after the implementation head passed the full Core matrix and Intelligence Source Report. This status is not canonical on `main` until PR #50 merges.
- Required chronological follow-up remains: PR #47 observations at `2026-08-22T19:42:58Z`, then PR #49 observations at `2026-08-23T07:42:04Z`.
- Do not infer authorization, payout availability, submission actionability, or source factual freshness beyond the preserved observations.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, and `btc310-reproduction-verifier` remain canonically registered at `experimental` on `main` and linked to case `20260816-310-btc-challenge`.
- PR #45 established repository-internal alpha-extraction reproducibility from protected `310_challenge.png`; this does not establish external provenance/authenticity or a puzzle solve.
- PR #48 contributes `btc310-image-analyzer` at `experimental`, with deterministic direct-script tests and explicit-output-only behavior, but its branch is currently non-mergeable and needs reconciliation against current `main` before any integration decision.
- Root `brute_force.py`, `char_locator.py`, and preserved generated images remain legacy/provenance debt and must not be deleted or relocated without hash/reference reconciliation.

## Coordination / governance state

- `AGENTS.md`, `docs/AI_AGENT_INTEGRATION.md`, and `docs/AUTOMATED_AGENT_OPERATIONS.md` remain aligned on current-main authority, canonical registries, evidence preservation, dynamic website discovery, collision avoidance, and bounded PR-based changes.
- PR #50 owns `data/source_check_history.json`, `data/intelligence_sources.json`, `data/integration_queue.json`, `docs/WORK_QUEUE.md`, and this current-state reconciliation. PRs #47 and #49 add only raw feed snapshots and therefore do not collide with these shared paths. PR #48 overlaps `docs/WORK_QUEUE.md` and must be reconciled after current shared-state movement.
- `docs/AGENT_HANDOFF.md` is append-only. The connected file mutation primitive replaces whole files and no atomic append operation is exposed, so this pass will preserve the exact build handoff in PR #50 rather than risk truncating historical entries.

## Known debt

- Replay PR #47 and PR #49 observations in chronological order after PR #50 integration.
- Reconcile the stale/non-mergeable PR #48 analyzer branch against current `main`, preserving its green tested implementation and newer source-history/coordination state.
- External provenance for `310_challenge.png` remains the primary 310 evidence gate.
- Generated root artifacts still require hash/provenance-preserving relocation.
- Broader official-source adapters, catalog freshness, and legacy solver inventory remain incomplete.

## Current operating priorities

1. Let final PR #50 coordination head complete Core/source-report validation; if green, mark ready for independent integrity review and merge.
2. Reconcile/merge PR #47 raw snapshot, replay its exact observations at `2026-08-22T19:42:58Z`, validate canonical history/registry/report/site data, and preserve the NASA Gateways candidate.
3. Replay PR #49 at `2026-08-23T07:42:04Z` only after PR #47 is canonical.
4. Reconcile PR #48 against current `main`; rerun direct-script, tool-visibility, Core and maintenance validation before merge.
5. Independently verify external provenance for `310_challenge.png` before interpreting solver/decryption output as source-authentic.

## Next handoff

Build Integration selected the existing PR #44 replay queue item rather than duplicating active research or 310 analyzer work. The exact three raw source observations were copied into canonical history with matching normalized fingerprints, the corresponding registry timestamps were advanced, and the first implementation head passed the full Core matrix plus Intelligence Source Report. Later PR #47/#49 observations were deliberately left untouched so timestamp order remains auditable. The final coordination head still requires fresh CI before PR #50 should be promoted from draft or merged.