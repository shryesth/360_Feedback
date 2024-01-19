import PySimpleGUI as sg
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
    sg.theme("DarkGrey2")

    layout = [
        [sg.Text("Select a PDF file:")],
        [sg.InputText(key="pdf_path", size=(40, 1)), sg.FileBrowse()],
        [sg.Button("Convert to Text"), sg.Button("Exit")],
    ]

    window = sg.Window("PDF to Text Converter", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Exit":
            break
        elif event == "Convert to Text":
            pdf_path = values["pdf_path"]
            if pdf_path:
                txt_path = pdf_path.rsplit(".", 1)[0] + ".txt"
                pdf_to_text(pdf_path, txt_path)
                sg.popup(f"Conversion complete. Text saved to:\n{txt_path}")
            else:
                sg.popup_error("Please select a PDF file.")

    window.close()

if __name__ == "__main__":
    main()
