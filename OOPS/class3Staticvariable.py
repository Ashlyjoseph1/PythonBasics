class Luminar:
    institution_name="luminar"
    fees=25000
    def setvalue(self,name,roll,age):
        self.name=name
        self.roll=roll
        self.age=age
    def printvalue(self):
        print(self.name,self.roll,self.age,Luminar.institution_name,Luminar.fees)
st1=Luminar()
st1.setvalue("Ashly",101,25)
st1.printvalue()

st2=Luminar()
st2.setvalue("Anilamol",102,23)
st2.printvalue()

st3=Luminar()
st3.setvalue("swetha",110,25)
st3.printvalue()