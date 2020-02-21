
import json

def main(string):

 
    print(string)
  
    res = json.loads(string) 
    print (type(res)) 

    for lis in res:
        print("for loop")
        print(lis)
        for st in lis:
            print(st)











