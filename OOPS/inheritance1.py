class Person:
    def setvalue(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name,self.age,self.place)
class Student(Person):
    def setstu(self,roll,dept):
        self.roll=roll
        self.dept=dept
    def printstu(self):
        print(self.name,self.age,self.place,self.roll,self.dept)
st1=Student()
st1.setvalue("Ashly",23,"ernklm")
st1.setstu(101,"bigdata")
st1.printstu()