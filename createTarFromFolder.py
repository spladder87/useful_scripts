import os
import tarfile

all_files = os.listdir()

for folder in all_files:
    if os.path.isdir(folder):
        if folder == "DIAB":
            continue
        print(folder)
        tar = tarfile.open(f"{folder}.tar", "w")
        tar.add(folder)
        tar.close()

