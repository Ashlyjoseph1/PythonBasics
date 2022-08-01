#inheritance

#parent
#child

#class A (Parent)

   # features(methods&variables)

#class B (Child)

class A:
    def printa(self,num1): #parent class,base class,super class
        self.num1=num1
        print("Inside class A",self.num1)

class B(A): #inheritance
    def printb(self,num2): #child class,sub class,derived class
        self.num2=num2
        print("Inside class B",self.num2,self.num1)

b=B()
b.printa(20)
b.printb(40)
