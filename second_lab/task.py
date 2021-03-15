import os

from core.grayscale import grayscale
from core.filtration import filtration
from PIL import Image

IMAGE_NAME = 'old_text_2'
IMAGE_FORMAT = 'jpg'
IMAGE_MODE = 'RGB'
IMAGES_FOLDER_NAME = 'images'
IMAGE_PATH = f'../{IMAGES_FOLDER_NAME}/{IMAGE_NAME}.{IMAGE_FORMAT}'


def first_part_spatial_smooth(image):
    image_filtration_folder_path = f'../{IMAGES_FOLDER_NAME}/{IMAGE_NAME}_processed/filtration'

    spatial_smoothed_image_path = f'{image_filtration_folder_path}/{IMAGE_NAME}_spatial_smoothed.{IMAGE_FORMAT}'
    spatial_smoothed_difference_image_path = f'{image_filtration_folder_path}/{IMAGE_NAME}_spatial_smoothed_difference.{IMAGE_FORMAT}'

    os.makedirs(image_filtration_folder_path, exist_ok=True)
    grayscaled = grayscale.mean_grayscale(image)
    filtration.spatial_smoothing(grayscaled).save(spatial_smoothed_image_path)
    filtration.spatial_smoothing_difference(grayscaled).save(spatial_smoothed_difference_image_path)


im = Image.open(IMAGE_PATH).convert(IMAGE_MODE)
first_part_spatial_smooth(im)
