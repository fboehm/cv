

# concatenate bib files
bash concatenate-bib-files.bash Exported\ Items.bib google-scholar-supplemental.bib software.bib kidney.bib hutten2025.bib
# output file is boehm.bib

# convert to yaml

bash convert_bib_to_yaml.bash boehm.bib boehm.yaml

# delete unwanted lines

grep -vE '^(---|nocite)' boehm.yaml > boehm2.yaml
sed 's/{\.nocase}//g; s/\[//g; s/\]//g' boehm2.yaml > boehm-fixed.yaml
