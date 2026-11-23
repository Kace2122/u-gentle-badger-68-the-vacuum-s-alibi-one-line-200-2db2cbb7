"""The Vacuum's Alibi: write one funny line to /output/entry.txt.

The line is a single noir-detective alibi, at most 200 characters: the
vacuum places itself at the dock at 14:02, charging, with forty-one
witnesses in the cloud -- and the crumb was already dead when it arrived.
"""

import os

LINE = "My lidar places me at the dock at 14:02, charging, with forty-one witnesses in the cloud. The crumb was dead before I arrived, detective."

OUTPUT_PATH = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def main():
    # Gate: UTF-8 text of 1 to 200 characters, not only white space,
    # written as exactly one line with no trailing newline.
    assert 1 <= len(LINE) <= 200
    assert LINE.strip() == LINE and "\n" not in LINE
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read it back: the artifact on disk must be exactly the line,
    # byte for byte, so a truncated or re-encoded write fails loudly.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        assert f.read() == LINE


if __name__ == "__main__":
    main()
