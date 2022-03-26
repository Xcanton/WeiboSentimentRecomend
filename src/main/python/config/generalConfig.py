import sys
import os


def readFile(filePath, type = "r", encoding = "utf-8"):
    file = open(filePath, type, encoding=encoding)
    file_text = file.read()
    file.close()

    return file_text


def returnDirSubDir(Path):
    if not os.path.exists(Path) or not os.path.isdir(Path):
        return None
    return [item for item in os.listdir(Path) if os.path.isdir(os.path.join(Path,item))]

def returnDirSubFile(Path):
    if not os.path.exists(Path) or not os.path.isdir(Path):
        return None
    return [item for item in os.listdir(Path) if os.path.isfile(os.path.join(Path,item))]