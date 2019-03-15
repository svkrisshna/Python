import json
json = json.loads(open('D:/requirements', 'r').read())
#value = json['ip']
#print(value)



# print the keys and values
for key in json:
    value = json[key]
    print("{}".format(value))
    f = open('requirements.txt','a')
    f.write(str(value))
    f.write("\n")
    f.close()


import os
import subprocess
#subprocess.call('start', shell = True)
os.system('pip install -r requirements.txt')
