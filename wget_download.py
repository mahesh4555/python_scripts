
import wget

#url =http://localhost:8000/a.py
#destination_path = /home/Documents/
def file_download(url, file_destination_path):
    print("File download started")
    try:
        wget.download(url, out=file_destination_path)
        print("File download completed")
        return 1
    except Exception as e:
        print("Exception occurred in file_download")
        print(e)
        print("Problems in downloading")
        return 0
