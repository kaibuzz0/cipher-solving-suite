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
