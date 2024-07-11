#!/usr/bin/env python3

import pandas as pd
import argparse
import os
import sys

def xlsx_to_csv(xlsx_filename, remove_top_rows):
    # Check if the file exists
    if not os.path.exists(xlsx_filename):
        print(f"File '{xlsx_filename}' not found.")
        return


    if not xlsx_filename.lower().endswith('.xlsx'):
        print("The file is not an XLSX file.")
        return


    try:
        df = pd.read_excel(xlsx_filename, skiprows=remove_top_rows)
    except Exception as e:
        print(f"Failed to read the Excel file: {e}")
        return

    # Create a CSV filename
    csv_filename = os.path.splitext(xlsx_filename)[0] + '.csv'

    # Save the DataFrame to a CSV file
    try:
        df.to_csv(csv_filename, index=False)
        print(f"File '{xlsx_filename}' has been converted to '{csv_filename}'.")
    except Exception as e:
        print(f"Failed to save the CSV file: {e}")

def main():
    parser = argparse.ArgumentParser(description='Convert XLSX file to CSV file.')
    parser.add_argument('--file', required=True, help='Path to the XLSX file')
    parser.add_argument('--remove-top-rows', type=int, default=0, help='Number of top rows to remove')

    args = parser.parse_args()

    xlsx_to_csv(args.file, args.remove_top_rows)

if __name__ == "__main__":
    if len(sys.argv) == 1 or '--help' in sys.argv:
        print("""
Usage: python convert_xlsx_to_csv.py --file <filename> [--remove-top-rows <number>]

Options:
  --file              Path to the XLSX file (required)
  --remove-top-rows   Number of top rows to remove (default: 0)

Examples:
  python convert_xlsx_to_csv.py --file yourfile.xlsx
  python convert_xlsx_to_csv.py --file yourfile.xlsx --remove-top-rows 2
        """)
    else:
        main()
