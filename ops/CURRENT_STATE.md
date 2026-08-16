# Current Repository State

Last reconciled: 2026-08-16 19:39 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Latest `main` commit inspected: `03416162ff0a47f73b575df70b78465beda5be79` (`Merge pull request #7 ... Tooling/repo starter kit`).
- Recurring-agent operating contract and `data/integration_queue.json` are present on `main` following PR #6.
- No open pull requests or open GitHub issues were present before the research branch was opened.
- Canonical tool registry exists at `data/tools.json`; canonical intelligence source/feed/history files are active.
- Repository operating contract, maintenance policy, work queue, intelligence workflow, case workflow, automated-agent operations contract, and agent handoff are present.

## Current research/intelligence state

- The old Challenge.gov discovery endpoint is no longer current: Challenge.gov was sunset on March 30, 2026. The research pass updated the stable `challenge-gov` registry entry to the official USA.gov active federal challenges page while preserving the ID for compatibility.
- USA.gov currently lists active federal challenges. The Connecting Talent to Opportunity Challenge is listed through April 1, 2028 with $15,000,000 in total cash prizes, but eligibility is specialized and must be checked on the hosting competition page before treating it as directly actionable.
- ETHGlobal's official calendar still lists ETHOnline 2026 for September 4-16, followed by Tokyo and Mumbai events later in 2026.
- Sherlock bug-bounty pages reviewed during this pass report current LIVE programs; Midas is listed with a 500,000 USDC maximum reward. A listing is not authorization beyond the exact program scope/rules.
- Source check history now contains real first-seen checks for the federal challenge source, ETHGlobal events, and the newly registered Sherlock bug-bounty lane.

## Known state / debt

- Generated/legacy root artifacts remain a documented P1 cleanup item; preserve hashes/provenance before relocation.
- Link-health/catalog freshness automation remains P2 work and is increasingly important because the Challenge.gov migration demonstrated real source drift.
- GitHub Search, HackerOne directory, Code4rena contests, Sherlock contests, and arXiv cryptography remain never-checked in the canonical registry and need real source checks in later research passes.
- Legacy solver inventory/input-output/dependency documentation remains P2 work.
- The GitHub Pages UI dark workspace should remain visually unchanged unless a specific defect is verified; data/feed updates may continue to flow through the normal Pages build.

## Current operating priorities

1. Review and preserve the exact Midas Sherlock bounty scope/rules before deciding whether to open an active case; do not test until scope is verified.
2. Continue real source checks for never-checked primary/discovery lanes, prioritizing HackerOne, Code4rena, Sherlock contests, GitHub Search, and arXiv cryptography.
3. Add deterministic link-health/source-migration checks so retired endpoints like Challenge.gov are detected earlier.
4. Keep `main`, CI, Pages, registries, handoffs, and documentation aligned.
5. Preserve and inventory research artifacts before relocation.

## Next handoff

The build/integration role should treat the source-migration discovery as justification for link-health/catalog freshness tooling. For the Midas bounty, only create an active case after the exact published scope, exclusions, severity/reward rules and submission terms are preserved and shown to be appropriate for authorized work.
