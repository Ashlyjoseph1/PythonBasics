class Person:
    def setp(self,name,age):
        self.name=name
        self.age=age
class Child(Person):
    def setc(self,place):
        self.place=place
class Student(Child):
     def sets(self,roll,dept,college):
         self.roll=roll
         self.dept=dept
         self.college=college
     def prints(self):
         print(self.name,self.age,self.place,self.roll,self.dept,self.college)
st=Student()
st.setp("anu",23)
st.setc("ernklm")
st.sets(101,"bigdata","KTTT")
st.prints()