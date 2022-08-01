class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printval(self):
        print(self.name,self.age,self.place)
class Student(Person):
    def __init__(self,roll_no,dept,college,name,age,place):
        super().__init__(name,age,place)
        self.roll_no=roll_no
        self.dept=dept
        self.college=college
    def printstu(self):
        print(self.roll_no, self.dept, self.college)
ob=Student("Ashly",26,"Ernklm",101,"bigdata","ktt")
ob.printstu()
ob.printval()