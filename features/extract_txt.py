import pdfplumber

def extract_txt(pdf_path, include_tables=False):
    full_text = ""
    all_tables = []

    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        half_page = total_pages // 2

        for page_number, page in enumerate(pdf.pages, start=1):
            # Text extraction logic
            if include_tables:
                # Extract full text if including tables
                text = page.extract_text()
                if text:
                    full_text += f"\n\n--- Page {page_number} ---\n\n" + text
            else:
                # Only extract text from first half if not including tables
                if page_number <= half_page:
                    text = page.extract_text()
                    if text:
                        full_text += f"\n\n--- Page {page_number} ---\n\n" + text

            # Table extraction logic — always extract if include_tables is True
            if include_tables:
                tables = page.extract_tables()
                for table in tables:
                    markdown_table = convert_table_to_markdown(table)
                    all_tables.append(f"\n\n--- Table from Page {page_number} ---\n\n{markdown_table}")

    return full_text.strip(), all_tables

def convert_table_to_markdown(table):
    if not table or not table[0]:
        return ""
    
    header = table[0]
    rows = table[1:]

    def format_row(row):
        return "| " + " | ".join(str(cell or "") for cell in row) + " |"

    md = format_row(header) + "\n"
    md += "| " + " | ".join(["---"] * len(header)) + " |\n"
    for row in rows:
        md += format_row(row) + "\n"

    return md.strip()


if __name__=='__main__':
    text, tables = extract_txt("test_data/VPLAY-B24Q3.pdf")
    # Print preview
    #print("=== Extracted Text Preview ===")
    #print(text[:1000])  # Preview first 1000 characters

    print("\n=== Extracted Tables ===")
    for table_md in tables[1:2]:
        print(table_md)
