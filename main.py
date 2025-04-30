import os
from src.extract_data import extract_text_from_pdf, ocr_pdf_to_text
from src.process_data import extract_invoice_data
from src.categorize_data import categorize_invoice
from src.validate_data import validate_data
from src.report_data import save_data_to_csv

def process_invoice(pdf_path, is_scanned=False):
    print(f"\n📄 Processing invoice: {pdf_path}")
    
    if is_scanned:
        print("🔍 Using OCR for scanned PDF...")
        text = ocr_pdf_to_text(pdf_path)
    else:
        print("📄 Using text-based PDF extraction...")
        text = extract_text_from_pdf(pdf_path)

    print("📃 Extracted Text Preview:\n", text[:300])

    invoice_data = extract_invoice_data(text)
    print("🧾 Extracted Invoice Data:", invoice_data)

    if 'vendor' in invoice_data:
        invoice_data['category'] = categorize_invoice(invoice_data['vendor'])
    else:
        invoice_data['category'] = "Unknown"

    errors = validate_data(invoice_data)
    if errors:
        print("❌ Validation Errors:", errors)
        return

    save_data_to_csv([invoice_data])
    print(f"✅ Invoice {invoice_data.get('invoice_number', 'N/A')} saved successfully.")

if __name__ == "__main__":
    print("==== 📂 Batch Invoice Processor ====\n")

    folder_path = "data/invoices"
    is_scanned_input = input("📝 Are the invoices scanned PDFs? (yes/no): ").strip().lower()
    is_scanned = is_scanned_input in ['yes', 'y']

    pdf_files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]

    if not pdf_files:
        print("❌ No PDF files found in the folder.")
    else:
        for file_name in pdf_files:
            pdf_path = os.path.join(folder_path, file_name)
            try:
                process_invoice(pdf_path, is_scanned)
            except Exception as e:
                print(f"❗ Error processing {file_name}: {e}")
