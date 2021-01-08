
import subprocess
cc="ipconfig"
op = subprocess.check_output(cc, shell=True)
print(op)
op2 =op.decode("utf-8")

print(op2)
print("form3t")

dict1={}
for line in op2.split('\n'):
    try:
        print(line)
        if ':' in line:
            line_f = line.split(':', 1)
            print("line_f=", line_f)
            dict1.update({line_f[0]: line_f[1]})
            # dictf = dict(line_f)
            # print("dictf=", dictf)
    except:
        print("exc")
print("dic :", dict1)


#Alternate waay of writing the same
resultDict = dict(line.split(':', 1) for line in op2.split('\n') if ':' in line)
print(resultDict)

#Same as above way with space removed
resultDict = dict(map(str.strip, line.split(':', 1)) for line in op2.split('\n') if ':' in line)
print(resultDict)
