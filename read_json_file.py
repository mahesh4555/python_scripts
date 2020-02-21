import json
#read and write into a json file

#default, in read mode('r')
f=open("device.txt")

print("opened")
readings = json.load(f)
readings['update_type']='hello'
f.close()
print(readings)


f=open("device.txt","w")

print("opened")
json.dump(readings,f)
print(readings)
