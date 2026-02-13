all: cv-boehm.pdf

# Tools
LATEXMK = latexmk


cv-boehm.pdf: cv-boehm.tex boehm.bib boehm.sty cv-awards.tex boehm.sty cv-contact.tex cv-education.tex cv-employment.tex cv-mentoring.tex cv-personal.tex cv-presentations.tex cv-pubs.tex cv-research-experience.tex cv-service.tex cv-teaching.tex
		$(LATEXMK) -pdfps -bibtex cv-boehm.tex