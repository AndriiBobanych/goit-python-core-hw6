import os.path
import sys
from cleaner import arrange_folder


def main():
    try:
        target_folder = sys.argv[1]
    except IndexError:
        print("target folder doesn't defined")
        return

    if not os.path.exists(target_folder):
        print("Not exist")
    arrange_folder(target_folder)


if __name__ == "__main__":
    main()