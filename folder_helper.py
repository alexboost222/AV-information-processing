IMAGES_FOLDER_NAME = 'images'
REPORTS_FOLDER_NAME = 'reports'
PROJECTIONS_FOLDER_NAME = 'projections'


def image_path(image_name, image_format):
    return f'../{IMAGES_FOLDER_NAME}/{image_name}.{image_format}'
