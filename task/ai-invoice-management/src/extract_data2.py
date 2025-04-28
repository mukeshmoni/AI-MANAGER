# import pytesseract
# from pdf2image import convert_from_path
# from PIL import Image

# def ocr_pdf_to_text(pdf_path):
#     # Convert PDF to images
#     images = convert_from_path(pdf_path)
#     text = ""
    
  
#     for image in images:
#         text += pytesseract.image_to_string(image)
    
#     return text

# if __name__ == "__main__":
#     pdf_path = 'data/invoices/scanned_invoice.pdf'  # Replace with your actual PDF path
#     extracted_text = ocr_pdf_to_text(pdf_path)
#     print(extracted_text)
