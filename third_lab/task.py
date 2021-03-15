import os
import sys

from PIL import Image

from core.filtration import filtration
from core.grayscale import grayscale

IMAGES_FOLDER_NAME = 'images'


def image_path(image_name, image_format):
    return f'../{IMAGES_FOLDER_NAME}/{image_name}.{image_format}'


def first_part_roberts_cross(image, image_name, image_format):
    image_filtration_folder_path = f'../{IMAGES_FOLDER_NAME}/{image_name}_processed/filtration'

    roberts_cross_image_path = f'{image_filtration_folder_path}/{image_name}_roberts_cross.{image_format}'
    roberts_cross_difference_image_path = f'{image_filtration_folder_path}/{image_name}_roberts_cross_difference.{image_format}'

    os.makedirs(image_filtration_folder_path, exist_ok=True)
    grayscaled = grayscale.mean_grayscale(image)
    smoothed = filtration.spatial_smoothing(grayscaled)
    filtration.roberts_cross(smoothed).save(roberts_cross_image_path)
    filtration.roberts_cross_difference(smoothed).save(roberts_cross_difference_image_path)


def main():
    im_name, im_format = sys.argv[1].split('.')
    im = Image.open(image_path(im_name, im_format)).convert('RGB')
    first_part_roberts_cross(im, im_name, im_format)


if __name__ == '__main__':
    main()
