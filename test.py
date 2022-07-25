import os
from pathlib import Path

file_path = "C:\\test\\test.txt"

extension = file_path.split(".")[-1]

filename: str = os.path.split(file_path)[-1]

print(extension)
print(filename)