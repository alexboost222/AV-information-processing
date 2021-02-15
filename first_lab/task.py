from core.sampling import sampling
from PIL import Image

image_name = 'picture3'
image_format = 'png'
image_mode = 'RGB'

image_path = f'images/{image_name}.{image_format}'
upsampled_integer_number_of_times_image_path = f'images/{image_name}_upsampled_m.{image_format}'
downsampled_integer_number_of_times_image_path = f'images/{image_name}_downsampled_n.{image_format}'
oversampled_two_pass_image_path = f'images/{image_name}_oversampled_two_pass.{image_format}'
oversampled_one_pass_image_path = f'images/{image_name}_oversampled_one_pass.{image_format}'

upsample_factor = 3
downsample_factor = 4

image = Image.open(image_path).convert(image_mode)
sampling.bilinear_interpolation_upsampling(image, upsample_factor).save(upsampled_integer_number_of_times_image_path)
sampling.decimation_downsampling(image, downsample_factor).save(downsampled_integer_number_of_times_image_path)
sampling.decimation_downsampling(sampling.bilinear_interpolation_upsampling(image, upsample_factor), downsample_factor).save(oversampled_two_pass_image_path)
sampling.one_pass_resampling(image, upsample_factor, downsample_factor).save(oversampled_one_pass_image_path)
