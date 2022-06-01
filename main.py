from pathlib import Path
import sys
import os
import random

extensions = ["txt", "docx", "jpg", "jpeg", "png", "ppt", "pptx", "mp3", "ogg", "wav", "flac", "m4a", "mp4", ""]


def execute(inp_path: str):
    path = Path(inp_path)

    if path.is_dir():
        for file in path.iterdir():
            if file.is_file():
                directory = str(file.absolute())
                dir_ext = directory.split('.')

                random_number = random.randint(0, len(extensions) - 1)
                while extensions[random_number] == dir_ext[1]:
                    random_number = random.randint(0, len(extensions) - 1)
                new_extension = extensions[random_number]

                new_directory = dir_ext[0] + "." + new_extension
                print(new_directory)
                os.rename(file.absolute(), new_directory)
            else:
                print(file.name)
    else:
        print("ERR: Not a valid directory")


if len(sys.argv) >= 2:
    execute(sys.argv[1])
else:
    print("Usage: main.py {DIRECTORY NAME}")
