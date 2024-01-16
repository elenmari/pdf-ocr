
import sys
import pytesseract

from pdf2image import convert_from_path
from PIL import Image

import os  # NOQA
import uuid  # NOQA
import re  # NOQA

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
pattern = re.compile(r'[^\.\/]+')


def write_to_file(file_name: str = '', content: str = '') -> None:
    if not file_name:
        file_name = f'user-{uuid.uuid4()}.txt'

    if not os.path.exists('./dump'):
        # mkdir
        os.mkdir('./dump')

    try:
        with open(f'./dump/{file_name}.txt', mode='w+', encoding='utf-8') as f:
            f.write(content)
    except ValueError as e:
        print('> write_to_file ERR.')
        print(e)

    return


def main(pdf_path: str):
    images = convert_from_path(pdf_path)
    extracted_text = ''

    dump_file = pattern.findall(pdf_path)[1]
    print(dump_file)
    # for i, image in enumerate(images):
    for image in images:
        # Perform OCR on each image
        text = pytesseract.image_to_string(image, lang='eng')
        extracted_text += text

    if extracted_text:
        write_to_file(dump_file, extracted_text)

    return extracted_text


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python app.py <pdf_path>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    txt = main(pdf_path)
