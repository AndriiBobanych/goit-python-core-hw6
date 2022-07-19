import sys
from pathlib import Path


# we create the function for parsing the input folder
def user_folder_scan(path: Path) -> None:
    for element in path.iterdir():

        # we check if the element is folder (if "yes" - we use recursion to check sub-folder)
        if element.is_dir():
            if element.name not in ('archives', 'video', 'audio', 'documents', 'images', 'other'):
                # we use recursion to check the attached sub-folder
                user_folder_scan(element)
            else:
                continue

        # if element is "file" - we take full path to file for further handling
        extension_for_folder = get_extension(element.name)   # we use function to take suffix to create the folder later
        fullname = path / element.name   # we take full route (path) to file


# we create the function to take suffix to create the folder later
def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


if __name__ == '__main__':

    folder_for_scan = sys.argv[1]
    user_folder_scan(Path(folder_for_scan))