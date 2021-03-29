from folder_helper import IMAGES_FOLDER_NAME
from PIL import Image
from core.grayscale.grayscale import mean_grayscale
from core.sampling.sampling import cut_empty_rows_and_cols

image_format = 'png'
image_names = 'AΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'

alphabet_folder_name = 'greek_alphabet_uppercase'
alphabet_folder_path = f'{IMAGES_FOLDER_NAME}/{alphabet_folder_name}'

for image_name in image_names:
    image_path = f'{alphabet_folder_path}/{image_name}.{image_format}'
    image = Image.open(image_path).convert('RGB')
    grayscaled = mean_grayscale(image)

    cut_empty_rows_and_cols(grayscaled, 0, 254).save(image_path)
