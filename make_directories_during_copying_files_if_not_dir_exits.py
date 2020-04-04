
#create directory or directories if not present while copying

def make_dirs_and_copy():
    source_filepath='main15.zip'
    destination_filepath='./mahesh/next/new/11/12/14/15'
# or destination_filepath='./mahesh/next/new/11/12/14/15/main.zip'
    print("dirname : ",os.path.dirname(destination_filepath))
    _, file= os.path.split(destination_filepath)
    print("dir:",_)
    print("file:",file)
    print("copying process started")
    try:
        shutil.copyfile(source_filepath, destination_filepath)
    except IOError as e:
        print("Exception occured and handled here")
        ########################
        os.makedirs(os.path.dirname(destination_filepath))
        ########################
        shutil.copyfile(source_filepath, destination_filepath)
    print("copying process completed")



