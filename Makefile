all: cv-boehm.pdf

cv-boehm.pdf: cv-boehm.tex cv-awards.tex boehm.sty cv-contact.tex cv-education.tex cv-employment.tex cv-mentoring.tex cv-personal.tex cv-presentations.tex cv-pubs.tex cv-research-experience.tex cv-service.tex cv-teaching.tex
		pdflatex cv-boehm; biber cv-boehm; pdflatex cv-boehm; pdflatex cv-boehm

cv-boehm.tex: cv-boehm.Rnw
		R CMD Sweave cv-boehm.Rnw