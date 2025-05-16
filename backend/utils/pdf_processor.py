# backend/utils/pdf_processor.py

import fitz  # PyMuPDF

import fitz  # PyMuPDF

def extract_text_from_pdf(filepath):
    try:
        text = ""
        with fitz.open(filepath) as doc:
            for page in doc:
                text += page.get_text()
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""



def search_in_pdf_text(pdf_path, query):
    """
    Extracts text from the PDF and searches for the given query.
    Returns matching lines.
    """
    results = []
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text = page.get_text()
            for line in text.split('\n'):
                if query.lower() in line.lower():
                    results.append(line)
    return results
