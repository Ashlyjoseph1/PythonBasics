num1=int(input("enter number1"))
num2=int(input("enter number2"))
num3=int(input("enter number3"))

if(num1>num2 & num2>num3):
    print("largest number is",num2)
elif(num1>num2 & num3>num1):
    print("largest number is",num1)
else:
    print("largest number is",num3)