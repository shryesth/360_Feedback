import os
import pytesseract
from PIL import Image

def convert_image_to_text(image_path, output_folder='converted_text'):
    # extract text from image
    text = extract_text_from_image(image_path)

    # create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # create text file and write extracted text
    text_file_path = os.path.join(output_folder, os.path.basename(image_path).replace('.', '_') + '.txt')
    with open(text_file_path, 'w') as f:
        f.write(text)

def extract_text_from_image(image_path):
    # load image using PIL
    image = Image.open(image_path)

    # convert image to text using pytesseract
    text = pytesseract.image_to_string(image)

    return text

# convert images in a folder to text files in another folder
input_folder = 'converted_images'
output_folder = 'converted_text'

if os.path.exists(input_folder):
    for image_file in os.listdir(input_folder):
        if image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_folder, image_file)
            convert_image_to_text(image_path, output_folder)
else:
    print(f"Input folder '{input_folder}' does not exist.")