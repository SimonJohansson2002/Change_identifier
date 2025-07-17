import pdfplumber

def extract_txt(pdf_path):
    full_text = ""
    all_tables = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            # Extract plain text
            text = page.extract_text()
            if text:
                full_text += f"\n\n--- Page {page_number} ---\n\n" + text

            # Extract tables
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
