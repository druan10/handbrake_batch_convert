'''
Based on --> http://www.semifluid.com/2014/04/11/batch-handbrake-video-file-conversion-with-python/
'''

import os
import time
import subprocess
import sys

fileList = []
# Set Root Dir to script location.
os.chdir(os.path.dirname(os.path.abspath(__file__)))
rootdir = './'

for root, subFolders, files in os.walk(rootdir):
    for file in files:
        theFile = os.path.join(root,file)
        fileName, fileExtension = os.path.splitext(theFile)
        if fileExtension.lower() in ('.avi', '.divx', '.flv', '.m4v', '.mkv', '.mov', '.mpg', '.mpeg', '.wmv', '.mp4'):
            print(f'Adding, {theFile}.')
            fileList.append(theFile)

runstr = '"C:/handbrake-cli/HandBrakeCLI.exe" -i "{0}" -o "{1}" --preset="Web/Vimeo YouTube HQ 720p60" --two-pass --turbo'

print('=======--------=======')

while fileList:
    inFile = fileList.pop()
    fileName, fileExtension = os.path.splitext(inFile)
    outFile = fileName+'-new.mp4'

    print(f'Processing, {inFile}')
    returncode  = subprocess.call(runstr.format(inFile,outFile))
    time.sleep(5)
    print('Renaming Original file: ',inFile)
    os.rename(inFile,fileName+'-original'+fileExtension),