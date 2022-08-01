#multiple inheritance
#child more than one parent class
#minimum 3 parent class

class A:
    def printa(self):
        print("Inside class A")
class B:
    def printb(self):
        print("Inside class B")
class C(A,B):
     def printc(self):
         print("Inside class C")
ob=C()
ob.printc()
ob.printb()
ob.printa()




