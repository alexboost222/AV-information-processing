from PIL import Image
from core.math import math
from core.verification import verification


# TODO extract different scripts for different modes like RGB etc
def closest_neighbor_upsampling(image, factor):
    verification.verify_is_image_or_exception(image)

    if factor == 1:
        return image.copy()

    verification.verify_is_natural_or_exception(factor)

    result_width = image.width * factor
    result_height = image.height * factor
    result = Image.new(image.mode, (result_width, result_height))

    for x in range(result_width):
        x_nearest = int(x * image.width / result_width)
        for y in range(result_height):
            y_nearest = int(y * image.height / result_height)
            result.putpixel((x, y), image.getpixel((x_nearest, y_nearest)))

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

    for x in range(result_width):
        for y in range(result_height):
            if (x % factor == 0) and (y % factor == 0):
                result.putpixel((x, y), image.getpixel((x // factor, y // factor)))
                continue

            prev_row_number = y // factor
            next_row_number = prev_row_number + 1
            prev_col_number = x // factor
            next_col_number = prev_col_number + 1

            if (next_row_number >= image.height) or (next_col_number >= image.width):
                result.putpixel((x, y), (0, 0, 0))
                continue

            prev_row_prev_col_pixel = image.getpixel((prev_col_number, prev_row_number))
            prev_row_next_col_pixel = image.getpixel((next_col_number, prev_row_number))
            next_row_prev_col_pixel = image.getpixel((prev_col_number, next_row_number))
            next_row_next_col_pixel = image.getpixel((next_col_number, next_row_number))

            upper_pseudo_pixel = math.rgb_color_lerp(prev_col_number, prev_row_prev_col_pixel, next_col_number, prev_row_next_col_pixel, x / factor)
            lower_pseudo_pixel = math.rgb_color_lerp(prev_col_number, next_row_prev_col_pixel, next_col_number, next_row_next_col_pixel, x / factor)

            result.putpixel((x, y), math.rgb_color_lerp(prev_row_number, upper_pseudo_pixel, next_row_number, lower_pseudo_pixel, y / factor))

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

    for x in range(image.width - factor + 1):
        if x % factor != 0:
            continue

        for y in range(image.height - factor + 1):
            if y % factor != 0:
                continue

            result.putpixel((x // factor, y // factor), image.getpixel((x, y)))

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

    for x in range(result_width):
        for y in range(result_height):
            result.putpixel((x, y), image.getpixel((x * downsample_factor // upsample_factor, y * downsample_factor / upsample_factor)))

    return result


# Assumes that image has 'L' mode (grayscale)
def cut_empty_rows_and_cols(image, min_threshold, max_threshold):
    verification.verify_is_image_or_exception(image)

    empty_row_numbers = []
    empty_column_numbers = []

    for x in range(image.width):
        row_is_empty = True
        for y in range(image.height):
            if min_threshold <= image.getpixel((x, y)) <= max_threshold:
                row_is_empty = False
                break

        if row_is_empty:
            empty_column_numbers.append(x)

    for y in range(image.height):
        row_is_empty = True
        for x in range(image.width):
            if min_threshold <= image.getpixel((x, y)) <= max_threshold:
                row_is_empty = False
                break

        if row_is_empty:
            empty_row_numbers.append(y)

    result = Image.new(image.mode, (image.width - len(empty_column_numbers), image.height - len(empty_row_numbers)))

    t = 0
    for x in range(image.width):
        if x in empty_column_numbers:
            continue
        for y in range(image.height):
            if y in empty_row_numbers:
                continue

            result_col_number = t // result.height
            result_row_number = t % result.height

            result.putpixel((result_col_number, result_row_number), image.getpixel((x, y)))
            t += 1

    return result
