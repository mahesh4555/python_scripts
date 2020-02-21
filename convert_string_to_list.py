
import json

string ='[["/home/Documents/device_diag/new_scripts/","http://192.168.0.122:8000/a.py",\
"replace"], ["/home/Documents/device_diag/new_scripts/","http://192.168.0.122:8000/a.py",\
"new"]]'

def main(string):

 
    print(string)
  
    res = json.loads(string) 
    print (type(res)) 


    print(res)
    for lis in res:
        print(lis)
        for st in lis:
            print(st)












if __name__ == "__main__":
   # main('[["//lis/t1","l//i:st2:900"],["list3","list4"]]')
    ''' 
    filepath= "/home/pi/Documents/device_diag/new_scripts/"
    file_url='http://192.168.0.122:8000'
    operation='replace'
    '[["/home/pi/Documents/device_diag/new_scripts/"],
file_url='http://192.168.0.122:8000'
    operation='replace'
    list1=[filepath,file_url,operation]
    list2=[filepath,file_url,operation]
    updates_list=[list1,list2]
    updates_string=str(updates_list)
    updates_string1=str(list1)
    main(updates_string1)
    '''
    main('[["/home/pi/Documents/device_diag/new_scripts/","http://192.168.0.122:8000/a.py",\
"replace"], ["/home/pi/Documents/device_diag/new_scripts/","http://192.168.0.122:8000/a.py",\
"new"]]')
