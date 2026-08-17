# Current Repository State

Last reconciled: 2026-08-17 19:17 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Main currently includes merged research PR #23 at `d234397d20607a7b4f98cd8df184fcbe382e7d86`.
- Main Core validation run `32008197711` passed on Python 3.11, 3.12, and 3.13; Pages run `32008197700` passed for the same main commit. Later scheduled Intelligence Source Report run `32022878957` and Daily Repository Maintenance run `32017729563` also passed on that main commit.
- GitHub Pages currently reports `built`, public, HTTPS-enforced, and workflow-backed at `https://kaibuzz0.github.io/cipher-solving-suite/`.
- PR #22 registered the directly tested Command Site snapshot exporter in canonical `data/tools.json`.
- Canonical intelligence source/feed/history files and `data/integration_queue.json` are active; the integration queue is empty.
- The repository is connected to `kaibuzz0/Git-hub-command-site`; repository/tool/toolset state flows through generated snapshot/site-data paths rather than bespoke website edits.
- Case dashboard integration is already implemented: `scripts/build_site_data.py` scans `research/active-puzzles/*/case.json`, Pages packages `site-data/cases.json`, and `site/app.js` renders the Active Cases view. The stale TODO was reconciled on PR #24's branch.

## Build / integration state

- Open PR #24 on branch `agent/build-link-health-20260817` adds `tools/catalog_link_health.py` as a bounded catalog/source URL inventory and verification tool.
- Independent integrity review found the implementation consistent with repository policy: default inventory is network-free, replay is deterministic, live checks are bounded diagnostics, canonical catalogs are not mutated, and HTTP reachability is not represented as factual freshness.
- The tool detects invalid URL shape, healthy responses, HTTP failures, network failures, and likely source migrations when a successful response resolves to a different final URL. HEAD-specific 403/405 behavior remains an explicit diagnostic limitation rather than an automated truth signal.
- `data/tools.json` registers the shared tool as `catalog-link-health`; the Pages workflow copies canonical `data/tools.json`, and `site/app.js` renders user-visible registry entries dynamically. No bespoke site HTML is required.
- `tests/test_catalog_link_health.py` covers documented direct-script inventory, redirect/migration replay, HTTP-error replay, invalid non-HTTPS URL rejection, and external fixture-path portability.
- The first PR CI run exposed a fixture portability defect because external `--input` paths were assumed to be under repository root; the implementation was corrected without weakening tests.
- Latest PR #24 Core validation run `32009085665` passed Python 3.11, 3.12, and 3.13, including tests, compile checks, source/history/feed validation, artifact inventory, 310 migration verification, dashboard data generation, and maintenance. Daily Repository Maintenance run `32009085718` also passed.
- The `tested` maturity label is supported. No promotion to `verified` was made because bounded live semantics have not been independently exercised against a controlled redirect/error endpoint in this run.

## Current research/intelligence state

- The latest source-health pass reviewed CTFtime, HackerOne Directory, Code4rena contests, Sherlock contests, and Sherlock bug bounties and recorded real fingerprints in `data/source_check_history.json`.
- Aave V4 is published only as a high-value Sherlock bounty discovery lead; exact Scope-tab assets/exclusions/prohibited techniques/severity/reward/submission terms still need preservation before case activation or any testing.
- Midas remains a discovery lead with the same exact-scope preservation requirement.
- `github-search` and `arxiv-cryptography` remain never-checked; the arXiv fetch timed out and was not falsely marked fresh.

## Known state / debt

- The broader catalog freshness/age policy remains outstanding even though deterministic link-health/source-migration capability exists in PR #24.
- Generated/legacy root artifacts remain a P1 cleanup item; preserve hashes/provenance before relocation.
- Legacy solver inventory/input-output/dependency documentation remains P2 work.
- Several merged topic branches remain on the remote; do not prune automatically without evidence/dependency review.
- Security opportunity listings are discovery only; public availability is not authorization beyond exact published scope/rules.

## Current operating priorities

1. Let PR #24's new documentation-only integrity reconciliation rerun CI; merge only if the refreshed head remains green and mergeable.
2. Define the remaining catalog freshness/age policy without conflating HTTP reachability with factual currency.
3. Preserve and verify exact Aave V4 and Midas Sherlock scope/rules before deciding whether either merits an active case; do not test first.
4. Complete real checks for `github-search` and `arxiv-cryptography` without fabricating freshness on fetch failures.
5. Preserve root/legacy evidence and inventory legacy solver modules before cleanup/refactoring.

## Next handoff

The next integrity/release pass should inspect the refreshed PR #24 CI after this documentation-only reconciliation and merge it if all checks remain green. Research/case agents should keep Aave V4 and Midas in discovery-only state until exact scope/rules are preserved.
