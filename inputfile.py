import os

def isValidDir(a):
    return os.path.isdir(a)


def collectInputPaths():
    try:
        num_folders_to_sort = abs(int(input("How many folders would you like to sort: ")))
    except ValueError:
        print("Program is expecting a number....")
        exit()

    check_directories = []
    print("please input the directories line by line.\n To exit please enter n ")
    check_dir_count = 0
    while check_dir_count < num_folders_to_sort:
        directory = input(f" Please enter the path {check_dir_count}: ")
        if directory == "n": break
        if isValidDir(directory):
            check_directories.append(directory);
            check_dir_count += 1
        else:
            print("Invalid Directory path, please enter a correct one, or press n to exit")
    return check_directories
