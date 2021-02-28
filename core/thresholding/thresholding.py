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
    histogram_center = histogram_weight_center(histogram, extreme_left, extreme_right)

    while extreme_left < extreme_right:
        left_part_weight = sum(histogram[extreme_left:histogram_center])
        right_part_weight = sum(histogram[histogram_center:extreme_right])

        if left_part_weight > right_part_weight:
            extreme_left += 1
        else:
            extreme_right -= 1

        histogram_center = histogram_weight_center(histogram, extreme_left, extreme_right)

    threshold_color = histogram_center

    for x in range(result.width):
        for y in range(result.height):
            result.putpixel((x, y), image.getpixel((x, y)) >= threshold_color)

    return result


def histogram_weight_center(histogram, start, stop):
    weight_delta_absolute = sum(histogram[start:stop])
    center = start

    for i in range(start, stop):
        left_part_weight = sum(histogram[start:i])
        right_part_weight = sum(histogram[i:stop])

        new_weight_delta_absolute = abs(right_part_weight - left_part_weight)

        if new_weight_delta_absolute < weight_delta_absolute:
            center = i
            weight_delta_absolute = new_weight_delta_absolute

    return center
