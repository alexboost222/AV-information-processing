from PIL import Image, PngImagePlugin


def closest_neighbor_width_interpolation_png(image, to_width):
    image_type = type(image)
    is_image = issubclass(image_type, type(Image))

    if is_image:
        raise TypeError(f"Object passed to function has type {image_type}. Expected that it will be subclass of Image")

    if image.width > to_width:
        raise ValueError(f"Passed image width {image.width} > to_width {to_width}, but <= expected")

    gap = to_width // image.width

    new_pixels = list()

    for i in range(image.height):
        gap_iterator = 0
        last_key_pixel_number = -1
        for j in range(to_width):
            is_key_pixel = gap_iterator == 0
            is_enough_place = to_width - j >= image.width - last_key_pixel_number - 1
            last_key_pixel_number += is_key_pixel or not is_enough_place
            new_pixels.append(image.getpixel((last_key_pixel_number, i)))
            gap_iterator += 1
            gap_iterator %= gap + 1

    result = Image.new(image.mode, (to_width, image.height))
    result.putdata(new_pixels)

    return result


def closest_neighbor_height_interpolation_png(image, to_height):
    is_image = issubclass(type(image), type(Image))

    if is_image:
        raise TypeError(f"Object passed to function has type {type(image)}. Expected that it will be subclass of Image")

    if image.height > to_height:
        raise ValueError(f"Passed image height {image.height} > to_height {to_height}, but <= expected")

    gap = to_height // image.height

    new_pixels = list()

    for i in range(image.width):
        gap_iterator = 0
        last_key_pixel_number = -1
        for j in range(to_height):
            is_key_pixel = gap_iterator == 0
            is_enough_place = to_height - j >= image.height - last_key_pixel_number - 1
            last_key_pixel_number += is_key_pixel or not is_enough_place
            new_pixels.append(image.getpixel((i, last_key_pixel_number)))
            gap_iterator += 1
            gap_iterator %= gap + 1

    result = Image.new(image.mode, (image.width, to_height))
    result.putdata(new_pixels)

    return result


image_path = 'images/5x5.png'
resized_image_path = 'images/5x5_resized.png'

new_width = 934
new_height = 934

im = Image.open(image_path)
resized_im = closest_neighbor_height_interpolation_png(closest_neighbor_width_interpolation_png(im, new_width), new_height)
resized_im.save(resized_image_path)
