#create calculator
#1.Addition
#2.Substraction
#3.Multiplication
#4.dIVISION
# enter a choice 1 add 2 sub 3 mul 4 div
# num1
# num2
def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1 - num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2
print("1.Addition\n"
      "2.Substraction\n"
      "3.Multiplication\n"
      "4.Division\n")
choice=int(input("enter your choice"))
num1=int(input("enter number1"))
num2=int(input("enter number2"))
if (choice==1):
    print(num1,"+",num2,"=",add(num1,num2))
elif (choice==2):
    print(num1, "-", num2, "=", sub(num1, num2))
elif (choice==3):
    print(num1, "*", num2, "=", mul(num1, num2))
elif (choice==4):
    print(num1, "/", num2, "=", div(num1, num2))
else:
    print("invalid")