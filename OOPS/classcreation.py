#how to create a class
#syntax
 #class(keyword) class_name:
# class Person:

#methods
#functions inside class is called methods

class Person:
    def reading(self): #method1       #self: an instance keyword
      print("reading books")
    def writing(self):
      print("writing a book") #method2
pe=Person()
pe.reading()
pe.writing()

pe1=Person()
pe1.reading()
pe1.writing()
