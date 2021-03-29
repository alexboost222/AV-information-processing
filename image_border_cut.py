from folder_helper import IMAGES_FOLDER_NAME
from PIL import Image
from core.grayscale.grayscale import mean_grayscale

image_format = 'png'
image_names = 'AΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'

alphabet_folder_name = 'greek_alphabet_uppercase'
alphabet_folder_path = f'{IMAGES_FOLDER_NAME}/{alphabet_folder_name}'

for image_name in image_names:
    image_path = f'{alphabet_folder_path}/{image_name}.{image_format}'
    image = Image.open(image_path).convert('RGB')
    grayscaled = mean_grayscale(image)

    empty_row_numbers = []
    empty_column_numbers = []

    for x in range(grayscaled.width):
        row_is_empty = True
        for y in range(grayscaled.height):
            if grayscaled.getpixel((x, y)) != 255:
                row_is_empty = False
                break

        if row_is_empty:
            empty_column_numbers.append(x)

    for y in range(grayscaled.height):
        row_is_empty = True
        for x in range(grayscaled.width):
            if grayscaled.getpixel((x, y)) != 255:
                row_is_empty = False
                break

        if row_is_empty:
            empty_row_numbers.append(y)

    result = Image.new('L', (grayscaled.width - len(empty_column_numbers), grayscaled.height - len(empty_row_numbers)))

    t = 0
    for x in range(grayscaled.width):
        if x in empty_column_numbers:
            continue
        for y in range(grayscaled.height):
            if y in empty_row_numbers:
                continue

            result_col_number = t // result.height
            result_row_number = t % result.height

            result.putpixel((result_col_number, result_row_number), grayscaled.getpixel((x, y)))
            t += 1

    result.save(image_path)
