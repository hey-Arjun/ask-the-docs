import os
from pypdf import PdfReader
import pytesseract
from pdf2image import convert_from_path


def load_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def load_pdf_text(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text.strip()


def load_pdf_ocr(file_path: str) -> str:
    images = convert_from_path(file_path)
    text = ""

    for img in images:
        text += pytesseract.image_to_string(img)

    return text.strip()


def load_document(file_path: str) -> str:
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".txt":
        return load_txt(file_path)

    elif ext == ".pdf":
        text = load_pdf_text(file_path)

        if len(text.strip()) < 50:
            text = load_pdf_ocr(file_path)

        return text

    else:
        raise ValueError("Unsupported file format")
