from typing import Dict, List
import os
import shutil
from normalize import normalize


DESTINATION: Optional(str) = None

ARCHIVES = "archives"
UNKNOWN = "unknown"

CATEGORIES: Dict[str, List] = {
    "images": ['jpeg', 'png', 'jpg', 'svg'],
    "videos": ['avi', 'mp4', 'mov', 'mkv'],
    "documents": ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'],
    "music": ['mp3', 'ogg', 'wav', 'amr'],
    "archives": ['zip', 'gz', 'tar'],
    "unknowns": [],
    }


def define_category(file_path: str):
    global CATEGORIES
    extension = file_path.split(".")[-1]
    for category, category_extensions in CATEGORIES.items():
        if extension in category_extensions:
            return category
    CATEGORIES[UNKNOWN].append(extension)
    return UNKNOWN


def unpack_archive(archive_src: str, destination_folder: str):
    shutil.unpack_archive(archive_src, destination_folder)


def move_to_category_folder(src: str, destination: str):
    category = define_category(src)
    destination_folder: str = os.path.join(destination, category)  # - /target/images
    if category == ARCHIVES:
        unpack_archive(src, destination_folder)
        return

    filename = os.path.split(src)  # /target/some_subfolder/image.jpeg
    new_filename = normalize(filename.split(".")[-1])  # => zobrazenna.jpeg
    destination_filepath = os.path.join(destination_folder, new_filename)  # target/images/zobrazenna.jpeg
    shutil.move(src, destination_filepath)


def arrange_folder(target_path: str, destination_folder: str = None):
    if destination_folder is None:
        destination_folder = target_path

    inner_files = os.listdir(target_path)
    for filename in inner_files:
        file_path: str = os.path.join(target_path, filename)

        if os.path.isdir(file_path):
            arrange_folder(file_path)

        elif os.path.isfile(file_path):
            move_to_category_folder(file_path)

        else:
            raise OSError

