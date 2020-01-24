#!/usr/bin/python3


##
## CODE-WORKING
## 
## Working on Code
##


import os
import fnmatch


def FolderLoop(startDir):
    # https://stackoverflow.com/questions/30444105/better-way-to-find-absolute-paths-during-os-walk
    for path, dirs, files in os.walk(startDir):
        print('path=', path)
        for file in files:
            print('file=', os.path.join(path, file))    
    


def FindFiles(startDir, pattern):
    ##
    ## FindFiles
    ## Return a list of found files with path
    ##
    ## Usage:
    ##
    ## pattern = 'props.conf'
    ## startDir = '/opt/splunk/etc'
    ## foundFiles = FindFile(startDir, pattern)
    ## print(len(foundFiles))
    ## for x in foundFiles:
    ##    print(x)
    ##
    result = []

    for path, dirs, files in os.walk(startDir):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(path, name))
                ## print(os.path.join(path, name))
    return result

def ProcessFile(path):
    print("ProcessFile():", path)



def main():
    print('Call FolderLoop()')
    startDir = '/tmp'
    FolderLoop(startDir)
    print()

    print('Call FindFiles()')
    pattern = 'props.conf'
    startDir = '/opt/splunk/etc/apps'
    foundFiles = FindFiles(startDir, pattern)
    for p in foundFiles:
        ProcessFile(p)


if __name__ == "__main__":
    main()
