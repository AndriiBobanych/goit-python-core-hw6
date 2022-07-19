# import argparse
import sys
from pathlib import Path
# from shutil import copyfile

# parser = argparse.ArgumentParser()
# parser.add_argument("--sourse", required=True, help="source folder")

# args = vars(parser.parse_args())
# source_folder = args.get("source")

# source_folder = sys.argv[1]


def user_folder_scan(path: Path) -> None:
    for element in path.iterdir():
        if element.is_dir():
            if element.name not in ('archives', 'video', 'audio', 'documents', 'images', 'other'):
                # we use recursion to check the attached subfolder
                user_folder_scan(element)
            else:
                continue
        
#         else:
#             copy_file_handler(element)


def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


# def copy_file_handler(file: Path):
#     new_path = source_folder / file.suffix        #
#     new_path.mkdir(exist_ok=True, parents=True)
#     copyfile(file, new_path / file.name)


if __name__ == '__main__':
    
    folder_for_scan = sys.argv[1]
    user_folder_scan(Path(folder_for_scan))