from pybtex.database.input import bibtex
from pybtex.database.output import bibtex as bib_out
from pybtex.database import BibliographyData


def filter_entries(entries, entry_type):
    return {key: entry for key, entry in entries.items() if entry.type == entry_type}

def save_to_file(entries, filename):
    with open(filename, 'w', encoding='utf-8') as bibfile:
        bib_data = BibliographyData(entries=entries)
        writer = bib_out.Writer()
        writer.write_stream(bib_data, bibfile)

def main():
    with open('../boehm.bib', 'r', encoding='utf-8') as bibfile:
        parser = bibtex.Parser()
        bib_data = parser.parse_file(bibfile)

        for entry_type in ['article', 'book', 'incollection', 'software', 'inproceedings', 'misc', 'unpublished']:
            filtered_entries = filter_entries(bib_data.entries, entry_type)
            output_filename = f'boehm-{entry_type}.bib'
            save_to_file(filtered_entries, output_filename)
            print(f'{output_filename} created successfully.')

if __name__ == "__main__":
    main()
