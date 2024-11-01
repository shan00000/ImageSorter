import os
from inputfile import check_dir


## currently working on it.
def save_duplicates(file, root, filename):
    duplicate_file_path = os.path.join(root, "duplicate")
    destination = os.path.join(duplicate_file_path,filename)
    count = 0

    while os.path.isfile(destination):
        path, extension = str(destination).split(".")
        path = path + f"({count})"
        destination = path + "." + extension
        count += 1


    if check_dir(duplicate_file_path):
        os.replace(file, destination)
    else:
        os.makedirs(duplicate_file_path)
        os.replace(file, destination)


## somewhat done
def flatten_files(source_dir, target_dir=None, is_sub_dir=False):
    if target_dir is None: target_dir = source_dir
    items_in_dir = os.listdir(source_dir)
    for item in items_in_dir:
        item_path = os.path.join(source_dir, item)
        if os.path.isdir(item_path):
            flatten_files(item_path, target_dir, True)
        else:
            if is_sub_dir:
                savepath = os.path.join(target_dir, item)
                if os.path.isfile(savepath):
                    save_duplicates(savepath, target_dir, item)
                else:
                    os.replace(item_path, savepath)


## to put into files
# def getallfilenames(filepaths, diric=None):
#         for currentdir in filepaths:
#             filesavailable = os.listdir(currentdir)
#             for file in filesavailable:
#                 if os.path.isdir(file):
#
#                 else:
#                     root, extension = os.path.splitext(file)
#
#                     curentfilelocation = os.path.join(currentdir, file)
#                     filetosave = os.path.join(currentdir, extension)
#                     futurelocation = os.path.join(filetosave,file)
#
#                     if check_dir(filetosave):
#                         os.replace(curentfilelocation,futurelocation)
#                     else:
#                         os.makedirs(filetosave)
#                         os.replace(curentfilelocation, futurelocation)


def main():
    filepaths = [r"C:\Users\sr2559g\OneDrive - University of Greenwich\Pictures\Teams Backgrounds"]
    # move_files_to_root(filepaths[0])
    # filesinDir = getallfilenames(filepaths)
    flatten_files(filepaths[0])


main()
