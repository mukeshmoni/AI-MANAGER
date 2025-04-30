from src.extract_data import extract_text_from_pdf, ocr_pdf_to_text
from src.process_data import extract_invoice_data
from src.categorize_data import categorize_invoice
from src.validate_data import validate_data
from src.report_data import save_data_to_csv

def process_invoice(pdf_path, is_scanned=False):
    print(f"\n📄 Processing invoice: {pdf_path}")
    
    # Step 1: Extract text
    if is_scanned:
        print("🔍 Using OCR for scanned PDF...")
        text = ocr_pdf_to_text(pdf_path)
    else:
        print("📄 Using text-based PDF extraction...")
        text = extract_text_from_pdf(pdf_path)
    
    print("📃 Extracted Text:\n", text[:500])  # show only first 500 chars

    # Step 2: Extract data
    invoice_data = extract_invoice_data(text)
    print("🧾 Extracted Invoice Data:", invoice_data)

    # Step 3: Categorize vendor
    if 'vendor' in invoice_data:
        invoice_data['category'] = categorize_invoice(invoice_data['vendor'])
        print("📦 Category:", invoice_data['category'])
    else:
        print("⚠️ Vendor not found! Cannot categorize.")
        invoice_data['category'] = "Unknown"

    # Step 4: Validate
    errors = validate_data(invoice_data)
    if errors:
        print("❌ Validation Errors:", errors)
        return
    
    # Step 5: Save
    save_data_to_csv([invoice_data])
    print(f"✅ Invoice {invoice_data.get('invoice_number', '(Unknown)')} saved successfully!\n")


if __name__ == "__main__":
    print("==== AI Invoice Management System ====\n")
    while True:
        pdf_path = input("📂 Enter PDF file path (or type 'exit' to quit): ").strip()
        if pdf_path.lower() == 'exit':
            print("👋 Exiting application. Goodbye!")
            break

        is_scanned_input = input("Is this a scanned PDF? (yes/no): ").strip().lower()
        is_scanned = is_scanned_input in ['yes', 'y']

        try:
            process_invoice(pdf_path, is_scanned)
        except Exception as e:
            print("❗ Error during processing:", e)
