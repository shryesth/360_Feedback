import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract

class ImageToTextConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to Text Converter")

        self.image_path = ""
        self.text_result = tk.StringVar()

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Image display area
        self.image_label = tk.Label(self.root)
        self.image_label.pack()

        # Select Image button
        select_button = tk.Button(self.root, text="Select Image", command=self.select_image)
        select_button.pack()

        # Convert button
        convert_button = tk.Button(self.root, text="Convert", command=self.convert_image_to_text)
        convert_button.pack()

        # Text result display area
        result_label = tk.Label(self.root, textvariable=self.text_result)
        result_label.pack()

    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if self.image_path:
            self.display_image()

    def display_image(self):
        image = Image.open(self.image_path)
        image.thumbnail((300, 300))  # Resize for display
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def convert_image_to_text(self):
        if self.image_path:
            image = Image.open(self.image_path)
            text = pytesseract.image_to_string(image)
            self.text_result.set(text)

            # Save the text to a .txt file
            self.save_to_txt_file(text)

    def save_to_txt_file(self, text):
        output_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if output_file:
            with open(output_file, "w") as file:
                file.write(text)
                tk.messagebox.showinfo("Success", "Text saved to {}".format(output_file))

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToTextConverter(root)
    root.mainloop()