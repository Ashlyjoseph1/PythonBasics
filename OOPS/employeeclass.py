class Employee:
    def setvalue(self,name,id,desig,salary,company):
        self.name=name
        self.id=id
        self.desig=desig
        self.salary=salary
        self.company=company
    def printvalue(self):
        print(self.name,self.id,self.desig,self.salary,self.company)
emp1=Employee()
emp1.setvalue("ANNU",10001,"Teacher",10000,"luminar")
emp1.printvalue()

emp2=Employee()
emp2.setvalue("BINU",10002,"Accountant",15000,"luminar")
emp2.printvalue()

emp3=Employee()
emp3.setvalue("CINJU",10009,"Software engineer",15000,"mgmm")
emp3.printvalue()