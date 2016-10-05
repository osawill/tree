#!/usr/bin/env python3
import subprocess
import sys
# Directory tools
from os import listdir, walk, sep
from os.path import dirname, basename, isdir

itemsLeft = []
START = ""
totalDir = 0
totalFile = 0


# Recursive function
def printDir(root, level=0, last=False, parent=0):
    numDir = 0
    numFil = 0
    items = listdir(root)
    items.sort()
    if(level == 0):  # root directory
        print(root)
        if(root[-1] == '/'):  # Remove last slash to avoid inconsistencies
            root = root[:-1]
    else:  # subdirectories
        numDir += 1
        # Check if we're in the last folder of the parent directory
        if(last):
            print(("   " * (parent - 1)) + ("|   " * (level - parent - 1)) + '`-- ' + basename(root))
        else:
            print(("   " * (parent)) + ("|   " * (level - parent - 1)) + '|-- ' + basename(root))

    for idx, item in enumerate(items):
        item = root + '/' + item
        # Set flag for last file in directory
        if (idx == len(items) - 1):
            flag = True
            if(isdir(item)):
                parent = level + 1
        else:
            flag = False

        if(isdir(item)):
            (a, b) = printDir(item, level + 1, flag, parent)
            numDir += a
            numFil += b
        else:
            printFile(item, level, flag, parent)
            numFil += 1

    return (numDir, numFil)


def printFile(fil, level, last=False, lastLvl=0):
    # Print out files
    # Add correct spacing
    spacing = ("   " * lastLvl) + ('|   ' * (level - lastLvl))
    # Print filenames
    if(last):
        indent = spacing + '`-- '
    else:
        indent = spacing + '|-- '
    print(indent + basename(fil))


if __name__ == '__main__':
    # just for demo
    if(len(sys.argv) > 1):
        START = sys.argv[1]
    else:
        START = '.'
    (totalDir, totalFile) = printDir(START)
    print()
    print(str(totalDir) + " directories, " + str(totalFile) + " files")
