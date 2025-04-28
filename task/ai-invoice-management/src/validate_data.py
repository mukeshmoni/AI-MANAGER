def validate_data(invoice_data):
    errors = []
    if not invoice_data.get('invoice_number'):
        errors.append("Missing invoice number")
    if not invoice_data.get('invoice_date'):
        errors.append("Missing invoice date")
    if not invoice_data.get('invoice_amount'):
        errors.append("Missing invoice amount")
    if not invoice_data.get('vendor'):
        errors.append("Missing vendor name")
    return errors
