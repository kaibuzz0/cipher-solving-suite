# Opportunity Status Evidence Workflow

This workflow defines how agents preserve lifecycle, submission-phase, and deadline evidence before the repository evaluates whether an opportunity is actionable.

## Purpose

`tools/opportunity_actionability.py` can evaluate structured status fields deterministically, but it must not invent where those fields came from. `tools/opportunity_evidence.py` is the bridge between reviewed source material and evaluator-ready records.

The evidence normalizer is deliberately local and non-networked. It does not scrape pages, mark sources fresh, mutate `data/opportunities.json`, or treat HTTP reachability as factual freshness.

## Evidence bundle

Each input item requires a stable `id` and a non-empty `evidence` list. Every evidence statement records:

- `field`: one of `lifecycle_status`, `submission_status`, or `submission_deadline`;
- `value`: the exact normalized fact the agent intends to evaluate;
- `source_url`: an absolute HTTPS source URL;
- `observed_at`: timezone-aware ISO-8601 time when the source was actually reviewed;
- `excerpt`: a short preserved factual excerpt or faithful source note supporting the value;
- `source_name`: optional human-readable source identity.

For `submission_deadline`, the value must itself be a timezone-aware ISO-8601 timestamp. If a source publishes only a local date/time, preserve the source wording separately and resolve the timezone before normalizing the value.

## Deterministic selection policy

Multiple evidence statements for the same field are preserved. The normalizer selects the statement with the newest `observed_at` timestamp for evaluator input.

If two newest statements for the same field have the same observation time but conflicting values, normalization fails. Agents must resolve the disagreement rather than silently selecting one source.

Every normalized evidence statement receives a SHA-256 digest over its canonical structured content. The output also records the SHA-256 digest of the complete source bundle and maps each selected field to the digest of the evidence statement that supplied it.

## Commands

```bash
python tools/opportunity_evidence.py \
  --input tests/fixtures/opportunity_status_evidence.json \
  --output workspace/opportunity-status-normalized.json

python tools/opportunity_actionability.py \
  --input workspace/opportunity-status-normalized.json \
  --as-of 2026-08-19T12:00:00Z \
  --output workspace/opportunity-actionability.json
```

Generated reports belong in `workspace/` or another managed artifact location, not repository root.

## Official-source acquisition adapters

Source-specific adapters may emit this evidence-bundle format, but they must preserve the source wording, actual observation time, and non-destructive failure behavior rather than writing canonical opportunity state directly.

The NIH challenge adapter is the first bounded implementation:

```bash
python tools/nih_challenge_evidence.py \
  --title "NCI Office of Data Sharing Impact Prize" \
  --id nci-ods-impact-prize \
  --observed-at 2026-08-20T20:00:00Z \
  --output workspace/nih-challenge-evidence.json

python tools/opportunity_evidence.py \
  --input workspace/nih-challenge-evidence.json \
  --output workspace/nih-challenge-normalized.json
```

`nih_challenge_evidence.py` reads the official `https://www.nih.gov/challenges` index by default. Tests use `--input-html` with a deterministic local fixture so CI does not depend on network reachability or a mutable external page. The adapter emits lifecycle and submission-state evidence from the exact status phrase it finds. It emits `submission_deadline` only when the NIH source provides an explicit clock time and timezone; a date-only phrase such as `Open 08/03/2026 to 10/05/2026` is preserved as supporting evidence but is not converted into an invented end-of-day timestamp.

A fetch failure, changed page shape, missing exact title, or invalid observation timestamp returns a non-zero exit and does not write the requested output file. The adapter does not mark the NIH source fresh, modify `data/opportunities.json`, or prove eligibility, prize entitlement, or security-testing authorization.

## Refresh procedure

1. Review the current official or otherwise approved source.
2. Preserve a new evidence statement with the actual review time and source URL; do not overwrite older evidence merely because a newer statement exists.
3. Run `opportunity_evidence.py` and resolve any newest-evidence conflicts.
4. Feed the normalized output to `opportunity_actionability.py` with an explicit timezone-aware `--as-of` value.
5. Only update canonical opportunity/intelligence records when the reviewed evidence justifies that change under the repository's normal source and review rules.
6. Preserve primary evidence and hashes when a case or audit trail requires stronger proof than a short excerpt/source note.

## Boundary

This workflow proves only that structured status values were preserved and normalized reproducibly. It does not prove that a public security listing authorizes testing, that a bounty is payable, or that a source remains current after `observed_at`.
