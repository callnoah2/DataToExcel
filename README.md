# Data to Excel Importer

## Overview

This Python script allows users to import data from CSV or space-separated files into an Excel spreadsheet. It provides flexibility for specifying the number of columns and output file title.

## Usage

```bash
python3 import_to_excel.py [OPTIONS] FILE

## Options

-c, --columns: Specify the number of columns in the input file.
-o, --output: Specify the output title for the Excel file.
-f, --force: Force overwrite an existing file without prompting.

## Example Usage

python3 import_to_excel.py path/to/input_file.txt -c 6 -o Data_Date-Collected -f

## Requierd Modules

pandas: Data manipulation library.
openpyxl: Library for reading and writing Excel files.

## Notes:

The script reads both CSV and space-separated files.
If the output file already exists, the script prompts the user for confirmation before overwriting (unless -f is used).
If the number of columns is specified, it validates against the actual number of columns in the input file.