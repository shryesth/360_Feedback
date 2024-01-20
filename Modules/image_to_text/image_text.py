from PIL import Image
import pytesseract

def image_to_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def save_to_txt_file(text):
    output_file = input("Enter the output file location (including file name and .txt extension): ")
    if output_file:
        with open(output_file, "w") as file:
            file.write(text)
            print("Text saved to {}".format(output_file))

def main():
    image_path = input("Enter the image file location: ")

    if image_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        text = image_to_text(image_path)
        print("Text extracted from the image:\n{}".format(text))

        save_option = input("Do you want to save the text to a file? (yes/no): ").lower()
        if save_option == 'yes':
            save_to_txt_file(text)
    else:
        print("Please provide a valid image file.")

if __name__ == "__main__":
    main()
