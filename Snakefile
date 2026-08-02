# Snakefile -- build the CV (cv.pdf) with Quarto.
#
# The publication list is read *directly* from the BibTeX files
# (boehm.bib, boehm-wip.bib) by scripts/cvbib.py. There is no longer a
# bib -> yaml (pandoc) conversion step; the bib2yaml/ directory is no
# longer part of the build.
#
# Usage:
#   snakemake --cores 1            # build cv.pdf
#   snakemake --cores 1 clean      # remove build artifacts
#   snakemake --cores 1 -n         # dry run (show what would build)

import glob
import os

BIBS = ["boehm.bib", "boehm-wip.bib"]
QMDS = ["cv.qmd", "try-bib.qmd", "teaching.qmd"]
DATA = sorted(glob.glob("data/*.yaml"))
# Files contributed by the quarto-cv extension (template, filters, partials).
EXTENSION = sorted(
    f for f in glob.glob("_extensions/**/*", recursive=True) if os.path.isfile(f)
)


rule all:
    input:
        "cv.pdf",


rule cv:
    """Render cv.qmd -> cv.pdf, reading the .bib files directly."""
    input:
        qmds=QMDS,
        parser="scripts/cvbib.py",
        bibs=BIBS,
        data=DATA,
        extension=EXTENSION,
    output:
        "cv.pdf",
    shell:
        "quarto render cv.qmd --to quarto-cv-pdf"


rule clean:
    """Remove Quarto build artifacts (keeps cv.pdf out of the way)."""
    shell:
        "rm -rf cv.pdf cv.tex cv.pdf.md cv_files .quarto"
