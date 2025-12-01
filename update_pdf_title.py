#!/usr/bin/env python3
"""Update PDF metadata title"""

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    try:
        from PyPDF2 import PdfReader, PdfWriter
    except ImportError:
        print("Error: pypdf or PyPDF2 not installed")
        exit(1)

import sys

pdf_path = "assets/pdf/Nitish_Nagesh_Academic_CV_Nov2025.pdf"

try:
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    
    # Copy all pages
    for page in reader.pages:
        writer.add_page(page)
    
    # Update metadata
    writer.add_metadata({
        "/Title": "Nitish Nagesh - Academic CV",
        "/Subject": "Academic Curriculum Vitae",
        "/Author": "Nitish Nagesh"
    })
    
    # Write to a temporary file first
    output_path = pdf_path.replace(".pdf", "_updated.pdf")
    with open(output_path, "wb") as output_file:
        writer.write(output_file)
    
    # Replace original
    import shutil
    shutil.move(output_path, pdf_path)
    
    print(f"Successfully updated PDF metadata for {pdf_path}")
    
except Exception as e:
    print(f"Error updating PDF: {e}")
    exit(1)

