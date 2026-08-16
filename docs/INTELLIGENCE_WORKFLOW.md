# News / Intelligence Workflow

The intelligence layer is a user-facing stream of sourced discoveries backed by a managed collection network for human and AI agents.

## Mission

Turn external discoveries into concise, timestamped, source-backed intelligence that users can browse on the GitHub Pages dashboard and agents can reuse without repeating research.

## Canonical data

- Published feed: `data/intelligence.json`
- Source registry: `data/intelligence_sources.json`
- Source check history: `data/source_check_history.json`
- Feed manager: `scripts/intelligence_feed.py`
- Source manager: `scripts/source_registry.py`
- Check-history/change detector: `scripts/source_check_history.py`
- Scheduled report: `.github/workflows/intelligence-report.yml`
- Public rendering: GitHub Pages `News / Intel` and `Intel Sources` tabs

Do not create competing news, source, or check-history databases. Raw research notes/snapshots may live under `intelligence/feeds/`, but publishable intelligence and recurring collection policy belong in these canonical files.

## Source registry model

Every recurring source has:

- stable source ID,
- display name and HTTPS URL,
- source type (`official`, `platform`, `aggregator`, `research-index`, `feed`, `other`),
- source tier (`primary`, `discovery`, `secondary`),
- categories it covers,
- freshness SLA in hours,
- last checked timestamp,
- assigned agent/role,
- enabled state,
- default publishing confidence,
- notes describing verification expectations.

The dashboard derives `fresh`, `due-soon`, `due`, `never-checked`, or `disabled` from the registry. Freshness means the source has been checked recently; it does **not** mean every fact on that source has been independently verified.

## Collection cycle

1. Agent starts with `python scripts/source_registry.py list --due --agent <agent-name>`.
2. Open the assigned source and inspect material changes/new opportunities.
3. Create a stable textual representation of the observed source state and record the check with `scripts/source_check_history.py record`.
4. The history layer labels the source `first-seen`, `unchanged`, or `changed` and preserves the previous fingerprint.
5. If changed, verify the relevant claim, event date, rules, or source context.
6. Check the canonical feed for an existing matching item.
7. Publish useful new intelligence with the canonical source ID.
8. Validate source registry, source history, and intelligence feed.
9. Marking a recorded check updates the registry check timestamp; do not record fake checks merely to clear a due state.
10. If an item becomes actionable work, create/link a structured case.
11. Record meaningful findings/next action in the agent handoff.

The scheduled Intelligence Source Report only reports freshness and recorded content-change state. It does **not** scrape sources or auto-publish findings.

## Source commands

Show stale/never-checked sources:

```bash
python scripts/source_registry.py list --due
```

Show due sources assigned to one agent role:

```bash
python scripts/source_registry.py list --due --agent ctf-scout
```

Validate the source registry:

```bash
python scripts/source_registry.py validate
```

## Check history and change detection

Record the state you actually observed after reviewing a source:

```bash
python scripts/source_check_history.py record ctftime-upcoming \
  --observed "stable summary/list/digest of the current event state" \
  --note "Reviewed upcoming events and organizer links"
```

The tool stores a SHA-256 fingerprint and compares it to the last check for that source. Outcomes are:

- `first-seen` — no earlier recorded state,
- `unchanged` — same normalized observed state,
- `changed` — observed state differs from the previous fingerprint.

Validate history and generate the collection report:

```bash
python scripts/source_check_history.py validate
python scripts/source_check_history.py report
```

The report is written to `artifacts/intelligence-source-report.json` and summarizes total sources, sources due, sources whose most recent recorded check changed, and history-entry count.

## Required intelligence fields

Every published item must include a unique ID, deterministic fingerprint, title, concise summary, category, source name, HTTPS source URL, original publication/event time, agent checked time, confidence (`low`, `medium`, `high`), and relevance (`watch`, `useful`, `high`, `urgent`). When the source exists in the registry, set `source_id` to its canonical ID. Optional fields include agent notes, tags, and a related structured case.

## Publishing rule

An agent should not copy rumors or inferred payout/status claims into the feed as facts. If a claim is uncertain, say so in the summary/notes and use an appropriate confidence level. Prefer official sources. Discovery/aggregator sources should normally lead to a primary organizer/program source before detailed eligibility, prize, or scope claims are promoted as verified facts.

Security-related intelligence does not authorize testing. A bounty/program item may point users to an opportunity, but target scope still must be verified against official program rules before security testing.

## Feed commands

```bash
python scripts/intelligence_feed.py validate
python scripts/intelligence_feed.py list
python scripts/intelligence_feed.py list --category hackathon
```

Add a sourced item with `python scripts/intelligence_feed.py add ...` and include the canonical `--source-id` whenever available.

## Deduplication

Published items get a SHA-256-derived fingerprint based on normalized title and source URL. URL query strings/fragments are ignored so tracking parameters do not create fake-new items. CI rejects duplicate fingerprints and fingerprints that no longer match an item's title/source URL.

Source-check history uses a separate full SHA-256 digest of the stable observed source state. That fingerprint is for change detection, not publication identity.

## User-facing standard

The system should answer: what changed, when it changed, where the information came from, which agent/source lane owns it, whether the source is fresh or due, whether the most recent recorded state changed, how relevant/confident the intelligence is, and whether there is a case or next action connected to it.

The dashboard is a presentation layer; the JSON feed, source registry, and source check history remain the auditable source of truth.
