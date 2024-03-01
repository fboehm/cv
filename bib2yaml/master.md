# master.md

1. export my papers, etc from zotero to bibtex
2. convert bibtex file to yaml file with `convert_bib_to_yaml.bash`
3. use resulting yaml in cv qmd file; perhaps add a sym link to yaml file in the "data" subdir for cv.


```{bash}
bash convert_bib_to_yaml.bash boehm.bib 2024-02-29-boehm.yaml
```

4. manually remove first two lines and last line (ie, the `---` lines) from the yaml file
5. manually add type: other for other articles -- derose 2014, boehm 1997
6. manually fix 'type' values for software packages
7. manually add phd thesis



