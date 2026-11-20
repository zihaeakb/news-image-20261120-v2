#!/usr/bin/env python3
"""Entry program: copy the repository's entry.png to /output/entry.png.

Standard library only. Outside the grader, MAKEFUN_OUTPUT_DIR stands in
for /output. Deterministic: byte-identical output on every run.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(OUT, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"), os.path.join(OUT, "entry.png"))
