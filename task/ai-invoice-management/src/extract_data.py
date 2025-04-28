import pdfplumber
from PIL import Image, ImageEnhance
import pytesseract
from pdf2image import convert_from_path


def preprocess_image(image):
    # Convert to grayscale
    image = image.convert('L')
    
    # Enhance the contrast of the image
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)  
    
    return image


def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()  
    return text

def ocr_pdf_to_text(pdf_path):
    # Convert the PDF 
    images = convert_from_path(pdf_path)
    
    text = ''
    for image in images:
        preprocessed_image = preprocess_image(image)  # Preprocess the image of the pdfpage
        ocr_text = pytesseract.image_to_string(preprocessed_image) 
        print(f"OCR Extracted Text: {ocr_text}")  
        text += ocr_text
    
    return text
