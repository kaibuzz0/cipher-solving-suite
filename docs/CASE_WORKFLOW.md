# Challenge / Opportunity Case Workflow

Use a case directory whenever work becomes more than a simple catalog link. A case can represent a cipher puzzle, Bitcoin puzzle, CTF challenge, hackathon entry, authorized bug-bounty lead, audit target, coding competition, or GitHub research investigation.

## Create a case

```bash
python scripts/new_case.py --name "Puzzle 310 follow-up" --type puzzle --source "example source" --url "https://example.com/challenge"
```

For security-related work, also record the official authorization/scope page:

```bash
python scripts/new_case.py \
  --name "Authorized bounty lead" \
  --type bug-bounty \
  --source "Program name" \
  --url "https://example.com/program" \
  --authorization-url "https://example.com/program/policy"
```

Cases are created under `research/active-puzzles/YYYYMMDD-slug/`.

## Case contents

Each case contains:

- `case.json` — machine-readable metadata/status.
- `README.md` — human summary and checklist.
- `notes.md` — observations, hypotheses, links, agent notes.
- `attempts.md` — commands/tools/parameters/results; append rather than rewrite history.
- `evidence/` — source files, screenshots, hashes, exported challenge material, or other preserved evidence.

## Required lifecycle

1. **Intake** — record source URL, date, type, and authorization if security testing is involved.
2. **Preserve** — save evidence locally when allowed and record hashes/filenames.
3. **Triage** — identify likely techniques/tools and the smallest next experiment.
4. **Attempt** — append exact commands, parameters, outputs, and interpretation to `attempts.md`.
5. **Verify** — reproduce a solve/finding or clearly record why it remains unverified.
6. **Outcome** — set `status` to `solved`, `submitted`, `closed`, `blocked`, or another accurate state.
7. **Archive** — move finished cases to `research/solutions/` or `workspace/archive/` without deleting evidence.
8. **Handoff** — summarize the case in `docs/AGENT_HANDOFF.md` when agent ownership changes.

## Rules for AI agents

- Do not invent a live prize, scope, result, or target status.
- Public availability is not authorization for security testing.
- Prefer official source URLs and timestamp observations.
- Keep failed attempts; they prevent duplicate work.
- Do not store secrets, private keys, credentials, or wallet seeds in case files.
- When importing third-party material, preserve license/source information where relevant.

## Useful status values

`new`, `triage`, `active`, `blocked`, `solved`, `submitted`, `closed`, `archived`.
