cheld=int(input("enter the no of class held"))
cattend=int(input("enter the clasess attended"))
per=(cheld/cattend)*100
if(per>75):
    print("student is allowed to attend the calss")
else:
    print("student is not allowed to the class")