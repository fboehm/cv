

# concatenate bib files
bash concatenate-bib-files.bash Exported\ Items.bib google-scholar-supplemental.bib software.bib unpublished.bib kidney.bib
# output file is boehm.bib

# convert to yaml

bash convert_bib_to_yaml.bash boehm.bib

# delete unwanted lines

grep -vE '^(---|nocite)' boehm.yaml > boehm-fixed.yaml
