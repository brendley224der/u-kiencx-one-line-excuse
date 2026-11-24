"""One-line excuse an AI agent gives its human for missing a deadline.

Writes the single line to /output/entry.txt (created if missing).
Pure Python standard library only; fully deterministic.
"""

import os

LINE = "I finished it on time in a parallel branch \u2014 unfortunately, this is the main branch."


def main() -> None:
    text = LINE.strip()
    # The gate counts the entry text itself: one line, 1-160 characters,
    # not only whitespace. Count the line without its trailing newline,
    # and reject any embedded newline so the file can never hold two lines.
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert 1 <= len(text) <= 160, f"line must be 1-160 chars, got {len(text)}"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")


if __name__ == "__main__":
    main()
