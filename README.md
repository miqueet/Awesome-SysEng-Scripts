# Awesome-SysEng-Scripts

**Awesome-SysEng-Scripts**, a repository dedicated to providing scripts that make the lives of developers, system engineers, and sysadmins easier. Whether you're automating routine tasks, converting file formats, or managing infrastructure, this repository aims to be your go-to resource for reliable and efficient scripts.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Scripts](#scripts)
  - [XLSX to CSV Converter](#xlsx-to-csv-converter)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The goal of this repository is to collect and maintain a set of scripts that can help streamline various tasks for devs, sysadmins, and system engineers. Each script is designed to solve a specific problem or simplify a particular process, making it easier for you to focus on more critical aspects of your work.

## Getting Started

To get started, simply clone the repository to your local machine:

```
git clone https://github.com/yourusername/Awesome-SysEng-Scripts.git
cd Awesome-SysEng-Scripts


Scripts
XLSX to CSV Converter
This script converts an XLSX file to a CSV file and includes options to remove the top rows of the spreadsheet. It's useful for cleaning up and converting data files for further processing.

Usage
To use the XLSX to CSV converter script, run:

python convert_xlsx_to_csv.py --file <filename> [--remove-top-rows <number>]
Options
--file: Path to the XLSX file (required)
--remove-top-rows: Number of top rows to remove (default: 0)
Examples
Convert an XLSX file to CSV without removing any rows:


python convert_xlsx_to_csv.py --file yourfile.xlsx
Convert an XLSX file to CSV and remove the top 2 rows:


python convert_xlsx_to_csv.py --file yourfile.xlsx --remove-top-rows 2

Contributing
We welcome contributions from the community! If you have a script that you believe would benefit others, please submit a pull request. Make sure to follow these guidelines:

Fork the repository.
Create a new branch for your feature or bugfix.
Write your script and include a description in the script's section of the README.md.
Submit a pull request with a detailed description of your changes.
License
This project is licensed under the MIT License - see the LICENSE file for details.
