from zipfile import ZipFile

#file_path="home/main/mix_old.zip"
def zip_compress(file_path):

    file_dir, file_name = split_dir_and_filename(directorypath)
    zip_name = file_name + "_old"+ ".zip"
    zf = ZipFile(file_path, "w")
    for dirname, subdirs, files in os.walk(directorypath):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()
