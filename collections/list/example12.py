lst=[10,10,20,30,40,50,60,70,80,90,100]
lst1=[]
for i in lst:
    if i not in lst1:
        lst1.append(i)
print(lst1)