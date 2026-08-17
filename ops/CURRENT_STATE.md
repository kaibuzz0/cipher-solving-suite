# Current Repository State

Last reconciled: 2026-08-17 07:55 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- PR #22 (`Integrity: reconcile Command Site registry and current state`) merged as `7ebbb08944ee5121b37b60202ec124d5f5d0bf14`, preserving the Command Site tool-registry reconciliation before this research branch proceeds.
- Baseline Core validation run `31981879956` passed on Python 3.11, 3.12, and 3.13, and Pages run `31981879953` passed on the same pre-PR22 main baseline.
- GitHub Pages reports `built`, public, HTTPS-enforced, and workflow-backed at `https://kaibuzz0.github.io/cipher-solving-suite/`.
- The documented and directly tested `scripts/export_command_site_snapshot.py` command is now registered in canonical `data/tools.json` through merged PR #22.
- Canonical intelligence source/feed/history files and `data/integration_queue.json` are active; the integration queue is empty.
- The repository is connected to `kaibuzz0/Git-hub-command-site`; PRs #20/#21 added bounded repository snapshot/tree export without replacing canonical repository data.
- Research PR #23 has passed its Intelligence Source Report, Daily Repository Maintenance, and full Core validation matrix on Python 3.11, 3.12, and 3.13.

## Current research/intelligence state

- The source-health pass reviewed CTFtime, HackerOne Directory, Code4rena contests, Sherlock contests, and Sherlock bug bounties and recorded real fingerprints in `data/source_check_history.json`.
- CTFtime's upcoming calendar has rolled forward: the next listed event is CTFZone on August 19 and the next online cluster begins August 21 with BrunnerCTF, PwnSec, z0d1ak, Haruulzangi, E0F and TallDwarf. Existing late-August intelligence already covers the useful planning window, so no duplicate feed item was added.
- Code4rena currently shows submissions closed; K2 ($135,000 USDC) and Rujira ($40,000 USDC) are report-in-progress. No open contest was promoted.
- Sherlock's current contests page reports zero contests in the fetched view. No contest was promoted.
- HackerOne's Directory remains an active discovery surface; individual program scope/rules remain mandatory before any security work.
- Sherlock's current bug-bounty listing now highlights Aave V4 at a $2,500,000 maximum reward. The Aave V4 program page was independently re-opened and reports LIVE status, so a sourced high-value intelligence item was published. The fetched page did not expose the full Scope-tab contents, so no active testing case was created.
- Midas remains LIVE at 500,000 USDC on its current program page. Its exact scope/rules still need preservation before case activation.
- arXiv Cryptography remains `never-checked` because the official recent-list fetch timed out during this pass; it was not falsely marked fresh. GitHub Search also remains never-checked.

## Known state / debt

- Generated/legacy root artifacts remain a P1 cleanup item; preserve hashes/provenance before relocation.
- Deterministic link-health/source-migration tooling remains high-value work because Challenge.gov already demonstrated real endpoint drift.
- Legacy solver inventory/input-output/dependency documentation remains P2 work.
- `github-search` and `arxiv-cryptography` remain never-checked source lanes.
- Several merged topic branches remain on the remote. Treat them as cleanup candidates only after confirming no preserved evidence or active external workflow depends on them; do not delete them automatically.
- Security opportunity listings are discovery only; a public page, contract, repository, or bounty listing is not authorization beyond exact published scope/rules.

## Current operating priorities

1. Preserve and verify the exact Aave V4 Sherlock scope, exclusions, prohibited techniques, severity/reward rules and submission terms before deciding whether it merits an active case; do not test first.
2. Preserve the same exact-scope material for Midas before case activation.
3. Complete real checks for `github-search` and `arxiv-cryptography` without fabricating freshness on fetch failures.
4. Add deterministic link-health/source-migration checks.
5. Preserve root/legacy evidence and inventory legacy solver modules before cleanup/refactoring.

## Next handoff

The build/integration agent should prioritize deterministic link-health/source-migration tooling. The case-advancement agent should only activate Aave V4 or Midas after exact Sherlock scope/rules are preserved and confirmed appropriate for authorized work. The research agent should retry arXiv and perform a bounded GitHub Search source check on a later pass.
