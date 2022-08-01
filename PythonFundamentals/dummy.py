# from builtins import *
#
# ls=list()
class Person(object):
    name:str
    age:int
    place:str
    gender:str
    def __init__(self,**kwargs):
        self.name=kwargs.get("name")
        self.age=kwargs.get("age")
        self.place=kwargs.get("place")
        self.gender=kwargs.get("gender")

    def print_p(self):
        print("personname=",self.name,"age=",self.age,"place=",self.place,"gender=",self.gender)

    def __str__(self):
        return self.name

p=Person(name="ram",age=23,place="kym",gender="male")
# p.print_p()
print(p)