
# convert bib file to json for use with citeproc python module

bigbib=$1
outfile=boehm.json
# https://pandoc.org/demos.html number 38!
pandoc ${bigbib} -t csljson -o ${outfile}

