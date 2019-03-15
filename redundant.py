def Redundant(string):
    lis = []
    for i in string:
        if i == ')':
            dif = lis.pop()            
            ins = 0
            while dif != '(':
                ins += 1                
                dif = lis.pop()
            if ins <= 1:
                return True
        else:
            lis.append(i)
    return False

string = input("Give your input:")
if Redundant(string) == True:
    print("1")  
else:
    print("0")
