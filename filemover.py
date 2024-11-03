import os

from PIL import Image
from inputfile import isValidDir

def get_date_taken(path):
    with Image.open(path) as img:
        exif = img.getexif()
        if not exif:
            return False
        return exif.get(36867)

def MoveFilesMover(year_of_the_picture,item_path,item):
    if year_of_the_picture:
        year_folder_path = os.path.join(file_path, str(year_of_the_picture))
        if isValidDir(year_folder_path):
            os.replace(item_path, os.path.join(year_folder_path, item))
        else:
            os.makedirs(year_folder_path)
            os.replace(item_path, os.path.join(year_folder_path, item))
    elif not year_of_the_picture:
        no_year_folder_path = os.path.join(file_path, "NoDate")
        if isValidDir(no_year_folder_path):
            os.replace(item_path, os.path.join(no_year_folder_path, item))
        else:
            os.makedirs(no_year_folder_path)
            os.replace(item_path, os.path.join(no_year_folder_path, item))

def moveFilesToYears(file_path):
    items_in_dir = os.listdir(file_path)
    for item in items_in_dir:
        item_path = os.path.join(file_path, item)
        if isValidDir(item_path):
            continue
        else: # need to handle the files and non-media files before moving lets see
            year_of_the_picture = get_date_taken(item_path)
            MoveFilesMover(year_of_the_picture, item_path, item)
