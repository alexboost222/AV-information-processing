from PIL import Image
from random import sample as random_sample
from core.math import math


def closest_neighbor_upsampling(image, factor):
    is_image = isinstance(image, Image.Image)

    if not is_image:
        raise TypeError(f"Object passed to function has type {image.__class__}."
                        "Expected that it will be subclass of Image.")

    if factor == 1:
        return image.copy()

    is_natural = isinstance(factor, int) and factor > 0

    if not is_natural:
        raise ValueError(f"Passed upsampling factor {factor} is not natural but natural expected.")

    result_width = image.width * factor
    result_height = image.height * factor
    result = Image.new(image.mode, (result_width, result_height))

    for i in range(result_height):
        y_nearest = int(i * image.height / result_height)
        for j in range(result_width):
            x_nearest = int(j * image.width / result_width)
            result.putpixel((j, i), image.getpixel((x_nearest, y_nearest)))

    return result


def bilinear_interpolation_upsampling(image, factor):
    is_image = isinstance(image, Image.Image)

    if not is_image:
        raise TypeError(f"Object passed to function has type {image.__class__}."
                        "Expected that it will be subclass of Image.")

    if factor == 1:
        return image.copy()

    is_natural = isinstance(factor, int) and factor > 0

    if not is_natural:
        raise ValueError(f"Passed upsampling factor {factor} is not natural but natural expected.")

    result_width = image.width * factor
    result_height = image.height * factor
    result = Image.new(image.mode, (result_width, result_height))

    for i in range(result_height):
        for j in range(result_width):
            if (i // factor == 0) and (j // factor == 0):
                result.putpixel((j, i), image.getpixel((i // factor, j // factor)))
                continue

            prev_row_number = i // factor
            next_row_number = prev_row_number + 1
            prev_col_number = j // factor
            next_col_number = prev_col_number + 1

            if (next_row_number >= image.height) or (next_col_number >= image.width):
                result.putpixel((j, i), (0, 0, 0))
                continue

            prev_row_prev_col_pixel = image.getpixel((prev_col_number, prev_row_number))
            prev_row_next_col_pixel = image.getpixel((next_col_number, prev_row_number))
            next_row_prev_col_pixel = image.getpixel((prev_col_number, next_row_number))
            next_row_next_col_pixel = image.getpixel((next_col_number, next_row_number))

            upper_pseudo_pixel = math.rgb_color_lerp(prev_col_number, prev_row_prev_col_pixel, next_col_number, prev_row_next_col_pixel, j / factor)
            lower_pseudo_pixel = math.rgb_color_lerp(prev_col_number, next_row_prev_col_pixel, next_col_number, next_row_next_col_pixel, j / factor)

            result.putpixel((j, i), math.rgb_color_lerp(prev_row_number, upper_pseudo_pixel, next_row_number, lower_pseudo_pixel, i / factor))

    return result


def decimation_downsampling(image, factor):
    is_image = isinstance(image, Image.Image)

    if not is_image:
        raise TypeError(f"Object passed to function has type {image.__class__}."
                        "Expected that it will be subclass of Image.")

    if factor == 1:
        return image.copy()

    is_natural = isinstance(factor, int) and factor > 0

    if not is_natural:
        raise ValueError(f"Passed upsampling factor {factor} is not natural but natural expected.")

    result_width = image.width // factor
    result_height = image.height // factor
    result = Image.new(image.mode, (result_width, result_height))

    iterator = 0
    for i in range(image.height - factor + 1):
        if i % factor != 0:
            continue

        for j in range(image.width - factor + 1):
            if j % factor != 0:
                continue

            col = iterator % result_width
            row = iterator // result_width
            result.putpixel((col, row), image.getpixel((j, i)))
            iterator += 1

    return result
