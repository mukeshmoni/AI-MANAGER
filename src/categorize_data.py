def categorize_invoice(vendor):
    categories = {
        'TS Rajan Auto Parts': 'Auto Parts',
        'Meng Hing Herbs': 'Food',
        'Sekolah Memandu': 'Driving Services',
        'Lightroom Gallery': 'Home Fixtures'
    }
    return categories.get(vendor, 'Miscellaneous')  # Default category 

if __name__ == "__main__":
    vendor = 'TS Rajan Auto Parts'
    category = categorize_invoice(vendor)
    print(f"Category: {category}")
