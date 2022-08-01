class Employee:
    def __init__(self,id,fname,lname,age,prof,loc):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.prof=prof
        self.loc=loc
    def printcustomer(self):
        print(self.id,self.fname,self.lname,self.age,self.prof,self.loc)
f=open("C:/Users/user/Downloads/customer","r")
for i in f:
    data=i.rstrip("\n").split(",")
    id=data[0]
    fname=data[1]
    lname=data[2]
    age= data[3]
    prof=data[4]
    loc=data[-1]
    ob=Employee(id,lname,fname,age,prof,loc)
    ob.printcustomer()

    #print(ob.fname,ob.lname)


