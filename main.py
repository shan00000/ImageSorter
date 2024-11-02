import os
from inputfile import check_dir

duplicates_found = 0

## currently working on it.
def newFilePath(file_name, duplicate_folder_path):
    global duplicates_found
    duplicates_found = duplicates_found + 1
    file_name, extension = file_name.split('.')
    new_file_name = file_name + "-" + f"{str(duplicates_found)}." + extension
    print(new_file_name)
    return os.path.join(duplicate_folder_path, new_file_name)


def saveDuplicates(file_path, target_dir, file_name):
    duplicate_folder_path = os.path.join(target_dir, "PossibleDuplicate")
    new_file_path = newFilePath(file_name, duplicate_folder_path)
    if check_dir(duplicate_folder_path):
        os.replace(file_path, new_file_path)
        print("Duplicate")
    else:
        os.makedirs(duplicate_folder_path)
        os.replace(file_path, new_file_path)



## somewhat done
def flattenFiles(source_dir, target_dir=None, is_sub_dir=False):
    if target_dir is None: target_dir = source_dir
    items_in_dir = os.listdir(source_dir)
    for item in items_in_dir:
        item_path = os.path.join(source_dir, item)
        if os.path.isdir(item_path):
            flattenFiles(item_path, target_dir, True)
        else:
            if is_sub_dir:
                save_path = os.path.join(target_dir, item)
                if os.path.isfile(save_path):
                    saveDuplicates(item_path, target_dir, item)
                else:
                    os.replace(item_path, save_path)
                    continue





def main():
    # move_files_to_root(filepaths[0])
    # filesinDir = getallfilenames(filepaths)
    flattenFiles(file_paths[0])



main()
