lst=[9,45,10,89,23,1,0,345,100,67,56]
num=int(input("entre a element"))
flag=0
for i in lst:
    if(i==num):
        flag=1
        break
if(flag>0):
    print("element found")
else:
    print("element not found")

    # linear search
    # draw back
    # complexity
    # binary search