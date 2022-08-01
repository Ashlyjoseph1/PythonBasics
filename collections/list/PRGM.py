lst=[4,5,10,12,20]
lst1=[]
total_sum=sum(lst)
for i in lst:
    res=total_sum-i
    lst1.append(res)
print(lst1)
