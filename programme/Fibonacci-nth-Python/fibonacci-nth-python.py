a = 0
b = 1
i = 0
n = int(input("Input: "))
while (i!=n):
    print(a,end=" ")
    temp = a
    a = b
    b = temp + b
    i+=1
