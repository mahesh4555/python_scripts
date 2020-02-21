import os
#given a directory path
#this code will walk through all the sub-directories and delete the files inside it

for dirpath, dirnames, files in os.walk('/home/Downloads/new'):
    
    print("Curr_dirpath") 
    print(dirpath)
    curr_dir = dirpath

    print("Sub-directories")
    for sub_dir in dirnames:
        print("sub_dir")
        print(sub_dir) 

    print("Files")
    for file in files:   
        print(file)
        filepath=curr_dir+"/"+file
        print("filepath")
        print(filepath) 
        os.remove(filepath)


