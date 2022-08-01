# method1
# def fact():
#     num=int(input("enter a number"))
#     fac=1
#     for i in range(1,num+1):
#         fac=fac*i
#     print(fac)
# fact()

#method2
# def fact(num):
#     fac=1
#     for i in range(1,num+1):
#         fac=fac*i
#     print(fac)
# fact(5)

#method3
def fact(num):
    fac=1
    for i in range(1,num+1):
        fac=fac*i
    return fac
data=fact(5)
print(data)
