class Person:
    def setperson(self,name,age):
        self.name=name
        self.age=age
                                       #this/self
class Parent:
     def setparent(self,place,phno):
         self.place=place
         self.phno=phno

class Employee(Person,Parent):
      def setemplo(self,id,desig,salary):
          self.id=id
          self.desig=desig
          self.salary=salary
      def printemplo(self):
          print(self.name,self.age, self.place,self.phno,self.id,self.desig,self.salary)
emp=Employee()
emp.setperson("Ashly",23)
emp.setparent("kochi",54565667)
emp.setemplo(101,"python",13000)
emp.printemplo()
