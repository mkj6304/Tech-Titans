import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

# If using Windows, set the Tesseract path:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file. Uses OCR for scanned PDFs."""
    text = ""
    doc = fitz.open(pdf_path)

    for page in doc:
        # Try extracting searchable text
        page_text = page.get_text("text")
        if page_text.strip():
            text += page_text + "\n"
        else:
            # If no text found, use OCR
            pix = page.get_pixmap()
            img = Image.open(io.BytesIO(pix.tobytes("ppm")))
            text += pytesseract.image_to_string(img) + "\n"
    
    return text.strip()

if __name__ == "__main__":
    pdf_file = "sample.pdf"  # Replace with your PDF file
    extracted_text = extract_text_from_pdf(pdf_file)
    
    print("Extracted Text:\n", extracted_text)
