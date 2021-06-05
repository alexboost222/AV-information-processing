IMAGES_FOLDER_NAME = 'images'
REPORTS_FOLDER_NAME = 'reports'
RESOURCES_FOLDER_NAME = 'resources'

RESOURCES_FOLDER_PATH = f'./{RESOURCES_FOLDER_NAME}'
IMAGES_FOLDER_PATH = f'{RESOURCES_FOLDER_PATH}/{IMAGES_FOLDER_NAME}'


def image_path(image_name, image_format):
    return f'../{IMAGES_FOLDER_NAME}/{image_name}.{image_format}'
