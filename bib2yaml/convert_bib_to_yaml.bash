

#https://kevcaz.insileco.io/notes/biblio/bib2yaml_pandoc/
# i may need to manually make the boehm-detail bibtex file, with outputs from 
# zotero and google scholar
bigbib=$1
outfile=boehm.yaml
pandoc ${bigbib} -s -f biblatex -t markdown > ${outfile}


