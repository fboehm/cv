

#https://kevcaz.insileco.io/notes/biblio/bib2yaml_pandoc/

bigbib=boehm-detail.bib
outfile=boehm.yaml
pandoc ${bigbib} -s -f biblatex -t markdown > ${outfile}
