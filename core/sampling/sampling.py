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
