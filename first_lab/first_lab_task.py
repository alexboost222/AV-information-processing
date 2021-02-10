import first_lab_logic
from PIL import Image

image_path = 'images/eye.png'
upsampled_integer_number_of_times_image_path = 'images/eye_upsampled_m.png'
downsampled_integer_number_of_times_image_path = 'images/eye_downsampled_n.png'
oversampled_two_pass_image_path = 'images/eye_oversampled_two_pass.png'
oversampled_one_pass_image_path = 'images/eye_oversampled_one_pass.png'

m = 3
n = 2

im = Image.open(image_path)
first_lab_logic.upsample_integer_number_of_times(im, m).save(upsampled_integer_number_of_times_image_path)
first_lab_logic.downsample_integer_number_of_times(im, n).save(downsampled_integer_number_of_times_image_path)
first_lab_logic.downsample_integer_number_of_times(
    first_lab_logic.upsample_integer_number_of_times(im, m), n).save(oversampled_two_pass_image_path)
