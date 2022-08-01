class Student:
    def setvalue(self,name,rollno,department,college_name):
        self.name=name
        self.rollno=rollno
        self.department=department
        self.college_name=college_name
    def printvalue(self):
        print(self.name)
        print(self.rollno)
        print(self.department)
        print(self.college_name)
        #print(self.name,self.rollno,self.department,self.college_name)
ob1=Student()
ob1.setvalue("Asly",101,"bsc","KTMM")
ob1.printvalue()

ob2=Student()
ob2.setvalue("Bittu",102,"msc","KTMM")
ob2.printvalue()

ob3=Student()
ob3.setvalue("Jeeva",105,"msc","QRT")
ob3.printvalue()

