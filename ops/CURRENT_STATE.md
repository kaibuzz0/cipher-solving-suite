# Current Repository State

Last reconciled: 2026-08-27 08:05 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `c7817a106b4694dbf452ed33a7317840c0a1a9df`, the merge of PR #72 (`Research: reconcile HHS DS-MRN rules on current main`).
- Immediately before that, coordination-only PR #71 merged as `ce71987677de46c44922509e123ff108a267e009`. Its exact head `d1a3b9450112760200cc3deee5fa8d89b7e38af8` passed Core validation `33050076533` and Daily Repository Maintenance `33050076498`.
- PR #72 exact head `0e79c7b8e6eca7302e7e46dd3961f6adacaddad7` passed Core validation `33051244978` before merge. The PR changed only `intelligence/feeds/2026-08-24-source-health.json` and intentionally did not advance canonical source history, source-registry freshness, opportunities, active cases, tool/toolset registries, or site HTML.
- The previous Pages-backed main state remains the successful deployment from commit `94164e76350dd59dc6058fa4e4392b9bd28d382c` (`33008151160`). PR #70/#71/#72 did not alter site markup or canonical generated-data inputs that require a bespoke Pages implementation change.

## Build / integration state

- The HHS Digital Stockpile & Manufacturing Response Network Challenge research contribution is now preserved on current `main` through PR #72.
- The preserved Aug. 24 snapshot contains exact observations for `challenge-gov`, `ctftime-upcoming`, `sherlock-bounties`, and `ethglobal-events` at `2026-08-24T19:42:29Z`. Those observations are not yet canonical in `data/source_check_history.json` / matching source-registry timestamps.
- PR #72 independently verifies that the DS-MRN Phase 1 host still lists an August 28, 2026 at 8 PM deadline but does not state a timezone in the reviewed timeline; no timezone is inferred.
- Material actionability boundary: published Phase 1 rules prohibit AI-generated content for narrative development and video development. This repository must not generate a DS-MRN challenge submission. The lead is human-led opportunity intelligence only.
- PR #62 (Aug. 25 NASA RASC-AL/source health) and PR #66 (Aug. 26 source health/xTech Search 10 conflict) remain later contributed research and must not overtake the Aug. 24 replay.

## Current research / intelligence state

- PR #44 observations at `2026-08-22T07:42:16Z` are canonical through PR #50.
- Former PR #47 / merged PR #58 observations at `2026-08-22T19:42:58Z` are canonical through PR #60.
- Former PR #49 / merged PR #63 observations at `2026-08-23T07:42:04Z` are canonical through PR #67.
- Orbital Clarity raw research is canonical evidence through merged PR #70, but no structured active case was created.
- DS-MRN raw research is now canonical evidence through merged PR #72; the exact Aug. 24 source observations still require chronological replay before later source snapshots advance freshness.
- Public bounty/program listings remain discovery evidence only and are not authorization to test a target.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain canonically registered at `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal alpha extraction reproducibility is established, but external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, or a puzzle solve.
- Root legacy/generated artifacts remain provenance debt and must not be deleted or moved without hash/reference reconciliation.

## Known state / debt

- Canonical replay of the four exact Aug. 24 source observations is now the highest-priority source-integration item.
- The DS-MRN deadline timezone remains unresolved and must not be guessed; participant-specific eligibility and acceptance of Government unlimited-rights, tax, release, and indemnification terms remain human participation gates.
- PR #62 still requires complete NASA RASC-AL eligibility, deadline-timezone, judging/scoring, submission-limit, IP/publication, travel, and top-award verification before structured work.
- PR #66 still contains conflicting xTech|Search 10 official deadline surfaces and requires the actual full RFI/application evidence before actionability claims.
- Root legacy/generated artifacts still require hash- and reference-preserving migration.
- External provenance/authenticity for `310_challenge.png` remains unresolved.

## Current operating priorities

1. Replay the exact PR #72 Aug. 24 observations into canonical source history and matching source-registry timestamps, preserving predecessor fingerprints and `2026-08-24T19:42:29Z` exactly; validate source history/registry/report/intelligence/site-data/Core/Maintenance.
2. Keep DS-MRN at human-led intelligence only. Do not draft or generate its submission content because the published rules prohibit AI-generated narrative and video content.
3. Then reconcile PR #62 and PR #66 in chronology/source-overlap order.
4. Continue the 310 external-provenance gate and hash-preserving root-artifact inventory without inflating experimental capability claims.

## Coordination note

This build/integration pass merged green coordination PR #71, then merged one-file DS-MRN evidence PR #72 after its exact head passed Core validation. No source freshness was manufactured, no security target was activated, no opportunity was converted to an AI submission case, no tool maturity changed, no primary evidence was moved, and no bespoke website HTML was introduced.

## Next handoff

Repo Integrity / Build should independently verify the four Aug. 24 predecessor fingerprints against the current canonical source history, replay only those exact observations and corresponding registry timestamps, run source/intelligence/site-data/Core/Maintenance validation, and merge only if the chronological chain remains intact. PR #62 and PR #66 remain blocked behind that replay.
