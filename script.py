import os
import glob

count = 0
while (count < 1):
    input = raw_input("use "'">h"'" for help: ")
    line = input.split( )
    if line[0] == ">h":
        print(">a [tag] all                               add tag to all filenames in directory \n>a [tag] [filename1], [filename2], etc.    add tag to selected filenames \n>ra [tag] all                              remove tag from all filenames in directory \n>ra [tag] [filename1], [filename2], etc.   remove tag from selected filenames \n>rd                                        read directory \n>s                                         scan directory \n>se [tag]                                  search directory\n>w                                         write directory \n>x                                         exit program")

    # add tag to all filenames in directory
    elif len(line) >= 3 and line[0] == ">a" and len(line[1]) > 0 and line[2] == "all":
        path = os.path.dirname(os.path.realpath(__file__))

        with open(path + 'testfile.txt') as f:
            first_line = f.readline()
        os.chdir(first_line)
        formats = ["*.tif", "*.tiff", "*.gif", "*.jpeg", "*.jpg", "*.jif", "*.jfif", "*.jp2", "*.jpx", "*.j2k", "*.j2c", "*.fpx", "*.pcd", "*.png", "*.pdf"]
        for i in range(len(formats)):
            for file in glob.glob(formats[i]):
                os.rename(file, line[1] + file)

    # add tag to selected filenames
    elif len(line) >= 3 and line[0] == ">a" and len(line[1]) > 0 and len(line[2]) > 0:
        path = os.path.dirname(os.path.realpath(__file__))

        with open(path + 'testfile.txt') as f:
            first_line = f.readline()
        os.chdir(first_line)
        formats = ["*.tif", "*.tiff", "*.gif", "*.jpeg", "*.jpg", "*.jif", "*.jfif", "*.jp2", "*.jpx", "*.j2k", "*.j2c", "*.fpx", "*.pcd", "*.png", "*.pdf"]
        arr = []
        for i in range(len(formats)):
            for file in glob.glob(formats[i]):
                arr.append(file)
        for i in range(len(line)):
            for j in range(len(arr)):
                if line[i] == arr[j]:
                    os.rename(line[i], line[1] + line[i])

    # remove tag from all filenames in directory
    elif len(line) >= 3 and line[0] == ">ra" and len(line[1]) > 0 and line[2] == "all":
        path = os.path.dirname(os.path.realpath(__file__))

        with open(path + 'testfile.txt') as f:
            first_line = f.readline()
        os.chdir(first_line)
        formats = ["*.tif", "*.tiff", "*.gif", "*.jpeg", "*.jpg", "*.jif", "*.jfif", "*.jp2", "*.jpx", "*.j2k", "*.j2c", "*.fpx", "*.pcd", "*.png", "*.pdf"]
        for i in range(len(formats)):
            for file in glob.glob(formats[i]):
                pendingTag = file.replace(line[1], "")
                os.rename(file, pendingTag)

    # remove tag from selected filenames
    elif len(line) >= 3 and line[0] == ">ra" and len(line[1]) > 0 and len(line[2]) > 0:
        path = os.path.dirname(os.path.realpath(__file__))

        with open(path + 'testfile.txt') as f:
            first_line = f.readline()
        os.chdir(first_line)
        formats = ["*.tif", "*.tiff", "*.gif", "*.jpeg", "*.jpg", "*.jif", "*.jfif", "*.jp2", "*.jpx", "*.j2k", "*.j2c", "*.fpx", "*.pcd", "*.png", "*.pdf"]
        arr = []
        for i in range(len(formats)):
            for file in glob.glob(formats[i]):
                arr.append(file)
        for i in range(len(line)):
            for j in range(len(arr)):
                if line[i] == arr[j]:
                    pendingTag = line[i].replace(line[1], "")
                    os.rename(line[i], pendingTag)

    # read directory
    elif line[0] == ">rd":
        path = os.path.dirname(os.path.realpath(__file__))

        file = open(path + "testfile.txt", "r") 
        print file.read()
        file.close()

    # scan directory
    elif line[0] == ">s":
        path = os.path.dirname(os.path.realpath(__file__))

        with open(path + 'testfile.txt') as f:
            first_line = f.readline()
        os.chdir(first_line)
        formats = ["*.tif", "*.tiff", "*.gif", "*.jpeg", "*.jpg", "*.jif", "*.jfif", "*.jp2", "*.jpx", "*.j2k", "*.j2c", "*.fpx", "*.pcd", "*.png", "*.pdf"]
        print("READING IMAGE FILES IN " + first_line)
        for i in range(len(formats)):
            for file in glob.glob(formats[i]):
                print(file)

    # search directory
    elif len(line) >= 2 and line[0] == ">se" and len(line[1]) > 0:
        path = os.path.dirname(os.path.realpath(__file__))

        with open(path + 'testfile.txt') as f:
            first_line = f.readline()
        os.chdir(first_line)
        formats = ["*.tif", "*.tiff", "*.gif", "*.jpeg", "*.jpg", "*.jif", "*.jfif", "*.jp2", "*.jpx", "*.j2k", "*.j2c", "*.fpx", "*.pcd", "*.png", "*.pdf"]
        for i in range(len(formats)):
            for file in glob.glob(formats[i]):
                if line[1] in file:
                    print(file)

    # write directory
    elif line[0] == ">w":
        path = os.path.dirname(os.path.realpath(__file__))

        file = open(path + "testfile.txt","w")
        dir = raw_input("enter new directory: ")
        file.write(dir)
        file.close()

    # exit program
    elif line[0] == ">x":
        count += 1
quit()