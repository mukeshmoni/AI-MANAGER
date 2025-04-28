from src.extract_data import extract_text_from_pdf, ocr_pdf_to_text
from src.process_data import extract_invoice_data
from src.categorize_data import categorize_invoice
from src.validate_data import validate_data
from src.report_data import save_data_to_csv

def process_invoice(pdf_path, is_scanned=False):
    print(f"Processing invoice from: {pdf_path}")


    if is_scanned:
        print("Using OCR-based extraction...")
        text = ocr_pdf_to_text(pdf_path)
    else:
        print("Using regular text extraction...")
        text = extract_text_from_pdf(pdf_path)
    
    print("\nExtracted Text:\n", text)

    invoice_data = extract_invoice_data(text)
    print("\nExtracted invoice data:", invoice_data)


    if invoice_data.get('vendor') and invoice_data['vendor'] != 'Missing':
        invoice_data['category'] = categorize_invoice(invoice_data['vendor'])
    else:
        invoice_data['category'] = 'Uncategorized'
    print(f"Invoice category assigned: {invoice_data['category']}")

   
    errors = validate_data(invoice_data)
    if errors:
        print("Validation errors:", errors)
        return

   
       save_data_to_csv([invoice_data])
    print(f"\nProcessed and saved invoice data for Invoice Number: {invoice_data['invoice_number']}")

if __name__ == "__main__":
    pdf_path = "data/invoices/sample_invoice.pdf"   
    process_invoice(pdf_path, is_scanned=False)      
