#create a list from element of a range from 1200 to 2000 with steps of 130



# lst=[44,54,64,74,104]
#  create new list lst1=[50,60,70,110]
# lst=[44,54,64,74,104]
# lst1=[i+6 for i in lst]
# print(lst1)

# #1,15 element square greater then 50 elements print
# lst=[i for i in range(1,16) if i**2>50]
# print(lst)

dic={"sedan":1500,"suv":2000,"pickup":2500,"minivan":1600,"van":2400,"semi":13600,"bicycle":8}
#weight above 2000 collect vehicles name in upper case
# lst=[i for i in dic if dic[i]>2000]
# print(lst)
#uppercase conversion

lst=[i.upper() for i in dic if dic[i]>2000]
print(lst)