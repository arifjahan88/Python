import os

path = "D:\KDE OS\python file"

if os.path.exists(path):
    print("This is Exist!")
    if os.path.isfile(path):
        print("This is a file!")
    elif os.path.isdir(path):
        print("This is a directory!")
else:
    print("This is not Exist!")
