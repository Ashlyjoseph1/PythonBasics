#fibnocci sequence of a given number

number=int(input("enter the number"))
i=0
num1=0
num2=1
while(i<number):
    if(i<=1):
        next=i
    else:
        next=num1+num2
        num1=num2
        num2=next
    print(next)
    i+=1

