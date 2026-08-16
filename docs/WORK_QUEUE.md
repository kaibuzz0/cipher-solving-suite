# Shared Work Queue

This is the human-readable queue for AI agents. GitHub issues may mirror larger tasks; this file is the fast handoff surface inside the repository.

## Rules

- Claim one item at a time by adding your agent name and UTC timestamp.
- Do not claim work already assigned unless the previous agent explicitly releases it.
- Each completed item must link to evidence: commit/PR, tests, report, or reproducible command.
- Security targets require an official scope/rules URL before any testing.
- New opportunities must record when they were checked. Do not copy prize claims without a current official source.

## Priority queue

| Priority | State | Work | Owner | Evidence / Next step |
|---|---|---|---|---|
| P0 | in progress | Establish multi-agent operating structure and dashboard | ChatGPT | PR #1 |
| P0 | todo | Add deterministic unit tests for command-line tools | unclaimed | Cover catalog loading, filtering, earnings persistence |
| P0 | todo | Reconcile README and executable version/capability claims | unclaimed | README currently claims more live automation than exists |
| P1 | todo | Convert opportunity discovery from simulated data to verified catalog/live adapters | unclaimed | Keep fixtures explicitly labeled |
| P1 | todo | Inventory and relocate generated root artifacts without losing evidence | unclaimed | Preserve hashes and provenance |
| P1 | todo | Build case-template workflow for new puzzles/challenges | unclaimed | Add source, hash, clues, attempts, outcomes |
| P2 | todo | Add link health and catalog freshness checks | unclaimed | Avoid aggressive scraping; use official sources |
| P2 | todo | Add optional news/RSS adapters with cached timestamped output | unclaimed | Keep network failures non-destructive |

## Completed

Move completed rows here; do not delete them.
