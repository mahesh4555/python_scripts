from zipfile import ZipFile 

  
# specifying the zip filepath 
filepath = "/home/Documents/new_scripts/main15.zip"
def zip_extract(filepath):
    print("zip_extracting : ", filepath)
    filedir, filename = os.path.split(filepath)
    # print(filedir)
    # print(filename)

    with ZipFile(filepath, 'r') as zip:
        print('Extracting all the files now...')
        print('to:', filedir)
        zip.extractall(filedir)
        print('Done!')

