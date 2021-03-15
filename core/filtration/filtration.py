from PIL import Image
from core.verification.verification import verify_is_image_or_exception
from statistics import mean


# Assumes that image has 'L' mode (grayscale)
def spatial_smoothing(image):
    verify_is_image_or_exception(image)

    result = Image.new(image.mode, (image.width, image.height))

    for x in range(1, result.width - 1):
        for y in range(1, result.height - 1):
            window = list()
            for i in range(3):
                for j in range(3):
                    window.append(image.getpixel((x + i - 1, y + j - 1)))

            result.putpixel((x, y), int(round(mean(window))))

    return result


# Assumes that image has 'L' mode (grayscale)
def spatial_smoothing_difference(image):
    verify_is_image_or_exception(image)

    spatial_smoothed = spatial_smoothing(image)
    result = Image.new(image.mode, (image.width, image.height))

    for x in range(result.width):
        for y in range(result.height):
            result.putpixel((x, y), abs(image.getpixel((x, y)) - spatial_smoothed.getpixel((x, y))))

    return result


# Assumes that image has 'L' mode (grayscale)
def roberts_cross(image):
    verify_is_image_or_exception(image)

    result = Image.new(image.mode, (image.width, image.height))

    for x in range(result.width - 1):
        for y in range(result.height - 1):
            gradient_x = abs(image.getpixel((x, y)) - image.getpixel((x + 1, y + 1)))
            gradient_y = abs(image.getpixel((x + 1, y)) - image.getpixel((x, y + 1)))
            gradient = int(round((gradient_x ** 2 + gradient_y ** 2) ** 0.5))
            result.putpixel((x, y), gradient)

    return result


# Assumes that image has 'L' mode (grayscale)
def roberts_cross_difference(image):
    verify_is_image_or_exception(image)

    roberts_crossed = roberts_cross(image)
    result = Image.new(image.mode, (image.width, image.height))

    for x in range(result.width - 1):
        for y in range(result.height - 1):
            result.putpixel((x, y), abs(image.getpixel((x, y)) - roberts_crossed.getpixel((x, y))))

    return result
