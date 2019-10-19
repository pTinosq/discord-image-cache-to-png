import getpass
import os
from shutil import copyfile
import sys

def main():
    global discordDir
    stringpiece1 = (r"C:\Users")
    stringpiece2 = (r"AppData\Roaming\Discord")
    value=f"{stringpiece1}\{getpass.getuser()}\{stringpiece2}"
    if os.path.isdir(value):
        print("Automatically found Discord directory.")
        discordDir = value
    else:
        print("Discord directory could not be located. Please specify the location")
        
        def getDir():
            discordDir = input(r"Discord directory: ")
            if os.path.isdir(discordDir):
                print("Discord directory found!")
                return discordDir
                
            else:
                print("This directory doesn't exist. Please try again.")
                discordDir = getDir()
                return discordDir
        discordDir = getDir()
    
    print("Now that the directory has been found. I'll do some quick checks to ensure everything is where it's supposed to be.")
    input("Press any key to continue or ctrl+c to quit.")
    
    newdir = f"{discordDir}\Cache"
    if os.path.isdir(newdir):
        num=0
        for i in os.listdir(newdir):
            if str(i)[:4] == "data":
                pass
            elif str(i) == "index":
                pass
            else:
                num+=1
                print(f"Found {i}")
        print(f"Found a total of {num} images!")
        input("Enter to continue")
        print(f"\n\n\n\n\n\n")
        print(f"The next thing to do is to decide on how many of these images you want to download.")
        def allorcustom():
            print("a) All the images b) Custom number")
            a = input("a/b: ")
            if a.lower() == "a":
                return 0
            
            elif a.lower() == "b":
                return 1
            
            else:
                print("I don't understand this input.")
                input("Press enter to try again")
                val = allorcustom()
                return val
        val = allorcustom()
        if val == 0:
            images_count = num

        else:
            images_count = int(input("How many images would you like to download: "))

        if images_count > num:
            images_count = num

        input("Press enter to continue")

        print(f"\n\n\n\n\n\n\n")
        print("Next, we need to specify a directory to dump all the images into")
        print("Please create a folder and specify its location below")
        def getDirSave():
            SaveDir = input(r"Save-to directory: ")
            if os.path.isdir(SaveDir):
                print("Directory found!")
                return SaveDir
                
            else:
                print("This directory doesn't exist. Please try again.")
                SaveDir = getDirSave()
                return SaveDir
        SaveDir = getDirSave()
        print(f"\n\n\n\n\n\n\n")
        print("WARNING!")
        print("If you have specified the incorrect directory please exit the program now!")
        print("If you make any mistakes here, it'll be very hard to undo the damages")
        print("By pressing enter you agree that any damages caused by incorrect directory assignment is completely your own fault.")
        print(f"All {images_count} file(s) will be saved to: {SaveDir}")
        input("Press enter to continue the process at your own discretion or ctrl+c to exit")
        FileListArray=[]
        FileList=os.listdir(newdir)
        for i in FileList:
            if str(i)[:4] == "data":
                pass
            elif str(i) == "index":
                pass
            else:
                
                FileListArray.append(i)
                
        for i in range(int(images_count)):
            fileName = FileListArray[i]
            fileloc = f"{newdir}\{fileName}"
            newfile = f"{SaveDir}\{fileName}.png"
            print(f"Copied to {newfile}")
            try:
                copyfile(fileloc, newfile)
            except Exception as e:
                print(f"{e}")
                print(f"\nThis probably means that you didn't run as administrator so the script doesn't have permission to copy paste files.")
                input("")
                sys.exit()
            
            
        
        
    
        

    else:
        print("Error! A  cache folder doesn't exist.")
        input("Press enter to try again or ctrl+c to quit")
        main()
main()
