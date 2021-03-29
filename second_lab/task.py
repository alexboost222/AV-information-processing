import os
import sys

from core.grayscale import grayscale
from core.filtration import filtration
from PIL import Image
from folder_helper import IMAGES_FOLDER_NAME, image_path


def first_part_spatial_smooth(image, image_name, image_format):
    image_filtration_folder_path = f'../{IMAGES_FOLDER_NAME}/{image_name}_processed/filtration'

    spatial_smoothed_image_path = f'{image_filtration_folder_path}/{image_name}_spatial_smoothed.{image_format}'
    spatial_smoothed_difference_image_path = f'{image_filtration_folder_path}/{image_name}_spatial_smoothed_difference.{image_format}'

    os.makedirs(image_filtration_folder_path, exist_ok=True)
    grayscaled = grayscale.mean_grayscale(image)
    filtration.spatial_smoothing(grayscaled).save(spatial_smoothed_image_path)
    filtration.spatial_smoothing_difference(grayscaled).save(spatial_smoothed_difference_image_path)


def main():
    im_name, im_format = sys.argv[1].split('.')
    im = Image.open(image_path(im_name, im_format)).convert('RGB')
    first_part_spatial_smooth(im, im_name, im_format)


if __name__ == '__main__':
    main()
