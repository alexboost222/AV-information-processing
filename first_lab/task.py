import os

from core.sampling import sampling
from core.grayscale import grayscale
from core.thresholding import thresholding
from PIL import Image

IMAGE_NAME = 'cat'
IMAGE_FORMAT = 'png'
IMAGE_MODE = 'RGB'
IMAGE_PATH = f'images/{IMAGE_NAME}.{IMAGE_FORMAT}'


def first_part_sampling(image):
    image_sampling_folder_path = f'images/{IMAGE_NAME}_processed/sampling'
    upsampled_integer_number_of_times_image_path = f'{image_sampling_folder_path}/{IMAGE_NAME}_upsampled_m.{IMAGE_FORMAT}'
    downsampled_integer_number_of_times_image_path = f'{image_sampling_folder_path}/{IMAGE_NAME}_downsampled_n.{IMAGE_FORMAT}'
    oversampled_two_pass_image_path = f'{image_sampling_folder_path}/{IMAGE_NAME}_oversampled_two_pass.{IMAGE_FORMAT}'
    oversampled_one_pass_image_path = f'{image_sampling_folder_path}/{IMAGE_NAME}_oversampled_one_pass.{IMAGE_FORMAT}'

    upsample_factor = 3
    downsample_factor = 4

    os.makedirs(image_sampling_folder_path, exist_ok=True)

    sampling.bilinear_interpolation_upsampling(image, upsample_factor).save(
        upsampled_integer_number_of_times_image_path)
    sampling.decimation_downsampling(image, downsample_factor).save(downsampled_integer_number_of_times_image_path)
    sampling.decimation_downsampling(sampling.bilinear_interpolation_upsampling(image, upsample_factor),
                                     downsample_factor).save(oversampled_two_pass_image_path)
    sampling.one_pass_resampling(image, upsample_factor, downsample_factor).save(oversampled_one_pass_image_path)


def second_part_grayscale(image):
    image_grayscale_folder_path = f'images/{IMAGE_NAME}_processed/grayscale'

    mean_grayscaled_image_path = f'{image_grayscale_folder_path}/{IMAGE_NAME}_mean_grayscaled.{IMAGE_FORMAT}'
    photoshop_grayscaled_image_path = f'{image_grayscale_folder_path}/{IMAGE_NAME}_photoshop_grayscaled.{IMAGE_FORMAT}'

    os.makedirs(image_grayscale_folder_path, exist_ok=True)

    grayscale.mean_grayscale(image).save(mean_grayscaled_image_path)
    grayscale.photoshop_grayscale(image).save(photoshop_grayscaled_image_path)


def third_part_threshold(image):
    image_threshold_folder_path = f'images/{IMAGE_NAME}_processed/threshold'

    balansed_hist_thresholded_image_path = f'{image_threshold_folder_path}/{IMAGE_NAME}_balansed_hist_thresholded.{IMAGE_FORMAT}'

    os.makedirs(image_threshold_folder_path, exist_ok=True)
    thresholding.balansed_histogram_method(grayscale.mean_grayscale(image)).save(balansed_hist_thresholded_image_path)


im = Image.open(IMAGE_PATH).convert(IMAGE_MODE)
first_part_sampling(im)
second_part_grayscale(im)
third_part_threshold(im)
