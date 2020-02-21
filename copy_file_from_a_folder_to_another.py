
#source_filepath =/home/Documents/hello.txt
#destination_filepath =/home/Documents_2/
def copy_file_from_a_folder_to_another(source_filepath, destination_filepath):
    print("copy file from folder called")
    print("From:", source_filepath)
    print("To:", destination_filepath)
    # retrieving filename from souce path
    dir, file_name = os.path.split(source_filepath)
    destination_filepath += file_name

    if os.path.isfile(destination_filepath):
        print("File exist", file_name)
        os.remove(destination_filepath)
        print("File deleted", file_name)
    try:
        print("copying process started")
        shutil.copyfile(source_filepath, destination_filepath)
        print("copying process completed")
        return 1
    except Exception as e:
        print("Exception occured in copy_file_from_a_folder_to_another")
        print(e)
        return 0
