# OCR extraction service stub
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import os

def extract_text_from_image(image_path: str) -> str:
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"Error extracting text from image: {e}"

def extract_text_from_pdf(pdf_path: str) -> str:
    try:
        images = convert_from_path(pdf_path)
        text = ""
        for img in images:
            text += pytesseract.image_to_string(img) + "\n"
        return text
    except Exception as e:
        return f"Error extracting text from PDF: {e}"
