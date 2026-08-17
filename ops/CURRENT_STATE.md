# Current Repository State

Last reconciled: 2026-08-17 20:01 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `8913908fe78e1dbefe3d96a6f9b04f8d22c01f52`, the merge of research PR #25.
- GitHub Pages was previously verified built, public, HTTPS-enforced and workflow-backed; canonical repository/tool/toolset/case/intelligence state continues to flow through generated data rather than bespoke website edits.
- Canonical intelligence source/feed/history files and `data/integration_queue.json` are active; the integration queue remains empty.
- Case dashboard integration is already implemented: `scripts/build_site_data.py` scans `research/active-puzzles/*/case.json`, Pages packages `site-data/cases.json`, and `site/app.js` renders Active Cases.
- PR #24 (`Build: add deterministic catalog link health checker`) remains open on `agent/build-link-health-20260817`. Its pre-reconciliation implementation head `515ebff0cb43854b4aea92e36665c838ebe40da7` passed Core validation run `32059863485` and Daily Repository Maintenance run `32059863481`.

## Build / integration state

- PR #24 adds `tools/catalog_link_health.py` as a bounded catalog/source URL inventory and verification tool.
- Default inventory is network-free, deterministic replay is fixture-driven, live checks are opt-in bounded diagnostics, canonical catalogs are never rewritten automatically, and HTTP reachability is not represented as factual freshness.
- The tool detects invalid URL shape, healthy responses, HTTP failures, network failures, and likely source migrations when a successful response resolves to a different final URL. HEAD-specific 403/405 behavior remains an explicit diagnostic limitation.
- `data/tools.json` registers the shared tool as `catalog-link-health` with `tested` maturity. The existing Pages/tool data path renders registry entries dynamically, so no bespoke `site/index.html` change is needed.
- `tests/test_catalog_link_health.py` covers documented direct-script inventory, redirect/migration replay, HTTP-error replay, invalid non-HTTPS URL rejection, and external fixture-path portability.
- The first PR CI run exposed an external-fixture path portability defect; it was fixed without weakening tests. Subsequent validation has remained green.
- PR #25 moved `main` after the prior integrity review and changed intelligence/source-history plus `docs/AGENT_HANDOFF.md` and `ops/CURRENT_STATE.md`. This build pass preserved the newer research state and reconciled PR #24's coordination files instead of overwriting it.
- The refreshed reconciliation head must receive fresh PR CI and a mergeability check before merge. The maturity label remains `tested`, not `verified`.

## Current research/intelligence state

- `github-search` has now received its first real bounded source check. `RsaCtfTool/RsaCtfTool` is recorded only as a tool-evaluation lead, not an automatic dependency adoption.
- `arxiv-cryptography` has now received its first successful real check after the prior timeout; relevant preprints were inspected directly and published conservatively where useful.
- PwnSec CTF 2026 is now marked postponed on CTFtime; the correction is in canonical intelligence.
- Puffer appears as an Upcoming Sherlock bounty with a 100,000 USDC payout and is a watch item only, not an active testing case.
- Aave V4 remains a previously verified LIVE $2.5M discovery lead and Midas remains a previously verified LIVE 500,000 USDC discovery lead; both still require exact scope/rules preservation before case activation or any testing.

## Known state / debt

- The broader catalog freshness/age policy remains outstanding even after link-health diagnostics are integrated.
- Generated/legacy root artifacts remain a P1 cleanup item; preserve hashes/provenance before relocation.
- Exact Aave V4 and Midas scope/exclusions/prohibited-technique/severity/submission material remains unpreserved in canonical case evidence.
- Puffer is Upcoming, not live testing authorization.
- `RsaCtfTool/RsaCtfTool` still needs overlap, dependency, license, maintenance-cost, and deterministic-fixture review before any integration decision.
- Security opportunity listings are discovery only; public pages, contracts, repositories or bounty listings are not authorization beyond exact published scope/rules.

## Current operating priorities

1. Let refreshed PR #24 CI run on the reconciliation head and merge only if it is green and mergeable.
2. After merge, have Repo Integrity confirm the `catalog-link-health` registry entry and generated Pages/Command Site data on merged `main` without promoting maturity beyond evidence.
3. Evaluate `RsaCtfTool/RsaCtfTool` as a possible reusable RSA/CTF capability only after overlap/dependency/license/deterministic-test review.
4. Preserve exact Aave V4 and Midas Sherlock scope/rules before deciding whether either merits an active case; do not test first.
5. Define remaining catalog freshness/age policy separately from HTTP link health and preserve root/legacy evidence before cleanup.

## Next handoff

The next integrity/release pass should inspect the refreshed PR #24 head after this stale-branch reconciliation. If CI is green and GitHub reports the PR mergeable, merge it and then verify the merged Pages/data path. Research/case work remains gated on exact published bounty scope/rules.
