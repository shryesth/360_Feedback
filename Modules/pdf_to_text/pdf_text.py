import fitz  # PyMuPDF

def pdf_to_text(pdf_path, txt_path):
    pdf_document = fitz.open(pdf_path)
    text = ""

    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text += page.get_text()

    pdf_document.close()

    with open(txt_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(text)

    return txt_path

def main():
    pdf_path = input("Enter the PDF file location: ")

    if pdf_path.endswith(".pdf"):
        txt_path = pdf_path.rsplit(".", 1)[0] + ".txt"
        pdf_to_text(pdf_path, txt_path)
        print(f"Conversion complete. Text saved to:\n{txt_path}")
    else:
        print("Please provide a valid PDF file.")

if __name__ == "__main__":
    main()
    