# News / Intelligence Workflow

The intelligence feed is the user-facing stream of sourced discoveries produced by human and AI agents.

## Mission

Turn external discoveries into concise, timestamped, source-backed intelligence that users can browse on the GitHub Pages dashboard and agents can reuse without repeating research.

## Canonical data

- Feed: `data/intelligence.json`
- Manager: `scripts/intelligence_feed.py`
- Public rendering: GitHub Pages `News / Intel` tab

Do not create competing news databases. Raw research notes may live elsewhere, but publishable intelligence belongs in the canonical feed.

## Required fields

Every published item must include:

- unique ID,
- title,
- concise summary,
- category,
- source name,
- HTTPS source URL,
- original publication/event time,
- time the agent checked it,
- confidence (`low`, `medium`, `high`),
- relevance (`watch`, `useful`, `high`, `urgent`).

Optional fields include agent notes, tags, and a related structured case.

## Categories

`puzzle`, `ctf`, `bug-bounty`, `hackathon`, `crypto`, `github`, `research`, `opportunity`, `tool`, `other`.

## Publishing rule

An agent should not copy rumors or inferred payout/status claims into the feed as facts. If a claim is uncertain, say so in the summary/notes and use an appropriate confidence level. Prefer official sources; if an official source is unavailable, preserve the best primary/credible source and label uncertainty.

Security-related intelligence does not authorize testing. A bounty/program item may point users to an opportunity, but target scope still must be verified against official program rules before security testing.

## Commands

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
  --source-name "Official organizer" \
  --source-url "https://example.com/announcement" \
  --published-at "2026-08-16T12:00:00Z" \
  --confidence high \
  --relevance high \
  --tags ai coding prizes
```

## Agent workflow

1. Discover an item from an external source.
2. Verify publication date, source, and material claim.
3. Check `data/intelligence.json` for duplicates.
4. Add the item using `scripts/intelligence_feed.py` or make an equivalent schema-valid edit.
5. Run `python scripts/intelligence_feed.py validate`.
6. If the discovery becomes actionable work, create/link a structured case.
7. Leave a handoff entry when the publication was part of a larger agent task.

## User-facing standard

The feed should answer:

- What changed?
- When did it happen?
- Where did this information come from?
- How relevant is it to this repo/user?
- How confident are we?
- Is there a case or next action connected to it?

The dashboard is a presentation layer; the JSON feed remains the auditable source of truth.
