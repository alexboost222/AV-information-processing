from PIL import Image, ImageDraw, ImageFont

from core.grayscale.grayscale import mean_grayscale
from core.sampling.sampling import cut_empty_rows_and_cols

WHITE = (255, 255, 255)
RGB_MODE = 'RGB'
IMAGE_NAME = 'test.png'

image = Image.new(mode=RGB_MODE, size=(843, 52), color=WHITE)

font = ImageFont.truetype(font='../fonts/times.ttf', size=52)

result = ImageDraw.Draw(im=image, mode=RGB_MODE)

result.text(xy=(0, 0), text='AΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ', font=font, fill=0, anchor='lt')

image.save('lol.png')

image = cut_empty_rows_and_cols(mean_grayscale(image))

image.save(fp=IMAGE_NAME)

