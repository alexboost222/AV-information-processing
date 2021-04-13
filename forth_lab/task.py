import sys
import matplotlib.pyplot as pyplot

from PIL import Image

from folder_helper import IMAGES_FOLDER_NAME, REPORTS_FOLDER_NAME
from mdutils.mdutils import MdUtils

from core.thresholding.thresholding import simple_threshold
from core.grayscale.grayscale import mean_grayscale
from core.feature_extraction.feature_extraction import black_weight, specific_black_weight, gravity_center,\
    normalized_gravity_center, central_horizontal_axial_moment, central_vertical_axial_moment, normalized_central_horizontal_axial_moment,\
    normalized_central_vertical_axial_moment, vertical_projection, horizontal_projection


ALPHABET = 'AΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'
# ALPHABET = 'A'
REPORT_FILE_NAME = 'forth_lab_report'
REPORT_FILE_TITLE = 'Лабораторная работа 4. Выделение признаков символов'
THRESHOLD = 100
PROJECTIONS_FOLDER_NAME = 'projections'


# TODO grab letters from .ttf file and create images on the fly
# TODO make method that cuts borders and use it
def generate_report(alphabet_folder_name):
    report = MdUtils(file_name=f'../{REPORTS_FOLDER_NAME}/{REPORT_FILE_NAME}')
    report.new_header(level=1, title=REPORT_FILE_TITLE)
    report.new_line(text='Выполнил Ахманов Алексей Б18-514')
    report.new_line(text='Алфавит - греческие заглавные')

    for letter in ALPHABET:
        letter_image_path = f'../{IMAGES_FOLDER_NAME}/{alphabet_folder_name}/{letter}.png'
        report.new_header(level=2, title=f'Буква {letter}')
        report.new_line(report.new_inline_image(text=letter, path=letter_image_path))
        letter_image = Image.open(letter_image_path).convert('RGB')
        grayscaled = mean_grayscale(letter_image)
        thresholded = simple_threshold(grayscaled, THRESHOLD)
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
