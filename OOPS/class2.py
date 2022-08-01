class Person:
    def details(self,name,age,place):
        self.fname=name
        self.myage=age
        self.myplace=place
    def printdetails(self):
        print(self.fname)
        print(self.myage)
        print(self.myplace)
de=Person()
de.details("ashly",23,"ktym")
de.printdetails()

de1=Person()
de1.details("jitto",25,"kochi")
de1.printdetails()

de2=Person()
de2.details("manu",25,"kochi")
de2.printdetails()

