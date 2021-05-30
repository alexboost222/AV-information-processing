from PIL import Image

from core.sampling.sampling import expand_with_white
from core.verification import verification


def draw_profiles(image: Image) -> Image:
    verification.verify_is_image_or_exception(image)

    result = expand_with_white(image=expand_with_white(image=image, where='to_left', size=30), where='to_bottom', size=30)

    return result
