from pathlib import Path
import shutil
import normalize
import parser
import handler


image_group = ('JPEG', 'PNG', 'JPG', 'SVG')
video_group = ('AVI', 'MP4', 'MOV', 'MKV')
document_group = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
music_group = ('MP3', 'OGG', 'WAV', 'AMR')
archive_group = ('ZIP', 'GZ', 'TAR')


ALL_FILES = []
EXTENSIONS = set()
UNKNOWN_EXT = set()


def main(folder: Path):
    parser.user_folder_scan(folder)
    for file in parser.JPEG_IMAGES:
        handle_media(file, folder / 'images' / 'JPEG')
    for file in parser.JPG_IMAGES:
        handle_media(file, folder / 'images' / 'JPG')
    for file in parser.PNG_IMAGES:
        handle_media(file, folder / 'images' / 'PNG')
    for file in parser.SVG_IMAGES:
        handle_media(file, folder / 'images' / 'SVG')
    for file in parser.MP3_AUDIO:
        handle_media(file, folder / 'audio' / 'MP3')

    for file in parser.MY_OTHER:
        handle_other(file, folder / 'MY_OTHER')
    for file in parser.ARCHIVES:
        handle_archive(file, folder / 'archives')

    # Виконуємо реверс списку для того щоб видалити всі папки
    for folder in parser.FOLDERS[::-1]:
        handle_folder(folder)


if __name__ == '__main__':
    if sys.argv[1]:
        folder_for_scan = Path(sys.argv[1])
        print(f'Start in folder {folder_for_scan.resolve()}')
        main(folder_for_scan.resolve())
