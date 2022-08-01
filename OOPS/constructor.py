#constructor

class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name,self.age,self.place)
pe1=Person("Ashly",23,"ktym")
pe1.printvalue()

pe2=Person("Binu",25,"ernklm")
pe2.printvalue()
