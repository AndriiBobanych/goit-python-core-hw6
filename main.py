from pathlib import Path
import re
import sys
import shutil
from normalize import normalize

images_ext = ('JPEG', 'PNG', 'JPG', 'SVG')
video_ext = ('AVI', 'MP4', 'MOV', 'MKV')
audio_ext = ('MP3', 'OGG', 'WAV', 'AMR')
documents_ext = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
archives_ext = ('ZIP', 'GZ', 'TAR')

folders_list = []
images_list = []
video_list = []
audio_list = []
documents_list = []
archives_list = []
unknown_list = []

extensions_set = set()
unknown_ext_set = set()


# we create the function to take suffix
def get_extension(filename):
    return Path(filename).suffix[1:].upper()


# PARSING PROCESS--------------------------------------------------------

# we create the function for parsing the input folder
def user_folder_scan(path: Path) -> None:
    for element in path.iterdir():

        # we check if the element is "folder"
        if element.is_dir():
            if element.name not in ('archives', 'video', 'audio', 'documents', 'images', 'other'):
                folders_list.append(element)
                # if "yes" - we use recursion to check the attached sub-folder
                user_folder_scan(element)
            else:
                continue

        # if element is "file":
        full_path_name = path / normalize(element.name)  # we take full route (path) to file
        file_extension = get_extension(element.name)  # we use function to take suffix to create the folder later

        if file_extension in images_ext:
            images_list.append(full_path_name)
            extensions_set.add(file_extension)

        elif file_extension in video_ext:
            video_list.append(full_path_name)
            extensions_set.add(file_extension)

        elif file_extension in audio_ext:
            audio_list.append(full_path_name)
            extensions_set.add(file_extension)

        elif file_extension in documents_ext:
            documents_list.append(full_path_name)
            extensions_set.add(file_extension)

        elif file_extension in archives_ext:
            archives_list.append(full_path_name)
            extensions_set.add(file_extension)

        else:
            unknown_list.append(full_path_name)
            unknown_ext_set.add(file_extension)


# HANDLING PROCESS --------------------------------------------------------

def handle_file(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder)


def handle_archive(filename: Path, target_folder: Path):
    # We create folder for archive
    target_folder.mkdir(exist_ok=True, parents=True)
    # We create folder for unpacking (named as archive without extension)
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()),
                              str(folder_for_file.resolve()))
    except shutil.ReadError:
        print(f'It is not archive {filename}!')
        folder_for_file.rmdir()
        return None
    filename.unlink()


def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f'Error occurs while deleting folder {folder}')


# MAIN PROCESS --------------------------------------------------------

def main_script(folder: Path):
    user_folder_scan(folder)

    for file in images_list:
        handle_file(file, folder / 'images')

    for file in video_list:
        handle_file(file, folder / 'video')

    for file in audio_list:
        handle_file(file, folder / 'audio')

    for file in documents_list:
        handle_file(file, folder / 'documents')

    for file in archives_list:
        handle_archive(file, folder / 'archives')

    for file in unknown_list:
        handle_file(file, folder / 'other')

    for folder in folders_list:
        handle_folder(folder)


# if main unit --------------------------------------------------------

if __name__ == '__main__':
    if sys.argv[1]:
        folder_for_scan = Path(sys.argv[1])
        print(f'We start in folder {folder_for_scan.resolve()}')
        main_script(folder_for_scan.resolve())
