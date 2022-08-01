salary=int(input("enter the salary"))
service=int(input("enter the service"))
bonus=salary*0.05
if(service>5):
    print("bonus amount is",bonus)
else:
    print("not eligible")