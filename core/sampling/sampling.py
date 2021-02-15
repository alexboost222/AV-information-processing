from PIL import Image
from core.math import math
from core.verification import verification

# TODO change order of for cycles from height; width to width; height


# TODO extract different scripts for different modes like RGB etc
def closest_neighbor_upsampling(image, factor):
    verification.verify_is_image_or_exception(image)

    if factor == 1:
        return image.copy()

    verification.verify_is_natural_or_exception(factor)

    result_width = image.width * factor
    result_height = image.height * factor
    result = Image.new(image.mode, (result_width, result_height))

    for i in range(result_height):
        y_nearest = int(i * image.height / result_height)
        for j in range(result_width):
            x_nearest = int(j * image.width / result_width)
            result.putpixel((j, i), image.getpixel((x_nearest, y_nearest)))

    return result


# TODO solve problem with black left and lower borders
def bilinear_interpolation_upsampling(image, factor):
    verification.verify_is_image_or_exception(image)

    if factor == 1:
        return image.copy()

    verification.verify_is_natural_or_exception(factor)

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


# TODO solve problem with dropping factor - 1 pixels from right and lower borders
def decimation_downsampling(image, factor):
    verification.verify_is_image_or_exception(image)

    if factor == 1:
        return image.copy()

    verification.verify_is_natural_or_exception(factor)

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


def one_pass_resampling(image, upsample_factor, downsample_factor):
    verification.verify_is_image_or_exception(image)

    verification.verify_is_natural_or_exception(upsample_factor)
    verification.verify_is_natural_or_exception(downsample_factor)

    if upsample_factor == downsample_factor:
        return image.copy()

    result_width = image.width * upsample_factor // downsample_factor
    result_height = image.height * upsample_factor // downsample_factor
    result = Image.new(image.mode, (result_width, result_height))

    for i in range(result_width):
        for j in range(result_height):
            result.putpixel((i, j), image.getpixel((i * downsample_factor // upsample_factor, j * downsample_factor / upsample_factor)))

    return result
