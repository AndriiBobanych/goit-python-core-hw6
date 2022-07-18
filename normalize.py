import re

CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "y", "j", 
                "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "f", "h", 
                "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ja", "je", "i", "ji", "g")

TRANSLITERATION_DICT = {} # sdictionary for collection of transliterations cyr: lat

for cyr, lat in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANSLITERATION_DICT[ord(cyr)] = lat
    TRANSLITERATION_DICT[ord(cyr.upper())] = lat.upper()


def normalize(name: str) -> str:
    translate_name = name.translate(TRANSLITERATION_DICT)
    translate_name = re.sub(r'\W', '_', translate_name)     #we change unknown symbols to "_"
    return translate_name
