import os
import glob

def getDirectory():
    path = os.path.realpath(__file__).split("/")
    path.pop()
    s = "/"
    path = s.join(path)
    print(path)

count = 0
while (count < 1):
    input = raw_input("use "'">h"'" for help: ")
    line = input.split( )
    if line[0] == ">h":
        print(">a [tag] all                               add tag to all filenames in directory \n>a [tag] [filename1], [filename2], etc.    add tag to selected filenames \n>ra [tag] all                              remove tag from all filenames in directory \n>rd                                        read directory \n>s                                         scan directory \n>w                                         write directory \n>x                                         exit program")

    # add tag to all filenames in directory
    elif line[0] == ">a" and len(line[1]) > 0 and line[2] == "all":
        path = os.path.realpath(__file__).split("/")
        path.pop()
        s = "/"
        path = s.join(path)

        with open(path + 'testfile.txt') as f:
            first_line = f.readline()
        os.chdir(first_line)
        formats = ["*.tif", "*.tiff", "*.gif", "*.jpeg", "*.jpg", "*.jif", "*.jfif", "*.jp2", "*.jpx", "*.j2k", "*.j2c", "*.fpx", "*.pcd", "*.png", "*.pdf"]
        for i in range(len(formats)):
            for file in glob.glob(formats[i]):
                os.rename(file, line[1] + file)

    # remove tag from all filenames in directory
    elif line[0] == ">ra" and len(line[1]) > 0 and line[2] == "all":
        path = os.path.realpath(__file__).split("/")
        path.pop()
        s = "/"
        path = s.join(path)

        with open(path + 'testfile.txt') as f:
            first_line = f.readline()
        os.chdir(first_line)
        formats = ["*.tif", "*.tiff", "*.gif", "*.jpeg", "*.jpg", "*.jif", "*.jfif", "*.jp2", "*.jpx", "*.j2k", "*.j2c", "*.fpx", "*.pcd", "*.png", "*.pdf"]
        for i in range(len(formats)):
            for file in glob.glob(formats[i]):
                pendingTag = file.replace(line[1], "")
                os.rename(file, pendingTag)

    # read directory
    elif line[0] == ">rd":
        path = os.path.realpath(__file__).split("/")
        path.pop()
        s = "/"
        path = s.join(path)

        file = open(path + "testfile.txt", "r") 
        print file.read()
        file.close()

    # scan directory
    elif line[0] == ">s":
        path = os.path.realpath(__file__).split("/")
        path.pop()
        s = "/"
        path = s.join(path)

        with open(path + 'testfile.txt') as f:
            first_line = f.readline()
        os.chdir(first_line)
        formats = ["*.tif", "*.tiff", "*.gif", "*.jpeg", "*.jpg", "*.jif", "*.jfif", "*.jp2", "*.jpx", "*.j2k", "*.j2c", "*.fpx", "*.pcd", "*.png", "*.pdf"]
        print("READING IMAGE FILES IN " + first_line)
        for i in range(len(formats)):
            for file in glob.glob(formats[i]):
                print(file)

    # write directory
    elif line[0] == ">w":
        path = os.path.realpath(__file__).split("/")
        path.pop()
        s = "/"
        path = s.join(path)

        file = open(path + "testfile.txt","w")
        dir = raw_input("enter new directory: ")
        file.write(dir)
        file.close()

    # exit program
    elif line[0] == ">x":
        count += 1
quit()