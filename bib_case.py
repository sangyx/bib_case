from argparse import ArgumentParser
import bibtexparser
from titlecase import titlecase

def convert_title_case(s):
    return titlecase(s)

def convert_sentence_case(s):
    return s.capitalize()

def parse_title(input_file, output_file, title_case, sentence_case):
    with open(input_file, "r") as bibtex_file:
        bibtex_str = bibtex_file.read()

    bib_database = bibtexparser.loads(bibtex_str)

    for i in range(len(bib_database.entries)):
        for field in title_case:
            if field in bib_database.entries[i]:
                bib_database.entries[i][field] = convert_title_case(bib_database.entries[i][field])
        
        for field in sentence_case:
            if field in bib_database.entries[i]:
                bib_database.entries[i][field] = convert_sentence_case(bib_database.entries[i][field])

    with open(output_file, "w") as bibtex_file:
        bibtexparser.dump(bib_database, bibtex_file)

if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("--input", type=str, help="input file path")
    parser.add_argument("--output", type=str, help="output file path")

    parser.add_argument("--title_case", nargs="+", default=[], help="fields to be converted to title case")
    parser.add_argument("--sentence_case", nargs="+", default=[], help="fields to be converted to sentence case")

    args = parser.parse_args()

    parse_title(args.input, args.output, args.title_case, args.sentence_case)