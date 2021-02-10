from PIL import Image


def closest_neighbor_interpolation(image, to_width, to_height):
    image_type = type(image)
    is_image = issubclass(image_type, type(Image))

    if is_image:
        raise TypeError(f"Object passed to function has type {image_type}. Expected that it will be subclass of Image")

    if image.width > to_width:
        raise ValueError(f"Passed image width {image.width} > to_width {to_width}, but <= expected")

    if image.height > to_height:
        raise ValueError(f"Passed image height {image.height} > to_height {to_height}, but <= expected")

    new_pixels = [None for _ in range(to_width * to_height)]

    for i in range(to_height):
        y_nearest = int(i * image.height / to_height)
        for j in range(to_width):
            x_nearest = int(j * image.width / to_width)
            new_pixels[i * to_width + j] = (image.getpixel((x_nearest, y_nearest)))

    result = Image.new(image.mode, (to_width, to_height))
    result.putdata(new_pixels)

    return result


image_path = 'images/5x5.png'
resized_image_path = 'images/5x5_resized.png'

new_width = 735
new_height = 61

im = Image.open(image_path)
resized_im = closest_neighbor_interpolation(im, new_width, new_height)
resized_im.save(resized_image_path)
