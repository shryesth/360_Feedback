from pdf2image import convert_from_path
import os

def convert_pdf_to_images(pdf_path, output_folder='converted_images'):
    # convert pdf to images
    images = convert_from_path(pdf_path)

    # create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # save each image
    for i, image in enumerate(images):
        image.save(f"{output_folder}/image_{i}.jpg", "JPEG")

# usage
pdf_path = ' '
convert_pdf_to_images(pdf_path)
    
