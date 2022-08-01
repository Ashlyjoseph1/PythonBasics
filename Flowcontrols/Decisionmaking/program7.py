held=int(input("enter the number of classes held"))
attend=int(input("enter the classes attended"))
per=(attend/held)*100
print(per)
if(per>75):
    print("student is allowed to attend the class")
else:
    print("student is not allowed to attend the class")