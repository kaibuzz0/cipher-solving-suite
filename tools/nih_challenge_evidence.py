#!/usr/bin/env python3
"""Acquire status evidence from the official NIH challenge index.

The adapter reads the NIH challenges HTML from the network or a local fixture,
finds one named challenge card, and emits an ``opportunity_evidence.py`` input
bundle. It preserves the exact source text used for each normalized field and
never mutates canonical opportunity data. Network failures are fatal and leave
any requested output path untouched.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

DEFAULT_URL = "https://www.nih.gov/challenges"
SOURCE_NAME = "NIH Challenges and Prize Competitions"

STATUS_RE = re.compile(
    r"(?:(?P<prefix>phase\s+\d+|milestone\s+\d+|recruitment\s+phase)\s+)?"
    r"(?P<state>open|closed)\s+"
    r"(?P<tail>(?:until\s+|on\s+)?\d{1,2}/\d{1,2}/\d{2,4}[^.!?]{0,100})"
    r"|(?P<coming>coming\s+soon)",
    re.IGNORECASE,
)
EXACT_DEADLINE_RE = re.compile(
    r"(?:until|to)\s+"
    r"(?P<date>\d{1,2}/\d{1,2}/\d{2,4})"
    r"(?:\s+at)?\s+"
    r"(?P<time>\d{1,2}:\d{2})\s*"
    r"(?P<ampm>AM|PM)\s+"
    r"(?P<tz>ET|EST|EDT)\b",
    re.IGNORECASE,
)


class ChallengeParser(HTMLParser):
    """Collect heading-delimited challenge cards as normalized text."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.cards: list[dict[str, str]] = []
        self._current: dict[str, list[str]] | None = None
        self._heading_depth = 0
        self._heading_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"h2", "h3", "h4"}:
            self._heading_depth += 1
            self._heading_parts = []

    def handle_endtag(self, tag: str) -> None:
        if tag in {"h2", "h3", "h4"} and self._heading_depth:
            self._heading_depth -= 1
            title = _clean(" ".join(self._heading_parts))
            if title:
                if self._current:
                    self._finish_current()
                self._current = {"title": [title], "text": []}
            self._heading_parts = []

    def handle_data(self, data: str) -> None:
        text = _clean(data)
        if not text:
            return
        if self._heading_depth:
            self._heading_parts.append(text)
        elif self._current is not None:
            self._current["text"].append(text)

    def close(self) -> None:
        super().close()
        if self._current:
            self._finish_current()

    def _finish_current(self) -> None:
        assert self._current is not None
        title = _clean(" ".join(self._current["title"]))
        text = _clean(" ".join(self._current["text"]))
        self.cards.append({"title": title, "text": text})
        self._current = None


def _clean(value: str) -> str:
    return " ".join(str(value).split())


def parse_observed_at(value: str) -> str:
    text = value.strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    dt = datetime.fromisoformat(text)
    if dt.tzinfo is None:
        raise ValueError("--observed-at must include timezone information")
    return dt.isoformat()


def fetch_html(url: str, timeout: float) -> str:
    request = Request(
        url,
        headers={"User-Agent": "cipher-solving-suite/3.1 opportunity-evidence-adapter"},
    )
    with urlopen(request, timeout=timeout) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def read_html(input_html: str | None, url: str, timeout: float) -> str:
    if input_html:
        return Path(input_html).read_text(encoding="utf-8")
    return fetch_html(url, timeout)


def find_card(html: str, title: str) -> dict[str, str]:
    parser = ChallengeParser()
    parser.feed(html)
    parser.close()
    wanted = _clean(title).casefold()
    exact = [card for card in parser.cards if card["title"].casefold() == wanted]
    if len(exact) != 1:
        raise ValueError(
            f"expected exactly one NIH challenge card titled {title!r}; found {len(exact)}"
        )
    return exact[0]


def extract_evidence(
    card: dict[str, str], source_url: str, observed_at: str
) -> list[dict[str, str]]:
    text = card["text"]
    match = STATUS_RE.search(text)
    if not match:
        raise ValueError(f"no supported status phrase found for {card['title']!r}")

    state = "coming_soon" if match.group("coming") else match.group("state").lower()
    status_excerpt = _clean(match.group(0))
    evidence: list[dict[str, str]] = []

    if state == "open":
        lifecycle = "active"
        submission = "open"
    elif state == "closed":
        lifecycle = "closed"
        submission = "closed"
    else:
        lifecycle = "upcoming"
        submission = "upcoming"

    for field, value in (
        ("lifecycle_status", lifecycle),
        ("submission_status", submission),
    ):
        evidence.append(
            {
                "field": field,
                "value": value,
                "source_url": source_url,
                "source_name": SOURCE_NAME,
                "observed_at": observed_at,
                "excerpt": status_excerpt,
            }
        )

    deadline = EXACT_DEADLINE_RE.search(status_excerpt)
    if deadline and state == "open":
        raw_date = deadline.group("date")
        year_width = len(raw_date.rsplit("/", 1)[-1])
        date_fmt = "%m/%d/%Y" if year_width == 4 else "%m/%d/%y"
        naive = datetime.strptime(
            f"{raw_date} {deadline.group('time')} {deadline.group('ampm').upper()}",
            f"{date_fmt} %I:%M %p",
        )
        tz_token = deadline.group("tz").upper()
        if tz_token == "EST":
            aware = naive.replace(tzinfo=ZoneInfo("Etc/GMT+5"))
        elif tz_token == "EDT":
            aware = naive.replace(tzinfo=ZoneInfo("Etc/GMT+4"))
        else:
            aware = naive.replace(tzinfo=ZoneInfo("America/New_York"))
        evidence.append(
            {
                "field": "submission_deadline",
                "value": aware.isoformat(),
                "source_url": source_url,
                "source_name": SOURCE_NAME,
                "observed_at": observed_at,
                "excerpt": status_excerpt,
            }
        )

    return evidence


def build_bundle(
    html: str, *, title: str, item_id: str, source_url: str, observed_at: str
) -> dict[str, Any]:
    card = find_card(html, title)
    return {
        "schema_version": 1,
        "adapter": "nih-challenge-evidence",
        "items": [
            {
                "id": item_id,
                "evidence": extract_evidence(card, source_url, observed_at),
            }
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--title", required=True, help="Exact NIH challenge title")
    parser.add_argument("--id", required=True, dest="item_id", help="Stable opportunity ID")
    parser.add_argument("--observed-at", required=True, help="Timezone-aware ISO-8601 review time")
    parser.add_argument("--url", default=DEFAULT_URL, help="Official NIH challenge index URL")
    parser.add_argument("--input-html", help="Local HTML fixture; skips network access")
    parser.add_argument("--output", help="Evidence-bundle JSON output path")
    parser.add_argument("--timeout", type=float, default=15.0, help="Network timeout in seconds")
    args = parser.parse_args(argv)

    try:
        observed_at = parse_observed_at(args.observed_at)
        html = read_html(args.input_html, args.url, args.timeout)
        bundle = build_bundle(
            html,
            title=args.title,
            item_id=args.item_id,
            source_url=args.url,
            observed_at=observed_at,
        )
    except (OSError, HTTPError, URLError, TimeoutError, UnicodeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    payload = json.dumps(bundle, indent=2) + "\n"
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
