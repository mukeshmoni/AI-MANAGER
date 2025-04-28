import re

def extract_invoice_data(text):
    invoice_data = {}

   # Invoice Number
    invoice_no_match = re.search(r'Invoice\s*#\s*(\d+)', text, re.IGNORECASE)
    invoice_data['invoice_number'] = invoice_no_match.group(1) if invoice_no_match else 'Missing'

    #  Invoice Date
    date_match = re.search(r'Invoice\s*Date\s*(\d{2}/\d{2}/\d{4})', text, re.IGNORECASE)
    invoice_data['invoice_date'] = date_match.group(1) if date_match else 'Missing'

    # Vendor Name 
    vendor_match = re.search(r'^(.+?)\s+INVOICE', text, re.IGNORECASE | re.MULTILINE)
    invoice_data['vendor'] = vendor_match.group(1).strip() if vendor_match else 'Missing'

    #  Total Amount
    amount_match = re.search(r'TOTAL\s+RM\s*([\d,]+\.\d{2})', text, re.IGNORECASE)
    invoice_data['invoice_amount'] = amount_match.group(1).replace(',', '') if amount_match else 'Missing'

    return invoice_data
