import os

from PIL import Image
from mdutils import MdUtils

from core import helpers, enhancement
from core.constants import constants
from core.grayscale import grayscale

IMAGES = [
    'old_paris.jpg',
    'old_saratov.jpg',
    'old_serpukhov.jpg'
]


def generate_report():
    report = MdUtils(file_name=f'./report.md')
    report.new_header(level=1, title='Контрастирование')
    report.new_line(text='Выполнил Ахманов Алексей Б18-514')

    for im in IMAGES:
        image_path = f'{helpers.folder_helper.IMAGES_FOLDER_PATH}/{im}'

        processed_image_folder_path = f'{image_path}_processed'
        os.makedirs(processed_image_folder_path, exist_ok=True)

        linear_contrasted_image_path = f'{processed_image_folder_path}/{im}_linear_contrasted.png'

        image = Image.open(fp=image_path).convert(constants.RGB_MODE)

        # Contrasting
        enhancement.contrasting.linear_contrasting(grayscale.mean_grayscale(image)).save(linear_contrasted_image_path)

        # Report
        report.new_header(level=2, title=f'{im}')

        report.new_header(level=3, title='Исходная картинка')
        report.new_line(report.new_inline_image(text='Исходная картинка', path=image_path))

        report.new_header(level=3, title='Линейное контрастирование')
        report.new_line(report.new_inline_image(text='Линейное контрастирование', path=linear_contrasted_image_path))

    report.create_md_file()


def main():
    generate_report()


if __name__ == '__main__':
    main()
