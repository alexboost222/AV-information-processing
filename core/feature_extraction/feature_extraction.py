from core.verification.verification import verify_is_image_or_exception


# Assumes that image in '1' mode
def black_weight(image):
    verify_is_image_or_exception(image)

    result = 0

    for x in range(image.width):
        for y in range(image.height):
            result += image.getpixel((x, y))

    return result


# Assumes that image in '1' mode
def specific_black_weight(image):
    verify_is_image_or_exception(image)

    return black_weight(image) / (image.width * image.height)


# Assumes that image in '1' mode
def gravity_center(image):
    verify_is_image_or_exception(image)

    x_coord = 0
    y_coord = 0

    for x in range(image.width):
        for y in range(image.height):
            pixel = image.getpixel((x, y))
            x_coord += x * pixel
            y_coord += y * pixel

    weight = black_weight(image)
    return int(round(x_coord / weight)), int(round(y_coord / weight))


# Assumes that image in '1' mode
def normalized_gravity_center(image):
    verify_is_image_or_exception(image)

    x, y = gravity_center(image)

    return (x - 1) / (image.width - 1), (y - 1) / (image.height - 1)


# Assumes that image in '1' mode
def central_horizontal_axial_moment(image):
    verify_is_image_or_exception(image)

    center = gravity_center(image)
    result = 0

    for x in range(image.width):
        for y in range(image.height):
            result += (y - center[1]) ** 2 * image.getpixel((x, y))

    return result


# Assumes that image in '1' mode
def normalized_central_horizontal_axial_moment(image):
    verify_is_image_or_exception(image)

    return central_horizontal_axial_moment(image) / (image.width ** 2 + image.height ** 2)


# Assumes that image in '1' mode
def central_vertical_axial_moment(image):
    verify_is_image_or_exception(image)

    center = gravity_center(image)
    result = 0

    for x in range(image.width):
        for y in range(image.height):
            result += (x - center[0]) ** 2 * image.getpixel((x, y))

    return result


# Assumes that image in '1' mode
def normalized_central_vertical_axial_moment(image):
    verify_is_image_or_exception(image)

    return central_vertical_axial_moment(image) / (image.width ** 2 + image.height ** 2)


# Assumes that image in '1' mode
def horizontal_projection(image):
    verify_is_image_or_exception(image)

    levels = []
    projections = []

    for y in range(image.height):
        y_projection = 0
        for x in range(image.width):
            y_projection += image.getpixel((x, y))

        levels.append(y)
        projections.append(y_projection)

    return levels, projections


# Assumes that image in '1' mode
def vertical_projection(image):
    verify_is_image_or_exception(image)

    levels = []
    projections = []

    for x in range(image.width):
        x_projection = 0
        for y in range(image.height):
            x_projection += image.getpixel((x, y))

        levels.append(x)
        projections.append(x_projection)

    return levels, projections
