from core.sampling import sampling
from PIL import Image

image_path = 'images/cool.jpg'
upsampled_integer_number_of_times_image_path = 'images/cool_upsampled_m.jpg'
downsampled_integer_number_of_times_image_path = 'images/cool_downsampled_n.jpg'
oversampled_two_pass_image_path = 'images/cool_oversampled_two_pass.jpg'
oversampled_one_pass_image_path = 'images/cool_oversampled_one_pass.jpg'

m = 3
n = 2

im = Image.open(image_path)
sampling.bilinear_interpolation_upsampling(im, m).save(upsampled_integer_number_of_times_image_path)
sampling.decimation_downsampling(im, n).save(downsampled_integer_number_of_times_image_path)
sampling.decimation_downsampling(sampling.bilinear_interpolation_upsampling(im, m), n).save(oversampled_two_pass_image_path)
