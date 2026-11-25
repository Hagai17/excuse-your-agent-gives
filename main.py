#!/usr/bin/env python3
"""Entry for make.fun bounty "The Excuse Your Agent Gives You".

Writes the one-line excuse to /output/entry.txt (the harness artifact)
and prints it to stdout. One line, 103 characters.
"""

import os

# The excuse is built from its two beats: the setup (the agent was mid-
# generation, the human mid-doubt) and the turn (doubt read as consent).
SETUP = 'The bug was in the part I generated while you were typing "are you sure?"'
TURN = "I took that as encouragement."
ENTRY = f"{SETUP} {TURN}"


def main() -> None:
    # Gate self-check: the sealed scorer accepts UTF-8 text of 1 to 200
    # characters, not only white space. Fail loudly rather than ship an
    # invalid artifact if the line is ever edited past the cap.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, gate is 1-200"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY

    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
            fh.write(ENTRY)
    except OSError:
        # The artifact directory is provided by the harness; if it is not
        # writable in a local run, stdout still carries the entry.
        pass
    print(ENTRY)


if __name__ == "__main__":
    main()
