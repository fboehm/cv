# README.md

if working in RStudio, be sure to compile by using Makefile, rather than by using button to compile PDF.

## quarto cv

https://github.com/mps9506/quarto-cv offers the `quarto-cv.pdf` format for quarto output.


## bolding my name in output pdf

https://tex.stackexchange.com/questions/33330/make-one-authors-name-bold-every-time-it-shows-up-in-the-bibliography

https://stackoverflow.com/questions/56873622/highlight-one-specific-author-when-generating-references-in-pandoc

## Aligning part of a line to the right margin

In some lines, I want to start at the left margin, then have a variable length space, then have, for example, the date, at the right hand side. Can i do this for both html and pdf outputs?

https://stackoverflow.com/questions/48374906/how-do-we-right-align-part-of-a-line-in-r-markdown


What is a nonbreaking space?

https://github.com/jgm/pandoc/issues/6154  

https://github.com/jgm/pandoc/commit/5d88396dd45bf8668d2066693a6891aa275c16f3

A backslash-escaped space is parsed as a nonbreaking space. In TeX output,
it will appear as `~`. In HTML and XML output, it will appear as a
literal unicode nonbreaking space character (note that it will thus
actually look "invisible" in the generated HTML source; you can still
use the `--ascii` command-line option to make it appear as an explicit
entity).


## To do with my CV

- [ ] add a link to my CV on my website
- [ ] add a link to my CV on my github
- [ ] Fix the appearance of "submitted manuscripts" text in pdf (right now, the words "Presented at the " appear in the citation. I believe that they are hard coded from the template) - actually, need to fix bib file for unpublished!
- [ ] Proofread carefully before sharing the new one
- [ ] bold my name in listed pubs
- [ ] update bib file (and partitioned bib files) to include dois, hyperlinks, etc
    - [ ] maybe export my zotero library to a bib file, then use that as the master bib file
- [ ] add horizontal rules to separate sections

- [ ] fix bib files

