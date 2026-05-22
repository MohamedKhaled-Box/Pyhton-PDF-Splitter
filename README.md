# PDF Splitter by Page Ranges

A simple Python script that splits a PDF into multiple smaller PDF files based on user-defined page ranges.

## Features

- Split PDFs into multiple files
- Supports overlapping page ranges
- Supports non-sequential ranges
- Allows skipping pages
- Interactive prompts for easy use
- Input validation for page ranges
- Works with both `pypdf` and `PyPDF2`

---

# Requirements

- Python 3.7 or higher
- One of the following libraries:
  - `pypdf` (recommended)
  - `PyPDF2`

Install the recommended dependency:

```bash
pip install pypdf
```

Or alternatively:

```bash
pip install PyPDF2
```

---

# Files

- `pdf_splitter.py` — Main script

---

# Usage

## Option 1: Interactive Mode

Run the script without arguments:

```bash
python pdf_splitter.py
```

The script will ask for:

1. PDF file path
2. Number of output files
3. Start and end page numbers for each file

Example:

```text
Enter the path to the PDF file: sample.pdf

How many output PDF files do you want to create? 2

Output File #1
Enter starting page number (1-indexed): 1
Enter ending page number (1-indexed, inclusive): 5

Output File #2
Enter starting page number (1-indexed): 10
Enter ending page number (1-indexed, inclusive): 15
```

---

## Option 2: Command-Line Argument

Provide the PDF path directly:

```bash
python pdf_splitter.py input.pdf
```

You will still be prompted for page ranges.

---

# Output Files

Generated files will be saved in the same directory as the original PDF.

Example:

```text
original.pdf
```

Will generate:

```text
original_part1.pdf
original_part2.pdf
original_part3.pdf
```

---

# Notes

- Page numbers are **1-indexed**
- Start and end pages are **inclusive**
- Ranges may:
  - Overlap
  - Skip pages
  - Be non-sequential

Examples of valid ranges:

| Range | Description |
|------|------|
| 1-5 | First 5 pages |
| 3-10 | Middle section |
| 5-5 | Single page |
| 10-20 | Later section |

---

# Error Handling

The script validates:

- File existence
- Positive integer inputs
- Valid page ranges
- Page numbers within PDF limits

Invalid input will trigger a re-prompt instead of crashing.

---

# Example Workflow

```bash
python pdf_splitter.py report.pdf
```

Input:

```text
How many output PDF files do you want to create? 3

Part 1: 1 to 5
Part 2: 6 to 10
Part 3: 20 to 25
```

Output:

```text
report_part1.pdf
report_part2.pdf
report_part3.pdf
```

---

# License

Free to use and modify.
