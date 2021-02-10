from core.sampling import sampling
from PIL import Image


def upsample_integer_number_of_times(image, m):
    is_image = isinstance(image, Image.Image)

    if not is_image:
        raise TypeError(f"Object passed to function has type {image.__class__}."
                        "Expected that it will be subclass of Image.")

    if not isinstance(m, int):
        raise TypeError(f"Object passed to function has type {m.__class__}."
                        "Expected that it will be int.")

    if m < 1:
        raise TypeError(f"Param k passed to method has value {m} < 1. Expected >= 1.")

    return sampling.closest_neighbor_upsampling(image, image.width * m, image.height * m)


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

    return sampling.decimation_downsampling(image, image.width // n, image.height // n)
