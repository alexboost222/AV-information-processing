from core.sampling import sampling
from PIL import Image

image_path = 'images/cool.jpg'
upsampled_integer_number_of_times_image_path = 'images/cool_upsampled_m.jpg'
downsampled_integer_number_of_times_image_path = 'images/cool_downsampled_n.jpg'
oversampled_two_pass_image_path = 'images/cool_oversampled_two_pass.jpg'
oversampled_one_pass_image_path = 'images/cool_oversampled_one_pass.jpg'

upsample_factor = 3
downsample_factor = 4

im = Image.open(image_path)
sampling.bilinear_interpolation_upsampling(im, upsample_factor).save(upsampled_integer_number_of_times_image_path)
sampling.decimation_downsampling(im, downsample_factor).save(downsampled_integer_number_of_times_image_path)
sampling.decimation_downsampling(sampling.bilinear_interpolation_upsampling(im, upsample_factor), downsample_factor).save(oversampled_two_pass_image_path)
