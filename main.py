#!/usr/bin/env python3
"""Entry for make.fun news-image-20261118 (Python 3.13, standard library only).

Writes the front-page image that sums up the world's news of Wednesday
18 November 2026 to /output/entry.png. The image is shipped in this
repository (entry.png, drawn by the build script) and copied here, so both
runs write identical bytes.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", OUT / "entry.png")


if __name__ == "__main__":
    main()
