

# concatenate bib files
bash concatenate-bib-files.bash Exported\ Items.bib google-scholar-supplemental.bib software.bib kidney.bib
# output file is boehm.bib

# convert to yaml

bash convert_bib_to_yaml.bash boehm.bib boehm.yaml

# delete unwanted lines

grep -vE '^(---|nocite)' boehm.yaml > boehm-fixed.yaml
