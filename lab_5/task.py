from PIL import Image, ImageDraw, ImageFont
from mdutils import MdUtils

from core.draw import draw
from core.sampling.sampling import cut_empty_rows_and_cols
from folder_helper import REPORTS_FOLDER_NAME, PROJECTIONS_FOLDER_NAME, IMAGES_FOLDER_NAME

PHRASE = 'ΨΟΜΓΤΗ ΛΙΟΣΡΦΔΔΦΗ ΦΓΤΩΖΦΥ ΚΜΙΞ ΒΞ '
REPORT_FILE_NAME = 'lab_5_report'
REPORT_FILE_TITLE = 'Лабораторная работа 5. Сегментация текста'
PHRASE_FOLDER_NAME = 'greek_phrase_uppercase'
GRAYSCALE_MODE = 'L'
WHITE = 255
FONT_SIZE = 52
FONT = ImageFont.truetype(font='../fonts/times.ttf', size=FONT_SIZE)


def generate_report():
    # report = MdUtils(file_name=f'../{REPORTS_FOLDER_NAME}/{REPORT_FILE_NAME}')
    # report.new_header(level=1, title=REPORT_FILE_TITLE)
    # report.new_line(text='Выполнил Ахманов Алексей Б18-514')
    # report.new_line(text='Алфавит - греческие заглавные')

    phrase_image_path = f'../{IMAGES_FOLDER_NAME}/{PHRASE_FOLDER_NAME}/phrase.png'
    phrase_projections_image_path = f'../{IMAGES_FOLDER_NAME}/{PHRASE_FOLDER_NAME}/phrase_projections.png'
    phrase_segments_image_path = f'../{IMAGES_FOLDER_NAME}/{PHRASE_FOLDER_NAME}/phrase_segments.png'
    phrase_image = Image.new(mode=GRAYSCALE_MODE, size=(1200, FONT_SIZE), color=WHITE)
    result = ImageDraw.Draw(im=phrase_image, mode=GRAYSCALE_MODE)
    result.text(xy=(0, 0), text=PHRASE, font=FONT, fill=0, anchor='lt')
    phrase_image = cut_empty_rows_and_cols(phrase_image)
    phrase_image.save(phrase_image_path)
    draw.draw_projections(phrase_image).save(phrase_projections_image_path)
    draw.draw_symbol_segments(phrase_image).save(phrase_segments_image_path)


def main():
    generate_report()


if __name__ == '__main__':
    main()
