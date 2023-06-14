"""
Created by Luke Schultz
Created on June 12, 2023
Last Modified on June 14, 2023
"""

import os
import sys
import copy

VERBOSE = True

def get_file_paths(directory):
    """

    """

    if VERBOSE:
        print("running get_file_paths() on the", directory, "directory...")

    file_paths = []
    directories = []  # list of all directories

    dirs = [directory]  # list of directories to search
    while (len(dirs) != 0):
        current_dir = dirs.pop()

        for entry in os.scandir(current_dir):
            if entry.is_dir():
                dirs.append(entry.path)
                directories.append(entry.path)
            else:
                file_paths.append(entry.path)

                if VERBOSE:
                    print("found:", entry.path)

    return file_paths, directories

def get_corrected_file_paths(file_paths):
    corrected_paths = copy.copy(file_paths)

    for i in range(len(file_paths)):
        corrected_paths[i] = corrected_paths[i].replace(" ", "_")
        corrected_paths[i] = corrected_paths[i].replace("(", "\(")
        corrected_paths[i] = corrected_paths[i].replace(")", "\)")
        if VERBOSE:
            print("corrected '" + str(file_paths[i]) + "' to '"
                  + str(corrected_paths[i]) + "'")

    return corrected_paths

def correct_file_paths(original_paths, correct_paths):

    assert(len(original_paths) == len(correct_paths))

    for i in range(len(original_paths)):

        if original_paths[i] == correct_paths[i]:
            continue

        command = ("mv " + original_paths[i].replace(" ", "\ ")
                                            .replace("(", "\(")
                                            .replace(")", "\)")
                   + " " + correct_paths[i])
        print(command)
        os.system(command)

if __name__=="__main__":
    file_paths, directories = get_file_paths(sys.argv[1])
    corrected_paths = get_corrected_file_paths(file_paths)
    corrected_directories = get_corrected_file_paths(directories)
    correct_file_paths(file_paths, corrected_paths)
