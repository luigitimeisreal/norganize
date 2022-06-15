from pathlib import Path
import os
import random

extensions = ["txt", "docx", "jpg", "jpeg", "png", "ppt", "pptx", "mp3", "ogg", "wav", "flac", "m4a", "mp4", ""]
banned_extensions = ["py", "exe", "md"]


def execute(inp_path: str):
    path = Path(inp_path)

    if path.is_dir():
        for file in path.iterdir():
            if file.is_file():
                filename = str(file.absolute())

                # Separate the extension from the path/name of the file
                dir_ext = filename.split('.')
                old_directory = dir_ext[0]
                old_extension = dir_ext[1]

                # Creates a random index for selecting a random extension
                random_index = random.randint(0, len(extensions) - 1)
                # Checks if the extension is different and if not it keeps searching for a random extension
                while extensions[random_index] == old_extension:
                    random_index = random.randint(0, len(extensions) - 1)
                new_extension = extensions[random_index]

                # Finally, it renames the file
                new_directory = f"{old_directory}.{new_extension}"
                print(new_directory)
                if old_extension not in banned_extensions:
                    os.rename(file.absolute(), new_directory)
            else:
                # Here will go the code for handling directories
                print(file.name)
    else:
        print("ERR: Not a valid directory")


if __name__ == "__main__":
    execute(os.getcwd())
