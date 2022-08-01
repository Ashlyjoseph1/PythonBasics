# def add(num1,num2):
#     sum=num1+num2
#     return sum
# data=add(25,30)
# data1=add(20,100)
# print(data)
# print(data1)
# 5 lines code
# traditional methods

# lamda
# map
# filter
# reduce
# list - comprehension

#lamda

 #anonymous function
 #no identity

 #syntax

 # variable_name=lambda arguments:operation

#add two numbers
# s=lambda n1,n2:n1+n2
# print(s(10,4))

#multiply 3 numbers
# m=lambda n1,n2:n1*n2
# print(m(100,2))

# find cube of a number
# c=lambda no:no**3
# print(c(4))


# map function
# lst=[1,2,3,4,5,6,7,8,9,10] f(x)==>[1,4,9,16,25,36,49,64,81,100] square of numbers in a list

# filter
#[1,32,3,4,5,6,7,8,9,10] f(x)==>[2,4,6,8,10] even numbers printing

# syntax

# variable_name=list(map(arg1,arg2))
# variable_name=list(filter(arg1,arg2))
# arg1:function
# arg2:iterable
# square of the elemets in list

# lst=[1,2,3,4,5,6,7,8,9,10]
#map
# def square(num):
#     op=num**2
#     return op
# data=list(map(square,lst))
# print(data)

# data=list(map(lambda num:num**2,lst))
# print(data)

#even number printing
# def even(num):
#     return num%2==0
# data=list(filter(even,lst))
# print(data)

# data=list(filter(lambda num:num%2==0,lst))
# print(data)

#add 1 to each element in the list

# data=list(map(lambda num:num+1,lst))
# print(data)


# list-comprehension
#
# lst=[]
# for i in range(1,101):
#     lst.append(i)
# print(lst)

#syntax

#list_name=[print range]
# lst=[i for i in range(1,101)]
# print(lst)

#1-75(1,5,9,13 ,17,21...75)


#1-100 even numbers
# lst1=[i for i in range(1,76,4)]
# print(lst1)


#list_name=[print range condition]
# lst=[i for i in range(1,101) if i%2==0]
# print(lst)

#1-50 odd numbers

# lst=[i for i in range(1,51) if i%2!=0]
# print(lst)

#1-50 0dd,even
# lst=[(i,"even") for i in range(1,51) if i%2!=0]
# print(lst)

#muiliple conditions
#syntax
#[print if condition else print range()]
#[print1 if condition1 else print2 if condition2 else print3 range]
#[print1 if condition1 else print2 if condition2 else print3 if condition3 else print4 range]

#1-50 number even print square number odd print cube
# lst=([i**2 if i%2==0 else i**3 for i in range(1,51)])
# print(lst)
# or
# lst=print([i**2 if i%2==0 else i**3 for i in range(1,51)])

#1-50 even print square,odd print that number
# lst=print([i**2 if i%2==0 else (i)for i in range(1,51)])
# (1,1)
# (2,4)
# (3,3)
# (4,16)


#even-print number and "even" and odd-print number and "odd"
# lst=[(i,'even') if i%2==0 else (i,'odd') for i in range(1,31)]
# print(lst)

# number even-square
# number divisible by 5 =0
# number odd -print the number
lst=[i**2 if i%2==0 else 0 if  i%5==0 else i for i in range(1,31) ]
print(lst)

