"""The One-Line Exit - entry generator.

Writes a single funny one-line resignation letter to entry.txt in the
output directory. The letter comes from an IT/operations voice: after
nine years of keeping the place running, the only maintenance window
the writer still believes in is their own.
"""

import os

ENTRY_TEXT = (
    "After nine years keeping this place running, I've realized the only "
    "maintenance window I believe in is my own \u2014 effective immediately."
)


MAX_CHARS = 140


def render_entry() -> str:
    """Return the entry text, validated against the competition gate.

    The sealed scorer accepts UTF-8 text of 1..MAX_CHARS characters
    (excluding the trailing newline) that is not only whitespace.
    Fail loudly here rather than emit an invalid entry.
    """
    text = ENTRY_TEXT.strip()
    if not text:
        raise ValueError("entry text must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry text is {len(text)} characters; cap is {MAX_CHARS}"
        )
    # Round-trip through UTF-8 to prove the text encodes cleanly.
    text.encode("utf-8").decode("utf-8")
    return text


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # newline="\n" pins exactly one trailing LF on every platform.
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(render_entry() + "\n")


if __name__ == "__main__":
    main()
