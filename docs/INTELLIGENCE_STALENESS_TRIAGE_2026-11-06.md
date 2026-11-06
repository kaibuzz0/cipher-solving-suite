# Intelligence source freshness triage — 2026-11-06

This is an **unverified queue snapshot**, not evidence of a successful external source check.

## Canonical state reviewed

- `data/intelligence_sources.json` currently advertises `updated_at: 2026-08-29T19:40:52Z`.
- `data/source_check_history.json` currently advertises `updated_at: 2026-08-29T19:40:52Z`.
- These dates are over two months old as of this triage. Source check timestamps must **not** be advanced without actually opening and inspecting the relevant source.
- The source registry and check history are canonical; this file does not replace either dataset.

## Next authorized collection pass

1. Run `python scripts/source_registry.py list --due` to obtain the current complete queue; prioritize official primary sources, then discovery sources.
2. For each source, inspect the actual official page, identify a dated observation and record the observed content through `scripts/source_check_history.py record`. Do not use this document as observed content.
3. Reconcile any opportunity with `data/opportunities.json`, `data/intelligence.json` and existing cases. For CTFs and bounty programs, verify registration status, permission/scope, eligibility, deadline and payout from the organizer, not an aggregator.
4. Run `python scripts/source_registry.py validate`, the source history validation, and site-data builder checks before publishing.
5. Keep stale claims marked unverified. In particular, August 2026 challenge and ETHOnline information must not be presented as a live November 2026 opportunity without new official evidence.

No external source fetches, eligibility checks, program authorizations, or test executions are claimed by this triage note.

## Reproducible overdue-source triage (registry metadata only)

As of 2026-11-06 19:36 UTC, **16 of 16 enabled sources** exceed their registry freshness SLA based solely on their saved `last_checked_at`. This calculation does not imply that any source was opened or checked today. The first eight by elapsed overdue hours are:

| Source ID | Type | Last recorded check | SLA | Hours overdue | Registered URL |
|---|---|---|---|---:|---|
| `hackerone-directory` | platform | 2026-08-17T07:43:55Z | 24h | 1931h | https://hackerone.com/directory/programs |
| `sherlock-contests` | platform | 2026-08-18T07:38:11Z | 12h | 1919h | https://audits.sherlock.xyz/contests |
| `algora-bounties` | platform | 2026-08-18T07:38:11Z | 12h | 1919h | https://algora.io/ |
| `topcoder-challenges` | platform | 2026-08-18T07:38:11Z | 12h | 1919h | https://www.topcoder.com/challenges |
| `upwork-software-development` | platform | 2026-08-18T07:38:11Z | 12h | 1919h | https://www.upwork.com/freelance-jobs/software-development/ |
| `freelancer-software-development` | platform | 2026-08-18T07:38:11Z | 12h | 1919h | https://www.freelancer.com/jobs/software-development/ |
| `intigriti-public-programs` | platform | 2026-08-18T07:38:11Z | 12h | 1919h | https://www.intigriti.com/researchers/bug-bounty-programs |
| `bugcrowd-engagements` | platform | 2026-08-18T07:38:11Z | 12h | 1919h | https://bugcrowd.com/engagements |

Use `python scripts/source_registry.py list --due` for the authoritative live queue. Open each official page, capture an actual dated observation, then record it with the source-history tool before changing canonical freshness timestamps. Do not promote discovery listings as authorized testing scope.

## 2026-11-06 official directory access probe (21:36 UTC)

- Registered source: `hackerone-directory`, official URL `https://hackerone.com/directory/programs`.
- A direct read of the official page returned only: “It looks like your JavaScript is disabled. To use HackerOne, enable JavaScript in your browser and refresh this page.” The address resolves, but this response exposes **no program list, authorization/scope, payouts or current eligibility**.
- Classification: **JS-required / unverified content**, not a completed program check. Do **not** advance `last_checked_at`, publish live bounty claims, or infer an authorized testing target. A browser with JavaScript enabled or an official documented API is required before any registry verification.
- Provenance: direct official-page retrieval on 2026-11-06; observation applies only to the returned access message, not to current program availability.
