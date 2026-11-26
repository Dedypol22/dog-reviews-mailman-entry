"""The Dog Reviews the Mailman: one funny one-line review.

A dog reviews its mailman after three years of the same visit: same
blue shorts, same bag, same 9 a.m. knock, and never once a treat. The
dog's grievance is filed the only way a dog can file anything — 412
complaints, all barking. The line is a concrete scene (a real routine,
a real number, a real time of day) told flat, in a dog's voice, with
the turn landing on the last two words.

Line: "Three years, same blue shorts, same bag, same 9 a.m. knock. He has never once brought me a treat. I have filed 412 complaints. All barking."

The line is 139 characters, well under the 200-character gate (140
bytes including the trailing newline).
"""

LINE = "Three years, same blue shorts, same bag, same 9 a.m. knock. He has never once brought me a treat. I have filed 412 complaints. All barking."

import os


def output_dir():
    """Return the output directory from MAKEFUN_OUTPUT_DIR or "/output"."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    """Write the review line to entry.txt and print it to stdout."""
    text = LINE + "\n"
    path = os.path.join(output_dir(), "entry.txt")
    os.makedirs(output_dir(), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
