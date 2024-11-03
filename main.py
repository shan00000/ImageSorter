import os

from filemover import moveFilesToYears
from inputfile import collectInputPaths, isValidDir
from Imageflattentool import flattenFiles





if __name__ == "__main__":
    file_paths = collectInputPaths()
    for file_path in file_paths:
        # flattenFiles(file_path)
        moveFilesToYears(file_path)


