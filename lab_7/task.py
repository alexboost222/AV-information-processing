from pprint import pprint

from PIL import Image

from core import helpers, constants, draw, grayscale, texturing

IMAGES = [
    'white.png'
]


def generate_report():
    for im in IMAGES:
        image_path = f'{helpers.folder_helper.IMAGES_FOLDER_PATH}/{im}'
        image = Image.open(image_path).convert(constants.constants.RGB_MODE)
        grayscaled = grayscale.grayscale.mean_grayscale(image)

        # draw.draw.draw_series_length_matrix(grayscale.grayscale.mean_grayscale(image)).show()

        [print(row) for row in texturing.texturing.series_length_matrix(grayscaled)]
        print(texturing.texturing.sre_coefficient(grayscaled))


def main():
    generate_report()


if __name__ == '__main__':
    main()
