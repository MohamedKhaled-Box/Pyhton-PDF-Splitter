#!/usr/bin/env python3
"""
PDF Splitter Script

Usage:
    python pdf_splitter.py [path_to_pdf]
    
    If no path is provided, the script will prompt for one.

Example:
    python pdf_splitter.py document.pdf
    
    Then follow the prompts:
    - Enter number of output files: 3
    - For part 1, enter start page: 1, end page: 5
    - For part 2, enter start page: 10, end page: 15
    - For part 3, enter start page: 3, end page: 7
    
    Output:
    - document_part1.pdf (pages 1-5)
    - document_part2.pdf (pages 10-15)
    - document_part3.pdf (pages 3-7)
"""

import sys
import os
try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    try:
        from PyPDF2 import PdfReader, PdfWriter
    except ImportError:
        print("Error: Neither pypdf nor PyPDF2 is installed.")
        print("Please install one of them: pip install pypdf")
        sys.exit(1)



def get_pdf_path():
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
    else:
        pdf_path = input("Enter the path to the PDF file: ").strip()
    
    if not os.path.exists(pdf_path):
        print(f"Error: File '{pdf_path}' does not exist.")
        sys.exit(1)
    
    if not pdf_path.lower().endswith('.pdf'):
        print(f"Warning: File '{pdf_path}' may not be a PDF file.")
    
    return pdf_path


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def get_page_range(part_num, total_pages):
    while True:
        print(f"\nPart {part_num}:")
        start_page = get_positive_integer(f"  Enter starting page number (1-{total_pages}): ")
        end_page = get_positive_integer(f"  Enter ending page number (1-{total_pages}): ")
        
        if start_page > total_pages:
            print(f"Error: Starting page {start_page} is out of range. PDF has {total_pages} pages.")
            continue
        
        if end_page > total_pages:
            print(f"Error: Ending page {end_page} is out of range. PDF has {total_pages} pages.")
            continue
        
        if start_page > end_page:
            print(f"Error: Starting page ({start_page}) cannot be greater than ending page ({end_page}).")
            continue
        
        return start_page, end_page


def split_pdf(pdf_path, ranges):
    reader = PdfReader(pdf_path)
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_dir = os.path.dirname(pdf_path) or '.'
    
    for i, (start, end) in enumerate(ranges, 1):
        writer = PdfWriter()
        
        for page_num in range(start - 1, end):
            writer.add_page(reader.pages[page_num])
        
        output_filename = f"{base_name}_part{i}.pdf"
        output_path = os.path.join(output_dir, output_filename)
        
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
        
        print(f"Created: {output_filename} (pages {start}-{end})")


def main():
    pdf_path = get_pdf_path()
    
    try:
        reader = PdfReader(pdf_path)
        total_pages = len(reader.pages)
        print(f"\nPDF loaded successfully. Total pages: {total_pages}")
    except Exception as e:
        print(f"Error reading PDF: {e}")
        sys.exit(1)
    
    num_parts = get_positive_integer(f"\nHow many separate output files do you want to create? ")
    
    ranges = []
    for i in range(1, num_parts + 1):
        start, end = get_page_range(i, total_pages)
        ranges.append((start, end))
    
    print(f"\n{'='*50}")
    print("Summary of splits:")
    for i, (start, end) in enumerate(ranges, 1):
        print(f"  Part {i}: pages {start}-{end} ({end - start + 1} pages)")
    print(f"{'='*50}\n")
    
    confirm = input("Proceed with splitting? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Operation cancelled.")
        sys.exit(0)
    
    try:
        split_pdf(pdf_path, ranges)
        print(f"\nSuccessfully created {num_parts} PDF file(s).")
    except Exception as e:
        print(f"Error during splitting: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
