import os.path
import sys
from folder_sorter import arrange_files_sorting_in_folder


def main():
    try:
        target_folder = sys.argv[1]
    except IndexError:
        print("Folder for sorting was not defined. Please enter path to folder.")
        return

    if not os.path.exists(target_folder):
        print("Indicated folder doesn't exist. Please check path and start process again")
        exit()

    print(f'\nWe start file sorting process in folder -> {target_folder}\n')
    arrange_files_sorting_in_folder(target_folder)
    print(f'Sorting process in progress...\n')
    print(f"Files were sorted successfully. Please check here -> {target_folder}\n")


if __name__ == "__main__":
    main()

