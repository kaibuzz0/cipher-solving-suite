# Current Repository State

Last reconciled: 2026-08-18 08:10 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `b3a507c31b64b40edc676806d83c2777a0b79ce6`, the merge of PR #26 (`Research: refresh due source health and actionable deadline state`).
- PR #24's reconciled head `fd8d8d13b1c46181552fbfa1925c7f8a0b1aa9f2` passed Core validation run `32063939444` on Python 3.11, 3.12, and 3.13 and Daily Repository Maintenance run `32063939494` before merge.
- GitHub Pages was last independently recorded as `built`, public, HTTPS-enforced, and workflow-backed; canonical repository/tool/toolset/case/intelligence state flows through generated data rather than bespoke website edits.
- Canonical intelligence source/feed/history files and `data/integration_queue.json` remain active; the integration queue is empty.
- No open PRs or open issues existed at the start of this build pass.
- Case dashboard integration remains implemented: `scripts/build_site_data.py` scans `research/active-puzzles/*/case.json`, Pages packages `site-data/cases.json`, and `site/app.js` renders Active Cases.

## Build / integration state

- `tools/catalog_link_health.py` remains merged as the bounded catalog/source URL inventory and verification tool from PR #24.
- Branch `agent/build-actionable-freshness-20260818` adds `tools/opportunity_actionability.py`, a deterministic evaluator that separates broad lifecycle labels from actual entry/submission actionability.
- The evaluator requires an explicit timezone-aware `--as-of` timestamp, treats passed deadlines and explicit closed submission states as non-actionable, refuses to promote broad `active` lifecycle metadata without submission-phase proof, and does not mutate canonical catalogs or infer factual freshness from HTTP reachability.
- `tests/fixtures/opportunity_actionability.json` preserves the USA.gov / 3D Surface Fuels mismatch as a deterministic example: discovery lifecycle may remain active while the official-host submission window is already closed.
- `tests/test_opportunity_actionability.py` covers documented direct-script behavior, lifecycle-vs-submission separation, deadline precedence over stale open labels, and timezone enforcement.
- `data/tools.json` registers the evaluator as `opportunity-actionability` with `experimental` maturity pending CI and independent integrity review. Normal Pages/tool discovery should occur through the existing registry/site-data path; no bespoke `site/index.html` edit is planned.

## Current research/intelligence state

- The latest due-source refresh verified that USA.gov's broad active-challenge lifecycle can outlive an actionable submission window. The official host for the 3D Surface Fuels & Vegetation Modeling Prize Challenge says solution submissions closed July 20, 2026 and the final Demo Day moved to virtual on August 20; the canonical intelligence feed records this correction.
- Algora's current homepage still exposes a Bounties navigation lane, but several linked challenge pages are completed/historical; challenge-level open-state verification is required before promotion.
- Intigriti's public-program surface includes current VDP/bounty programs such as NVIDIA; no active case or testing was started.
- Code4rena still shows submissions closed with K2 and Rujira in report-in-progress state; Sherlock contests still show zero current contests. ETHGlobal's previously published ETHOnline September 4-16 window remains intact.
- `RsaCtfTool/RsaCtfTool` remains only a tool-evaluation lead pending overlap, dependency, license, maintenance-cost, and deterministic-fixture review.
- PwnSec CTF 2026 remains postponed on CTFtime; Puffer remains an Upcoming Sherlock bounty watch item.
- Aave V4 and Midas remain previously verified discovery leads but still require exact scope/rules preservation before case activation or any testing.

## Known state / debt

- Actionable freshness now has a bounded implementation on the build branch, but CI and independent integrity verification are still required before maturity promotion or closing the broader catalog-freshness queue item.
- The evaluator currently consumes explicit structured phase/deadline evidence; automated extraction from arbitrary live pages is intentionally out of scope for this pass.
- Generated/legacy root artifacts remain a P1 cleanup item; preserve hashes/provenance before relocation.
- Exact Aave V4 and Midas scope/exclusions/prohibited-technique/severity/submission material remains unpreserved in canonical case evidence.
- Puffer is Upcoming, not live testing authorization.
- Security opportunity listings are discovery only; public pages, contracts, repositories or bounty listings are not authorization beyond exact published scope/rules.

## Current operating priorities

1. Run Core validation and Pages/site-data compatibility on `agent/build-actionable-freshness-20260818`; if green, integrity should independently verify classification semantics and registry visibility before promoting maturity beyond `experimental`.
2. Evaluate `RsaCtfTool/RsaCtfTool` as a possible reusable RSA/CTF capability only after overlap/dependency/license/deterministic-test review.
3. Preserve exact Aave V4 and Midas Sherlock scope/rules before deciding whether either merits an active case; do not test first.
4. Keep Algora challenge discovery gated on challenge-level open/closed verification.
5. Preserve root/legacy evidence and inventory legacy solver modules before cleanup/refactoring.

## Next handoff

Integrity should independently verify the actionable-freshness evaluator against the deterministic fixture, confirm `opportunity-actionability` appears through generated tool/Command Site data without bespoke HTML, and confirm the broader P2 freshness item remains open until a policy exists for producing/maintaining the structured phase/deadline evidence the evaluator consumes.
