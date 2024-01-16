
import sys
import pytesseract

from pdf2image import convert_from_path
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'


def main(pdf_path):
    images = convert_from_path(pdf_path)
    extracted_text = ''
    img = pytesseract.image_to_string(images[0], lang='eng')
    print(img)
    # for image in enumerate(images):
    #     # Perform OCR on each image
    #     text = pytesseract.image_to_string(image, lang='eng')
    #     extracted_text += text

    return extracted_text


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <pdf_path>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    txt = main(pdf_path)
    print(txt)
