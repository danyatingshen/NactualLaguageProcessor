from subprocess import call
import sys
import os, errno
import shutil, os, glob
import pathlib
        
def converting ():
    if (len(sys.argv) > 1):
        print("Error\nFormat: \n\tpython main.py your-pdf-file")
    else : 
        directoryfrom = 'PDFs'
        directoryto = 'TXTs'
        for filename in os.listdir(directoryfrom):
            file = pathlib.Path('TXTs/'+filename)
            if file.exists ():
                print (filename+" File exist")
            else:
                print (filename+" coverted")  
                call(["pdftotext", 'PDFs/'+filename])

def moveAllFilesinDir():
    srcDir = 'PDFs' 
    dstDir = 'TXTs'
    # Check if both the are directories
    if os.path.isdir(srcDir) and os.path.isdir(dstDir) :
        # Iterate over all the files in source directory
        for filePath in glob.glob('PDFs/*.txt', recursive=True):
            # Move each file to destination Directory
            try: 
                shutil.move(filePath, dstDir)
            except shutil.Error as e:
                print(filePath+" already exist in txt")
                call(["rm", filePath])
    else:
        print("srcDir & dstDir should be Directories")

def  main():
    converting()
    moveAllFilesinDir()

main()
    