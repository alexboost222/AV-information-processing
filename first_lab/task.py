import os
import sys

from core.sampling import sampling
from core.grayscale import grayscale
from core.thresholding import thresholding
from PIL import Image
from folder_helper import IMAGES_FOLDER_NAME, image_path


def first_part_sampling(image, image_name, image_format):
    image_sampling_folder_path = f'../{IMAGES_FOLDER_NAME}/{image_name}_processed/sampling'
    upsampled_integer_number_of_times_image_path = f'{image_sampling_folder_path}/{image_name}_upsampled_m.{image_format}'
    downsampled_integer_number_of_times_image_path = f'{image_sampling_folder_path}/{image_name}_downsampled_n.{image_format}'
    oversampled_two_pass_image_path = f'{image_sampling_folder_path}/{image_name}_oversampled_two_pass.{image_format}'
    oversampled_one_pass_image_path = f'{image_sampling_folder_path}/{image_name}_oversampled_one_pass.{image_format}'

    upsample_factor = 3
    downsample_factor = 4

    os.makedirs(image_sampling_folder_path, exist_ok=True)

    sampling.bilinear_interpolation_upsampling(image, upsample_factor).save(
        upsampled_integer_number_of_times_image_path)
    sampling.decimation_downsampling(image, downsample_factor).save(downsampled_integer_number_of_times_image_path)
    sampling.decimation_downsampling(sampling.bilinear_interpolation_upsampling(image, upsample_factor),
                                     downsample_factor).save(oversampled_two_pass_image_path)
    sampling.one_pass_resampling(image, upsample_factor, downsample_factor).save(oversampled_one_pass_image_path)


def second_part_grayscale(image, image_name, image_format):
    image_grayscale_folder_path = f'../{IMAGES_FOLDER_NAME}/{image_name}_processed/grayscale'

    mean_grayscaled_image_path = f'{image_grayscale_folder_path}/{image_name}_mean_grayscaled.{image_format}'
    photoshop_grayscaled_image_path = f'{image_grayscale_folder_path}/{image_name}_photoshop_grayscaled.{image_format}'

    os.makedirs(image_grayscale_folder_path, exist_ok=True)

    grayscale.mean_grayscale(image).save(mean_grayscaled_image_path)
    grayscale.photoshop_grayscale(image).save(photoshop_grayscaled_image_path)


def third_part_threshold(image, image_name, image_format):
    image_threshold_folder_path = f'../{IMAGES_FOLDER_NAME}/{image_name}_processed/threshold'

    balansed_hist_thresholded_image_path = f'{image_threshold_folder_path}/{image_name}_balansed_hist_thresholded.{image_format}'

    os.makedirs(image_threshold_folder_path, exist_ok=True)
    thresholding.balansed_histogram_method(grayscale.mean_grayscale(image)).save(balansed_hist_thresholded_image_path)


def main():
    im_name, im_format = sys.argv[1].split('.')
    im = Image.open(image_path(im_name, im_format)).convert('RGB')
    first_part_sampling(im, im_name, im_format)
    second_part_grayscale(im, im_name, im_format)
    third_part_threshold(im, im_name, im_format)


if __name__ == '__main__':
    main()
