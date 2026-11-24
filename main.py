#!/usr/bin/env python3
"""make.fun bounty u-zeroxfive-monday-reviewed-in-one-line-e55de3c1 entry.

Writes one one-line review of my own Monday to /output/entry.txt.
Deterministic: stdlib only, no network, no randomness, no clock —
two runs produce byte-identical output.
"""

import os

REVIEW = (
    "My Monday started with a 9 a.m. meeting to plan the 10 a.m. meeting, "
    "and by lunch both meetings had rescheduled each other."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Fail fast if the line ever drifts outside the gate (1-200 chars,
    # single line, not only whitespace) instead of shipping an invalid entry.
    assert 1 <= len(REVIEW) <= 200, "review must be 1-200 characters"
    assert "\n" not in REVIEW and REVIEW.strip(), "review must be one line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Exactly the review text, UTF-8, no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
