A = list()
length = int(input("Enter the number of elements you want: "))
print ('Enter numbers in array: ')
for i in range(int(length)):
    n = int(input("number :"))
    A.append(int(n))
print ('A: ',A)
target = int(input("Enter the target: "))

A.sort()
size = len(A)

result = 0
maxi = 10000
for i in range( 0, size - 1):
    j = i + 1
    k = size - 1
    while j < k:
        add = A[i] + A[j] + A[k]
        diff = abs(add - target)
        if(diff == 0):
            print(add)
        if(diff < maxi):
            maxi = diff
            result = add
        if(add <= target):
            j = j + 1
        else:
            k = k - 1
print(result)
