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
