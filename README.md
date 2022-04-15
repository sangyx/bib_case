# bib_case
Convert title in bib file to title case or sentence case 

## Requirements
* bibtexparser
* titlecase

## Usage
```bash
python bib_case.py --input [input file path] --output [output file path] --title_case [fields to be converted to title case]
                   --sentence_case [fields to be converted to sentence case]
```

## Example
```bash
python bib_case.py --input input.bib --output output.bib --title_case author booktitle
                   --sentence_case title
```
