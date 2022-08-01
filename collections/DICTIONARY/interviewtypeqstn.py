lst=[1,3,4,5,6,7,4,3,2,]
print(len(lst))
for i in range(0,len(lst)):
    if(lst[i-1]<lst[i]>lst[i+1])or(lst[i-1]>lst[i]<lst[i+1]):
        print(lst[i])