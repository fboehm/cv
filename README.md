# README.md


## January 20

- [ ] Consider adding a link to google scholar  
- [ ] Link to Publons?  
- [ ] link to mybibliography ncbi??

- [ ] Fix spacing before & after sections & subsections, etc
- [ ] Fix my bolding in bib entries where I'm first author

- [ ] Fix spacing in "Teaching Experience" section - I leave too much space between two consecutive courses, for example
- [ ] Fix date formatting in Mentoring Experience section. Need something like May 2015 to May 2016

- [ ] Add hyperlinks? to training in teaching section???

- [ ] Can I add hyperlinks to verify accomplishments or show materials? Maybe awards?

- [ ] look through github repositories & figshare, zenodo, etc, to find materials and info for recent presentatiosn
    - [ ] need to add useR! 2016 presentation and slides



- [ ] Consider moving location to new line (ie, for presentations, etc)
- [ ] consider italicizing or doing something to break up monotony of entries in some sections, like Community Service. Maybe italicize date???

- [ ] maybe organize better the peer reviewer item in Professional Service
    - [ ] maybe one journal per line??? Fix G3 name

- [ ] Maybe use one font size throughout all regular text??

Right now, for example, education section differs in size from Written Works

- [ ] USA or United States of America






## January 17, 2024


- [ ] fix issue with authors for the Costello, et al. Nature biotech piece

- [ ] fix formatting for different types of publications
    - [ ] fix text size in pdf output ("\\footnotesize")
- [ ] check keys for every type value
- [ ] maybe fix date issue: I arbitrarily add info to get a date from the yaml entry "issued". Maybe I actually want to make a new key, like "issued_formatted_for_sorting". then, when I go to print the item, I can use the original "issued" value!


## Older

- [ ] continue working with try-bib.qmd to get the bib yaml processing done as needed.



- [ ] convert bib file to yaml with pandoc?
- [ ] manually curate the bib file produced from zotero export
- [ ] ensure that all dois are used
- [ ] maybe look at csl file to see if I can copy effects of a csl with python & markdown
- [ ] if doi, then hyperlink title



- [ ] Fix qmd cv file to accommodate multiple dates in service yaml file (since one entry has two date values)




## To-do for new cv

- [ ] add a yaml for every section's data
- [ ] check formatting of text in pdf output
    - [ ] fix dates with python date package
- [ ] hide / echo: false for all code chunks
- [ ] make note about need for *two* section headers at top to get one to show up in pdf... i'm guessing that this is a quarto-cv extension issue
- [ ] fix / change extension code so that CV is in footer instead of "education adn training"
- [ ] Find way to use the multiple bib files... can I use lua with my current qmd? 
- [ ] revise overall bib file to include dois, hyperlinks, etc
- [ ] modify (perhaps bold) my name in the outputted pdf in the publications sections





## Old stuff

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

