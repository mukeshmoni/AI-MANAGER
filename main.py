from src.extract_data import extract_text_from_pdf, ocr_pdf_to_text
from src.process_data import extract_invoice_data
from src.categorize_data import categorize_invoice
from src.validate_data import validate_data
from src.report_data import save_data_to_csv

def process_invoice(pdf_path, is_scanned=False):
    print(f"Processing invoice from: {pdf_path}")

    # Step 1: Extract text
    if is_scanned:
        print("Using OCR extraction...")
        text = ocr_pdf_to_text(pdf_path)
    else:
        print("Using regular text extraction...")
        text = extract_text_from_pdf(pdf_path)

    print("Extracted Text:")
    print(text)

    # Step 2: Process text
    invoice_data = extract_invoice_data(text)
    print("Extracted invoice data:", invoice_data)

    # Step 3: Categorize
    invoice_data['category'] = categorize_invoice(invoice_data.get('vendor', ''))

    # Step 4: Validate
    errors = validate_data(invoice_data)
    if errors:
        print("Validation errors:", errors)
        return

    # Step 5: Save to CSV
    save_data_to_csv([invoice_data])
    print(f"Processed and saved invoice data for Invoice #{invoice_data['invoice_number']}.")

if __name__ == "__main__":
    pdf_path = "data/invoices/sample_invoice.pdf"  # Example file path
    process_invoice(pdf_path, is_scanned=False)    # Set to True if scanned PDF
