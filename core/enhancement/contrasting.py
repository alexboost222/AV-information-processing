from PIL import Image

from core.verification import verification


# Assumes that image has 'L' mode
def linear_contrasting(image: Image, min_brightness: int = 0, max_brightness: int = 255) -> Image:
    def calculate_brightness(f, f_min, f_max, g_min, g_max):
        return (f - f_min) / (f_max - f_min) * (g_max - g_min) + g_min

    verification.verify_is_image_or_exception(image)

    image_pixels = list(image.getdata())

    image_min_brightness = min(image_pixels)
    image_max_brightness = max(image_pixels)

    result = image.copy()

    for x in result.width:
        for y in result.height:
            brightness = calculate_brightness(result.getpixel((x, y)), image_min_brightness, image_max_brightness,
                                              min_brightness, max_brightness)
            result.setpixel((x, y), brightness)

    return result

