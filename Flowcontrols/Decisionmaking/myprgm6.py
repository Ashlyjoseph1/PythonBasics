salary=int(input("enter the salary"))
service=int(input("enter the service"))
if(service>5):
    print("bonus amount is",service*0.5)
else:
    print("not eligible")

#anothermethod

salary=int(input("enter the salary"))
service=int(input("enter the service"))
bonus=service*0.5
if(service>5):
    print("bonusamount is",bonus)
else:
    print("not eligible")


