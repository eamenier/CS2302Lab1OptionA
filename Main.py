import os
import random


def get_dirs_and_files(path):
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + './' + directory)]
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + './' + directory)]

    return dir_list, file_list


def classify_pic(path):
    # To be implemented by Diego: Replace with ML model
    if "dog" in path:
        return 0.5 + random.random() / 2

    return random.random() / 2


def process_dir(path):

    dir_list, file_list = get_dirs_and_files(path)

    cat_list = []
    dog_list = []
    


    # Your code goes here
    # traverse through directory and files
    for root, dirs, files in os.walk(path):
        # populate directory list
        for i in dirs:
            dir_list.append(i)
        # populate files list
        for i in files:
            #ignore files if they aren't Jpeg
            if i.endswith('jpg'):
                file_list.append(i)
    # populate dog and cat lists
    for i in range(len(file_list)):
        # if picture includes dog
        if classify_pic(file_list[i]) >= 0.5:
            dog_list.append(file_list[i])
        # if picture includes cat
        else:
            cat_list.append(file_list[i])
    # test to find out if dog/cat lists are correct
    print(dog_list)
    print(cat_list)
    return cat_list, dog_list

def main():
    start_path = './' # current directory

    process_dir(start_path)


main()

