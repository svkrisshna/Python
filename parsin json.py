import json

#please change the path in the below line to the path where you saved the json(requirements) file.

json = json.loads(open('D:/requirements', 'r').read())

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
os.system('pip install -r requirements.txt')
