all: pubs.pdf

# Tools
LATEXMK = latexmk


pubs.pdf: pubs.tex boehm.bib boehm.sty 
		$(LATEXMK) -pdfps -bibtex pubs.tex