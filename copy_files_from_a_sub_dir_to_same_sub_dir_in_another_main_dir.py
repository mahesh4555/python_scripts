# handles the incremental_updates
# move(replace or add) the files present in main1 dir to main2 dir
#main1 and main2 directories have the same directory structure, that is, it contains the same sub-directories
#If any files are present in main1 dir, it will be moved to the main2 dir


def copy_files_from_a_sub_dir_to_same_sub_dir_in_another_main_dir():
    for dirpath, dirnames, files in os.walk(mieupro_update_path):
        curr_dir = dirpath
        print("Files")
        for file in files:
            print("********************************************")
            print(file)
            src = curr_dir + "/" + file
            dest = curr_dir.replace('mieupro_update', 'mieupro') + '/'

            print("src:", src)
            print("dest:", dest)
            copy_file_from_a_folder_to_another(src, dest)
            os.remove(src)
            print("********************************************")



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
