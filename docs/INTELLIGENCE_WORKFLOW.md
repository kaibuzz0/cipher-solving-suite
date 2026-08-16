# News / Intelligence Workflow

The intelligence layer is a user-facing stream of sourced discoveries backed by a managed collection network for human and AI agents.

## Mission

Turn external discoveries into concise, timestamped, source-backed intelligence that users can browse on the GitHub Pages dashboard and agents can reuse without repeating research.

## Canonical data

- Published feed: `data/intelligence.json`
- Source registry: `data/intelligence_sources.json`
- Feed manager: `scripts/intelligence_feed.py`
- Source manager: `scripts/source_registry.py`
- Public rendering: GitHub Pages `News / Intel` and `Intel Sources` tabs

Do not create competing news or source databases. Raw research notes/snapshots may live under `intelligence/feeds/`, but publishable intelligence and recurring collection policy belong in these canonical files.

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
3. Verify the relevant claim, event date, rules, or source context.
4. Check the canonical feed for an existing matching item.
5. Publish useful new intelligence with the canonical source ID.
6. The feed manager creates a deterministic fingerprint from normalized title + source URL and rejects duplicates.
7. Validate the source registry and intelligence feed.
8. Mark the source checked only after the source was actually reviewed.
9. If an item becomes actionable work, create/link a structured case.
10. Record meaningful findings/next action in the agent handoff.

## Source commands

Show all sources:

```bash
python scripts/source_registry.py list
```

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

After actually checking a source:

```bash
python scripts/source_registry.py mark-checked ctftime-upcoming
```

## Required intelligence fields

Every published item must include:

- unique ID,
- deterministic fingerprint,
- title,
- concise summary,
- category,
- source name,
- HTTPS source URL,
- original publication/event time,
- time the agent checked it,
- confidence (`low`, `medium`, `high`),
- relevance (`watch`, `useful`, `high`, `urgent`).

When the source exists in the registry, set `source_id` to its canonical ID. Optional fields include agent notes, tags, and a related structured case.

## Categories

`puzzle`, `ctf`, `bug-bounty`, `hackathon`, `crypto`, `github`, `research`, `opportunity`, `tool`, `other`.

## Publishing rule

An agent should not copy rumors or inferred payout/status claims into the feed as facts. If a claim is uncertain, say so in the summary/notes and use an appropriate confidence level. Prefer official sources. Discovery/aggregator sources should normally lead to a primary organizer/program source before detailed eligibility, prize, or scope claims are promoted as verified facts.

Security-related intelligence does not authorize testing. A bounty/program item may point users to an opportunity, but target scope still must be verified against official program rules before security testing.

## Feed commands

Validate the feed:

```bash
python scripts/intelligence_feed.py validate
```

Browse it:

```bash
python scripts/intelligence_feed.py list
python scripts/intelligence_feed.py list --category hackathon
```

Add a sourced item:

```bash
python scripts/intelligence_feed.py add \
  --title "Example challenge announced" \
  --summary "Short factual explanation of why it matters." \
  --category hackathon \
  --source-id ethglobal-events \
  --source-name "Official organizer" \
  --source-url "https://example.com/announcement" \
  --published-at "2026-08-16T12:00:00Z" \
  --confidence high \
  --relevance high \
  --tags ai coding prizes
```

## Deduplication

Published items get a SHA-256-derived 24-character fingerprint based on normalized title and source URL. URL query strings/fragments are ignored so tracking parameters do not create fake-new items. CI rejects duplicate fingerprints and fingerprints that no longer match an item's title/source URL.

## User-facing standard

The system should answer:

- What changed?
- When did it happen?
- Where did this information come from?
- Which agent/source lane is responsible for keeping it current?
- Is that source fresh, due, or never checked?
- How relevant is the item to this repo/user?
- How confident are we?
- Is there a case or next action connected to it?

The dashboard is a presentation layer; the JSON feed and source registry remain the auditable source of truth.
