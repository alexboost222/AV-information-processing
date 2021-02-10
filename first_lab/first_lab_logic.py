from PIL import Image
from random import sample as random_sample


def closest_neighbor_upsampling(image, to_width, to_height):
    is_image = isinstance(image, Image.Image)

    if not is_image:
        raise TypeError(f"Object passed to function has type {image.__class__}."
                        "Expected that it will be subclass of Image.")

    if image.width > to_width:
        raise ValueError(f"Passed image width {image.width} > to_width {to_width}, but <= expected.")

    if image.height > to_height:
        raise ValueError(f"Passed image height {image.height} > to_height {to_height}, but <= expected.")

    new_pixels = [None for _ in range(to_width * to_height)]

    for i in range(to_height):
        y_nearest = int(i * image.height / to_height)
        for j in range(to_width):
            x_nearest = int(j * image.width / to_width)
            new_pixels[i * to_width + j] = image.getpixel((x_nearest, y_nearest))

    result = Image.new(image.mode, (to_width, to_height))
    result.putdata(new_pixels)

    return result


def decimation_downsampling(image, to_width, to_height):
    is_image = isinstance(image, Image.Image)

    if not is_image:
        raise TypeError(f"Object passed to function has type {image.__class__}."
                        "Expected that it will be subclass of Image.")

    if image.width < to_width:
        raise ValueError(f"Passed image width {image.width} < to_width {to_width}, but >= expected.")

    if image.height < to_height:
        raise ValueError(f"Passed image height {image.height} < to_height {to_height}, but >= expected.")

    new_pixels = [None for _ in range(to_width * to_height)]
    decimated_lines = random_sample(range(image.height), image.height - to_height)
    decimated_columns = random_sample(range(image.width), image.width - to_width)

    iterator = 0
    for i in range(image.height):
        if i in decimated_lines:
            continue

        for j in range(image.width):
            if j in decimated_columns:
                continue

            new_pixels[iterator] = image.getpixel((i, j))
            iterator += 1

    result = Image.new(image.mode, (to_width, to_height))
    result.putdata(new_pixels)

    return result


def upsample_integer_number_of_times(image, k):
    is_image = isinstance(image, Image.Image)

    if not is_image:
        raise TypeError(f"Object passed to function has type {image.__class__}."
                        "Expected that it will be subclass of Image.")

    if not isinstance(k, int):
        raise TypeError(f"Object passed to function has type {k.__class__}."
                        "Expected that it will be int.")

    if k < 1:
        raise TypeError(f"Param k passed to method has value {k} < 1. Expected >= 1.")

    return closest_neighbor_upsampling(image, image.width * k, image.height * k)


def downsample_integer_number_of_times(image, n):
    is_image = isinstance(image, Image.Image)

    if not is_image:
        raise TypeError(f"Object passed to function has type {image.__class__}."
                        "Expected that it will be subclass of Image.")

    if not isinstance(n, int):
        raise TypeError(f"Object passed to function has type {n.__class__}."
                        "Expected that it will be int.")

    if n < 1:
        raise TypeError(f"Param n passed to method has value {n} < 1. Expected >= 1.")

    return decimation_downsampling(image, image.width // n, image.height // n)


image_path = 'images/eye.png'
resized_image_path = 'images/eye_resized.png'

new_width = 100
new_height = 100

up_coef = 3
down_coef = 2

im = Image.open(image_path)
resized_im = downsample_integer_number_of_times(upsample_integer_number_of_times(im, up_coef), down_coef)
resized_im.save(resized_image_path)
