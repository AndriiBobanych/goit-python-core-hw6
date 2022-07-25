import re
import sys


CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "y", "j",
               "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "f", "h",
               "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ja", "je", "i", "ji", "g")


TRANSLITERATION_DICT = {}    # dictionary for collection of transliterations cyr: lat


for cyr, lat in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANSLITERATION_DICT[ord(cyr)] = lat
    TRANSLITERATION_DICT[ord(cyr.upper())] = lat.upper()


def normalize(name):
    # we make transliteration of cyrillic letters to latin
    translate_name = name.translate(TRANSLITERATION_DICT)
    idx = translate_name.rfind(".")
    # we change unknown symbols to "_"
    translate_name = re.sub(r'\W', '_', translate_name[0:idx]) + translate_name[idx:]
    return translate_name


if __name__ == '__main__':

    file_for_normalize = sys.argv[1]
    print(normalize(file_for_normalize))
