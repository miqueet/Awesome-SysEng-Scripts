#!/usr/bin/env python3

import pandas as pd
import argparse
import os
import sys
import csv

def xlsx_to_csv(xlsx_filename, remove_top_rows, change_delim_from, change_delim_to):
    # Check if the file exists
    if not os.path.exists(xlsx_filename):
        print(f"File '{xlsx_filename}' not found.")
        return

    # Check if the file has an .xlsx extension
    if not xlsx_filename.lower().endswith('.xlsx'):
        print("The file is not an XLSX file.")
        return

    # Read the Excel file
    try:
        df = pd.read_excel(xlsx_filename, skiprows=remove_top_rows)
    except Exception as e:
        print(f"Failed to read the Excel file: {e}")
        return

    # Create a CSV filename by replacing .xlsx with .csv
    csv_filename = os.path.splitext(xlsx_filename)[0] + '.csv'

    # Save the DataFrame to a CSV file
    try:
        df.to_csv(csv_filename, index=False)
        print(f"File '{xlsx_filename}' has been converted to '{csv_filename}'.")
    except Exception as e:
        print(f"Failed to save the CSV file: {e}")
        return

    # Change the delimiter if specified
    if change_delim_from and change_delim_to:
        try:
            with open(csv_filename, 'r', newline='') as csv_file:
                reader = csv.reader(csv_file, delimiter=change_delim_from)
                rows = list(reader)

            with open(csv_filename, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file, delimiter=change_delim_to, quoting=csv.QUOTE_MINIMAL)
                for row in rows:
                    writer.writerow(row)

            print(f"Delimiter in '{csv_filename}' has been changed from '{change_delim_from}' to '{change_delim_to}'.")
        except Exception as e:
            print(f"Failed to change the delimiter: {e}")

def main():
    parser = argparse.ArgumentParser(description='Convert XLSX file to CSV file.')
    parser.add_argument('--file', required=True, help='Path to the XLSX file')
    parser.add_argument('--remove-top-rows', type=int, default=0, help='Number of top rows to remove')
    parser.add_argument('--change-delim-from', help='Delimiter to change from (default: ",")', default=",")
    parser.add_argument('--change-delim-to', help='Delimiter to change to (default: ",")', default=",")

    args = parser.parse_args()

    xlsx_to_csv(args.file, args.remove_top_rows, args.change_delim_from, args.change_delim_to)

if __name__ == "__main__":
    if len(sys.argv) == 1 or '--help' in sys.argv:
        print("""
Usage: python convert_xlsx_to_csv.py --file <filename> [--remove-top-rows <number>] [--change-delim-from <char>] [--change-delim-to <char>]

Options:
  --file                  Path to the XLSX file (required)
  --remove-top-rows       Number of top rows to remove (default: 0)
  --change-delim-from     Delimiter to change from (default: ",")
  --change-delim-to       Delimiter to change to (default: ",")

Examples:
  python convert_xlsx_to_csv.py --file yourfile.xlsx
  python convert_xlsx_to_csv.py --file yourfile.xlsx --remove-top-rows 2
  python convert_xlsx_to_csv.py --file yourfile.xlsx --change-delim-from="," --change-delim-to=";"
        """)
    else:
        main()
