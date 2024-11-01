import os

check_dir = lambda a: os.path.isdir(a)


def inputCollector():
    try:
        numOfFiles = int(input("How many folders would you like to sort: "))
    except ValueError:
        print("Program is expecting a number....")
        exit()

    filepaths = []
    print("please input the directories line by line.\n To exit please enter n ")
    currentNumOfPaths = 0
    while currentNumOfPaths < numOfFiles:
        directory = input(f" Please enter the path {currentNumOfPaths}: ")
        if directory == "n": break
        if check_dir(directory):
            filepaths.append(directory);
            currentNumOfPaths += 1
        else:
            print("Invalid Directory path, please enter a correct one, or press n to exit")
    return filepaths
