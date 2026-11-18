#!/usr/bin/env python3
"""news-image-20261117: write the entry image to the output directory.

The entry image is entry.png, a news poster summing up the world news of
Tuesday 17 November 2026. The grader runs this program twice with no
network and both runs must write identical bytes, so the program is a
plain copy of the fixed file held in this repository.
"""

import os
import shutil
from pathlib import Path

REPO_DIR = Path(__file__).resolve().parent
IMAGE = REPO_DIR / "entry.png"


def output_dir():
    """The grader writes to /output; locally MAKEFUN_OUTPUT_DIR overrides it."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    if not IMAGE.is_file():
        raise SystemExit("entry image not found: %s" % IMAGE)
    dest_dir = output_dir()
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / "entry.png"
    shutil.copyfile(IMAGE, dest)
    # The grader requires identical bytes on every run: confirm the copy
    # landed whole before reporting success.
    if dest.stat().st_size != IMAGE.stat().st_size:
        raise SystemExit("entry image copy incomplete: %s" % dest)


if __name__ == "__main__":
    main()
