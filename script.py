import os
import glob

# global "constants" available to all functions in this file
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
FORMATS = ["*.tif", "*.tiff", "*.gif", "*.jpeg", "*.jpg", 
           "*.jif", "*.jfif", "*.jp2", "*.jpx", "*.j2k", 
           "*.j2c", "*.fpx", "*.pcd", "*.png", "*.pdf"]
TESTFILE = os.path.join(SCRIPT_DIR, 'testfile.txt')
HELP = ["* to be added",
        ">a [tag] all                       add tag to all filenames in directory",
        ">a [tag] [file1], [file2], etc.    add tag to selected filenames",
        ">ra [tag] all                      remove tag from all filenames in directory",
        ">ra [tag] [file1], [file2], etc.   remove tag from selected filenames",
        ">rd                                read current directory",
        ">s                                 scan files in directory",
        ">se [tag]                          search for tag in directory",
        ">w                                 write current directory",
        ">x                                 exit program"]

def add_tag_to_all(tag):
    # you don't use the index, so just iterate through the values directly
    for fmt in FORMATS:
        for file in glob.glob(fmt):
            os.rename(file, tag + file)


def add_tag(tag, selected):
    # it's not necessary here, but if you ever DO need the index
    # use enumerate instead of range(len(x)). it returns tuples of (index, value)
    for i, fmt in enumerate(FORMATS):
        for file in glob.glob(fmt):
            # if you make a list out of the selected files you can just use 
            # the "in" operator to test if a filename is in the list
            # if you turn it into a set instead this check will happen even faster
            if file in selected:
                os.rename(file, tag + file)

def remove_tag_from_all(tag):
    for fmt in FORMATS:
        for file in glob.glob(fmt):
            withoutTag = file.replace(tag, "")
            os.rename(file, withoutTag)

def remove_tag(tag, selected):
    for i, fmt in enumerate(FORMATS):
        for file in glob.glob(fmt):
            if file in selected:
                withoutTag = file.replace(tag, "")
                os.rename(file, withoutTag)

def search_tag(tag):
    for fmt in FORMATS:
        for file in glob.glob(fmt):
            if tag in file:
                print(file)

def write_directory(path):
    with open(TESTFILE, "w") as f:
        f.write(path)

def main():
    count = 0
    while (count < 1):
        input = raw_input("use "'">h"'" for help: ")
        line = input.split( )
        if line[0] == ">h":
            for line in HELP:
                print(line)
        
        elif len(line) >= 3 and line[0] == ">a" and len(line[1]) > 0 and line[2] == "all":
            add_tag_to_all(line[1])

        elif len(line) >= 3 and line[0] == ">a" and len(line[1]) > 0 and len(line[2]) > 0:
            add_tag(line[1], line[2])

        elif len(line) >= 3 and line[0] == ">ra" and len(line[1]) > 0 and line[2] == "all":
            remove_tag_from_all(line[1])

        elif len(line) >= 3 and line[0] == ">ra" and len(line[1]) > 0 and len(line[2]) > 0:
            remove_tag(line[1], line[2])

        elif line[0] == ">rd":
            with open(TESTFILE) as f:
                for line in f:
                    print(line)

        elif line[0] == ">s":
            for i, fmt in enumerate(FORMATS):
                for file in glob.glob(fmt):
                    print(file)

        elif len(line) >= 2 and line[0] == ">se" and len(line[1]) > 0:
            search_tag(line[1])

        elif len(line) >= 2 and line[0] == ">w" and len(line[1]) > 0:
            write_directory(line[1])

        elif line[0] == ">x":
            count += 1

if __name__ == "__main__":
    # set the current working directory for the entire file
    with open(TESTFILE) as f:
        for line in f:
            os.chdir(line.strip())
            break
    
    # start the main program
    main()