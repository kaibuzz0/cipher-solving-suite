# Cipher Solving Suite v3.1.0

A multi-agent research and operations hub for cipher puzzles, CTFs, hackathons, authorized bug-bounty/audit work, coding challenges, GitHub research, sourced news/intelligence, reusable prompts, notes, and earnings tracking.

**Start here.** This README is the repository front door for humans and AI agents. Use it to navigate the repo, find commands, locate active work, and understand the operating workflow before changing anything.

## Quick navigation

| I want to… | Go here |
|---|---|
| Open the human-facing dashboard | [`site/index.html`](site/index.html) |
| Browse sourced News / Intelligence | [`data/intelligence.json`](data/intelligence.json) |
| Understand how agents publish intelligence | [`docs/INTELLIGENCE_WORKFLOW.md`](docs/INTELLIGENCE_WORKFLOW.md) |
| Add/list/validate intelligence from terminal | [`scripts/intelligence_feed.py`](scripts/intelligence_feed.py) |
| See what an AI agent must read/do | [`AGENTS.md`](AGENTS.md) |
| Find the next task | [`docs/WORK_QUEUE.md`](docs/WORK_QUEUE.md) |
| Read the latest agent notes | [`docs/AGENT_HANDOFF.md`](docs/AGENT_HANDOFF.md) |
| Understand repo maintenance rules | [`docs/REPO_MAINTENANCE.md`](docs/REPO_MAINTENANCE.md) |
| Start a new puzzle/challenge/research case | [`docs/CASE_WORKFLOW.md`](docs/CASE_WORKFLOW.md) |
| Generate a standardized case folder | [`scripts/new_case.py`](scripts/new_case.py) |
| Browse money/skill opportunity links | [`data/opportunities.json`](data/opportunities.json) |
| Browse the internal tool registry | [`data/tools.json`](data/tools.json) |
| Browse reusable AI prompts | [`data/prompts.json`](data/prompts.json) |
| Build user-facing dashboard data | [`scripts/build_site_data.py`](scripts/build_site_data.py) |
| Search opportunities from terminal | [`tools/opportunity_finder.py`](tools/opportunity_finder.py) |
| Track attempts/earnings | [`tools/earnings_tracker.py`](tools/earnings_tracker.py) |
| Create a timestamped opportunity snapshot | [`tools/scanning/opportunity_scanner.py`](tools/scanning/opportunity_scanner.py) |
| Run the main command router | [`suite.py`](suite.py) |
| Run repo hygiene checks | [`scripts/maintenance_check.py`](scripts/maintenance_check.py) |
| Run core tests | [`tests/test_core.py`](tests/test_core.py) |
| Inspect active research | [`research/active-puzzles/`](research/active-puzzles/) |
| Inspect solver modules | [`solvers/`](solvers/) |
| Inspect generated/active work | [`workspace/`](workspace/) |
| Inspect CI | [`.github/workflows/ci.yml`](.github/workflows/ci.yml) |
| Inspect daily maintenance automation | [`.github/workflows/daily-maintenance.yml`](.github/workflows/daily-maintenance.yml) |
| Inspect Pages deployment | [`.github/workflows/pages.yml`](.github/workflows/pages.yml) |

## Two-layer architecture

This repository deliberately serves two audiences at once.

**Agent layer:** structured files, intelligence, case metadata, catalogs, work queues, handoffs, tests, and scripts let many AI/human agents work without losing context or duplicating effort.

**User layer:** the GitHub Pages Operations Hub turns that structured state into a readable dashboard. Users can see opportunities, sourced News / Intelligence, active cases, internal tools, prompts, research links, repository status, and agent workflow without digging through source files.

The website is a first-class output. When agents publish a sourced intelligence item, add a structured case, or update the tool/opportunity/prompt catalogs, the Pages build exposes the shared state to users.

## Agent start sequence

Every AI or human agent should use this order:

1. **README.md** — orient and navigate.
2. **AGENTS.md** — read operating and authorization rules.
3. **docs/AGENT_HANDOFF.md** — learn what the previous agent did.
4. **docs/WORK_QUEUE.md** — choose/claim the smallest useful task.
5. **Open PRs/issues** — avoid duplicated or conflicting work.
6. **Relevant code/data/research files** — inspect before editing.
7. **Publish sourced intelligence** — when external research produces a useful user-facing update, use `data/intelligence.json` and `docs/INTELLIGENCE_WORKFLOW.md`.
8. **Tests / maintenance checks** — verify before handoff.
9. **Publish structured state** — cases/tools/catalog changes should be visible to the user dashboard where appropriate.
10. **Append a handoff entry** — leave exact next steps for the next agent.

## Command center

```bash
# Repository status / command router
python suite.py --status

# Browse/validate sourced News / Intelligence
python scripts/intelligence_feed.py list
python scripts/intelligence_feed.py list --category github
python scripts/intelligence_feed.py validate

# Publish a sourced intelligence item
python scripts/intelligence_feed.py add \
  --title "Example challenge announced" \
  --summary "Short factual explanation of why it matters." \
  --category hackathon \
  --source-name "Official organizer" \
  --source-url "https://example.com/announcement" \
  --published-at "2026-08-16T12:00:00Z" \
  --confidence high \
  --relevance high

# Create a standardized new case
python scripts/new_case.py --name "Puzzle 310 follow-up" --type puzzle --source "source name" --url "https://example.com/challenge"

# Build the same structured summary used by the website
python scripts/build_site_data.py

# Opportunity discovery from the shared catalog
python suite.py --opportunities
python tools/opportunity_finder.py --list
python tools/opportunity_finder.py --search crypto
python tools/opportunity_finder.py --category hackathon

# Earnings / attempt tracking
python tools/earnings_tracker.py stats

# Timestamped catalog snapshot (not a live scrape)
python suite.py --scan

# Health / validation
python suite.py --maintenance
python -m pytest tests/ -vv --tb=short
```

## What works now

- `suite.py` — top-level status and command router.
- `data/intelligence.json` — canonical source-backed user-facing News / Intelligence feed.
- `scripts/intelligence_feed.py` — add/list/validate intelligence with timestamps, source, confidence, relevance, tags, notes, and optional case links.
- `docs/INTELLIGENCE_WORKFLOW.md` — publishing rules for agents researching external developments.
- `data/opportunities.json` — canonical opportunity/link catalog used by CLI and website.
- `data/tools.json` — canonical internal tool registry used by the website and validation.
- `data/prompts.json` — reusable AI prompt library.
- `tools/opportunity_finder.py` — list/search/filter/open catalog entries.
- `tools/earnings_tracker.py` — record attempts and verified earnings.
- `tools/scanning/opportunity_scanner.py` — timestamped catalog snapshots; deliberately **not labeled as live scraping**.
- `scripts/new_case.py` — standardized challenge/opportunity case generator.
- `scripts/build_site_data.py` — scans structured cases and catalogs to create dashboard `cases.json` and `status.json`.
- `docs/CASE_WORKFLOW.md` — case lifecycle, evidence, attempts, verification, and handoff rules.
- `AGENTS.md` — operating contract for AI and human agents.
- `docs/AGENT_HANDOFF.md` — append-only agent journal.
- `docs/WORK_QUEUE.md` — shared claimable work queue.
- `docs/REPO_MAINTENANCE.md` — maintenance rules and definition of done.
- `scripts/maintenance_check.py` — deterministic hygiene/compile checks.
- `tests/test_core.py` — deterministic catalog, intelligence, tool-registry, earnings, and case-generation tests.
- `site/` — static Operations Hub dashboard deployed through GitHub Pages after merge/configuration.

## Repository map

```text
cipher-solving-suite/
├── README.md                    # FRONT DOOR + navigation
├── AGENTS.md                    # agent rules / authorization boundary
├── suite.py                     # top-level command router
├── data/
│   ├── intelligence.json        # canonical sourced News / Intelligence feed
│   ├── opportunities.json       # canonical opportunity/link catalog
│   ├── tools.json               # canonical internal tool registry
│   └── prompts.json             # reusable AI prompts
├── docs/
│   ├── AGENT_HANDOFF.md         # append-only notes between agents
│   ├── CASE_WORKFLOW.md         # standardized challenge/case lifecycle
│   ├── INTELLIGENCE_WORKFLOW.md # sourced news/intelligence publishing rules
│   ├── REPO_MAINTENANCE.md      # maintenance / definition of done
│   └── WORK_QUEUE.md            # shared work claims and priorities
├── site/                        # GitHub Pages Operations Hub
├── site-data/                   # generated dashboard case/status snapshots
├── tools/                       # opportunity, earnings and scanning tools
├── scripts/
│   ├── build_site_data.py       # converts repo state into dashboard data
│   ├── intelligence_feed.py     # manages sourced News / Intelligence
│   ├── maintenance_check.py     # repository hygiene checks
│   └── new_case.py              # creates standardized case directories
├── tests/                       # deterministic validation
├── research/                    # active cases, research and solutions
├── intelligence/               # raw/timestamped supporting feed snapshots
├── solvers/                     # solving modules
├── workspace/                   # active/generated work
└── legacy/                      # older consolidated material
```

## Where new things belong

Do not create another random root-level file when an existing lane fits.

- Sourced user-facing news/research update → `data/intelligence.json`
- Raw timestamped external-feed snapshot → `intelligence/feeds/`
- New opportunity/platform link → `data/opportunities.json`
- New internal tool meant for agents/users → code in its proper module + registry entry in `data/tools.json`
- Reusable AI prompt → `data/prompts.json`
- New puzzle/challenge/bounty/research investigation → create a case with `scripts/new_case.py`
- Active challenge/case research → `research/active-puzzles/<case-id>/`
- Successful/reproducible solution → `research/solutions/`
- Solver code → `solvers/` or the appropriate existing tool module
- Temporary/generated work → `workspace/` or `artifacts/`
- Agent-to-agent notes → `docs/AGENT_HANDOFF.md`
- Future work → `docs/WORK_QUEUE.md`
- Stable process/rules → `docs/`

## News / Intelligence pipeline

The News / Intelligence layer is how external research becomes durable, user-visible knowledge instead of disappearing inside one agent conversation.

Every published item records what changed, source name/URL, source publication time, when an agent checked it, category, confidence, relevance, tags, optional notes, and an optional related case. The dashboard exposes these entries under **News / Intel** and lets users filter them by category.

Agents should prefer official/primary sources. Uncertain claims must be labeled with appropriate confidence rather than presented as verified facts. Intelligence about a bounty or target is **not** testing authorization. See [`docs/INTELLIGENCE_WORKFLOW.md`](docs/INTELLIGENCE_WORKFLOW.md).

## Standard case workflow

When an opportunity becomes real work, convert it into a case rather than scattering notes across the repository. A generated case contains `case.json`, `README.md`, `notes.md`, `attempts.md`, and `evidence/`.

That gives agents one place to preserve source URLs, authorization, evidence, hypotheses, commands, failed attempts, outcomes, ownership, and next actions. The Pages build scans these `case.json` files so active structured work can appear on the user dashboard. See [`docs/CASE_WORKFLOW.md`](docs/CASE_WORKFLOW.md).

## Opportunity pipeline

The catalog is a launchpad, not a promise of payout. It includes categories such as bug bounties, Web3 audit contests, CTFs, cryptography/security training, hackathons, government prize challenges, and GitHub research.

Availability, prizes, eligibility, rules, and scopes change. Verify those facts on the official linked page before investing time or testing a target.

## Security authorization boundary

Security tooling is for authorized CTFs, labs, audits, puzzles, and bug-bounty programs. Before testing a real target, save the official rules/scope and confirm the asset/action is allowed. A public hostname, contract, repository, IP address, or intelligence-feed entry is **not** authorization by itself.

## Static Operations Hub

`site/` is the human-facing dashboard. It exposes:

- repository summary counts,
- opportunities,
- sourced News / Intelligence with dates, confidence, relevance, notes, and source links,
- active structured cases and their next actions,
- the internal tool registry with commands and maturity,
- reusable AI prompts,
- agent workflow/handoffs,
- research launch links.

`.github/workflows/pages.yml` validates the intelligence feed, runs `scripts/build_site_data.py`, packages the shared catalogs plus generated case/status data, and publishes the site through GitHub Pages on `main` changes. The repository Pages setting may need to be set to **GitHub Actions** once.

## Validation and maintenance

Pull requests run Python 3.11, 3.12, and 3.13 validation through [`.github/workflows/ci.yml`](.github/workflows/ci.yml). Matrix jobs are named `Python 3.11`, `Python 3.12`, and `Python 3.13`, and `fail-fast` is disabled so one interpreter failure does not hide results from the others.

Tests run with `python -m pytest -vv --tb=short --junitxml=test-results.xml`. The Actions log therefore shows each individual test and a concise traceback instead of only an opaque exit code. Each Python job uploads its JUnit XML with `if: always()`, so failure diagnostics remain available when a test breaks.

Compile, intelligence-feed validation, dashboard-data generation, and maintenance validation also continue after a test failure. Their outcomes are written to the GitHub job summary; the intelligence feed, generated dashboard data, and maintenance reports are uploaded with `if: always()`. The matrix job fails only after all diagnostic stages have run. The goal is: **CI should answer exactly what failed, where, and on which Python version.**

The daily maintenance workflow checks missing required files, Python compile failures, version drift, generated files at repository root, and suspicious secret-like filenames. Findings become cleanup work; automation does not silently delete research evidence.

## Known cleanup debt

Older generated images/binaries and legacy research still exist at the root. They should be inventoried with hashes and references before relocation so research provenance is preserved. Older research documents may also contain stale payout/platform claims and should be treated as historical notes until revalidated.

## Mission

The repository should help a **user** quickly answer:

- What changed recently that could matter to me?
- Where did that information come from and how confident is it?
- What opportunities are available to investigate?
- What cases are active right now?
- What tools can I use and how do I run them?
- What did the agents learn?
- What research/resources should I open next?

And it should help an **agent** quickly answer:

- What new sourced information should be published for users?
- What legitimate opportunity should we investigate next?
- What tools do we already have?
- What has already been tried?
- What evidence and authorization do we have?
- What did the previous agent learn?
- What is broken or missing?
- What is the next highest-value piece of work?

License: MIT
