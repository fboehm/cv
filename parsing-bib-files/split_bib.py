import configargparse
from pybtex.database import BibliographyData
from pybtex.database.input import bibtex
from pybtex.database.output import bibtex as bib_out

def get_entry_types(entries):
    return set(entry.type for entry in entries.values())

def filter_entries(entries, entry_type):
    return {key: entry for key, entry in entries.items() if entry.type == entry_type}

def save_to_file(entries, filename):
    with open(filename, 'w', encoding='utf-8') as bibfile:
        bib_data = BibliographyData(entries=entries)
        writer = bib_out.Writer()
        writer.write_stream(bib_data, bibfile)

def main(args):
    with open(args.input_file, 'r', encoding='utf-8') as bibfile:
        parser = bibtex.Parser()
        bib_data = parser.parse_file(bibfile)

        entry_types = get_entry_types(bib_data.entries)

        for entry_type in entry_types:
            filtered_entries = filter_entries(bib_data.entries, entry_type)
            output_filename = f'{entry_type}.bib'
            save_to_file(filtered_entries, output_filename)
            print(f'{output_filename} created successfully.')

if __name__ == "__main__":
    parser = configargparse.ArgParser(description='Split BibTeX file based on entry types.')
    parser.add_argument('input_file', help='Path to the original BibTeX file', metavar='FILE')

    args = parser.parse_args()

    main(args)
