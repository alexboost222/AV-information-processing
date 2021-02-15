from PIL import Image
from core.verification.verification import verify_is_image_or_exception

THRESHOLDING_MODE = '1'


# Assumes that image has 'L' mode (grayscale)
def balansed_histogram_method(image):
    verify_is_image_or_exception(image)

    histogram = image.histogram()
    result = Image.new(THRESHOLDING_MODE, (image.width, image.height))

    extreme_left = 0
    extreme_right = len(histogram) - 1
    histogram_center = int(round((extreme_right + extreme_left) / 2))

    left_part_weight = sum(histogram[extreme_left:histogram_center])
    right_part_weight = sum(histogram[histogram_center:extreme_right])

    while extreme_left < extreme_right:
        if left_part_weight > right_part_weight:
            left_part_weight -= histogram[extreme_left]
            extreme_left += 1
        else:
            right_part_weight -= histogram[extreme_right]
            extreme_right -= 1

        new_histogram_center = int(round((extreme_left + extreme_right) / 2))

        if new_histogram_center < histogram_center:
            left_part_weight -= histogram[histogram_center]
            right_part_weight += histogram[histogram_center]
        elif new_histogram_center > histogram_center:
            left_part_weight += histogram[histogram_center]
            right_part_weight -= histogram[histogram_center]

        histogram_center = new_histogram_center

    threshold_color = histogram_center

    for x in range(result.width):
        for y in range(result.height):
            result.putpixel((x, y), image.getpixel((x, y)) >= threshold_color)

    return result
