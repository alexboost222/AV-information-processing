import sys
import matplotlib.pyplot as pyplot

from PIL import Image, ImageFont, ImageDraw

from core.sampling.sampling import cut_empty_rows_and_cols
from folder_helper import IMAGES_FOLDER_NAME, REPORTS_FOLDER_NAME
from mdutils.mdutils import MdUtils

from core.thresholding.thresholding import simple_threshold
from core.feature_extraction.feature_extraction import black_weight, specific_black_weight, gravity_center,\
    normalized_gravity_center, central_horizontal_axial_moment, central_vertical_axial_moment,\
    normalized_central_horizontal_axial_moment, normalized_central_vertical_axial_moment, vertical_projection,\
    horizontal_projection


ALPHABET = 'AΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'
REPORT_FILE_NAME = 'forth_lab_report'
REPORT_FILE_TITLE = 'Лабораторная работа 4. Выделение признаков символов'
THRESHOLD = 100
PROJECTIONS_FOLDER_NAME = 'projections'
GRAYSCALE_MODE = 'L'
WHITE = 255
FONT_SIZE = 52


def generate_report(alphabet_folder_name):
    report = MdUtils(file_name=f'../{REPORTS_FOLDER_NAME}/{REPORT_FILE_NAME}')
    report.new_header(level=1, title=REPORT_FILE_TITLE)
    report.new_line(text='Выполнил Ахманов Алексей Б18-514')
    report.new_line(text='Алфавит - греческие заглавные')
    font = ImageFont.truetype(font='../fonts/times.ttf', size=FONT_SIZE)

    for letter in ALPHABET:
        letter_image_path = f'../{IMAGES_FOLDER_NAME}/{alphabet_folder_name}/{letter}.png'
        letter_image = Image.new(mode=GRAYSCALE_MODE, size=(FONT_SIZE, FONT_SIZE), color=WHITE)
        result = ImageDraw.Draw(im=letter_image, mode=GRAYSCALE_MODE)
        result.text(xy=(0, 0), text=letter, font=font, fill=0, anchor='lt')
        letter_image = cut_empty_rows_and_cols(letter_image)
        letter_image.save(letter_image_path)
        report.new_header(level=2, title=f'Буква {letter}')
        report.new_line(report.new_inline_image(text=letter, path=letter_image_path))
        thresholded = simple_threshold(letter_image, THRESHOLD)
        report.new_line(text=f'Вес черного - {black_weight(thresholded)}')
        report.new_line(text=f'Удельный вес черного - {specific_black_weight(thresholded)}')
        center = gravity_center(thresholded)
        report.new_line(text=f'Координаты центра масс - ({center[0]}, {center[1]})')
        normalized_center = normalized_gravity_center(thresholded)
        report.new_line(text=f'Нормированные координаты центра масс - ({normalized_center[0]}, {normalized_center[1]})')
        report.new_line(text=f'Центральный горизонтальный осевой момент - {central_horizontal_axial_moment(thresholded)}')
        report.new_line(text=f'Центральный вертикальный осевой момент - {central_vertical_axial_moment(thresholded)}')
        report.new_line(text=f'Нормированный центральный горизонтальный осевой момент - {normalized_central_horizontal_axial_moment(thresholded)}')
        report.new_line(text=f'Нормированный центральный вертикальный осевой момент - {normalized_central_vertical_axial_moment(thresholded)}')

        h_levels, h_projections = horizontal_projection(thresholded)
        pyplot.plot(h_levels, h_projections)
        pyplot.title(f'Horizontal projection {letter}')
        path = f'../{PROJECTIONS_FOLDER_NAME}/horizontal_projection_{letter}.png'
        pyplot.savefig(path)
        pyplot.close()

        report.new_line(report.new_inline_image(text=letter, path=path))

        v_levels, v_projections = vertical_projection(thresholded)
        pyplot.plot(v_levels, v_projections)
        pyplot.title(f'Vertical projection {letter}')
        path = f'../{PROJECTIONS_FOLDER_NAME}/vertical_projection_{letter}.png'
        pyplot.savefig(path)
        pyplot.close()

        report.new_line(report.new_inline_image(text=letter, path=path))

        report.new_line()

    report.create_md_file()


def main():
    alphabet_folder_name = sys.argv[1]
    generate_report(alphabet_folder_name)


if __name__ == '__main__':
    main()
