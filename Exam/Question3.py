
lower=int(input("enter the lower limit"))
upper=int(input("enter the upper limit"))
flag=0
for i in range(2,lower//2+1):
    if(lower%i==0):
        flag=flag+1
        break
if(flag==0 & lower !=1):
 print(lower)

