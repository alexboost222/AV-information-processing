import csv
from pprint import pprint

from PIL import Image, ImageFont, ImageDraw

from core.feature_extraction.feature_extraction import proximity_measure, symbol_segments, proximity_assessment
from core.sampling.sampling import cut_empty_rows_and_cols

ALPHABET = 'AΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'
PHRASE = 'ΨΟΜΓΤΗ ΛΙΟΣΡΦΔΔΦΗ ΦΓΤΩΖΦΥ ΚΜΙΞ ΒΞ'
SYMBOLS_DIFF_THRESHOLD = 0.03
GRAYSCALE_MODE = 'L'
WHITE = 255
FONT_SIZE = 52
FONT = ImageFont.truetype(font='../fonts/times.ttf', size=FONT_SIZE)


def generate_report():
    phrase_image = Image.new(mode=GRAYSCALE_MODE, size=(1200, FONT_SIZE), color=WHITE)
    result = ImageDraw.Draw(im=phrase_image, mode=GRAYSCALE_MODE)
    result.text(xy=(0, 0), text=PHRASE, font=FONT, fill=0, anchor='lt')
    phrase_image = cut_empty_rows_and_cols(phrase_image)

    p_assessment = proximity_assessment(phrase_image, SYMBOLS_DIFF_THRESHOLD, PHRASE)

    with open('./proximity_assessment.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for i in p_assessment:
            writer.writerow(i)


def main():
    generate_report()


if __name__ == '__main__':
    main()
