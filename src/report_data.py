import csv
import os

def save_data_to_csv(invoices, output_file="output/invoices.csv"):
    # Create 'output' folder if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # If the file doesn't exist yet, create it with headers
    file_exists = os.path.isfile(output_file)

    with open(output_file, mode="a", newline="", encoding="utf-8") as csvfile:
        fieldnames = ['invoice_number', 'invoice_date', 'invoice_amount', 'vendor', 'category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        for invoice in invoices:
            writer.writerow(invoice)
