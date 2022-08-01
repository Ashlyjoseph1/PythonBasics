#binary search

#lst=[58,0,34,1,3]

#1. sort the gibven list in asending order

#[0,1,3,34,58]
#low          #upp
#2. Declare two variables

 #low=0
 #upper=len(lst)-1

 #3. calculate mid vale

 #mid=(low+upper)//2  (0+4)//2=2

lst=[23,90,66,25,45,78]
lst.sort()
print(lst)
#[23, 25, 45, 66, 78, 90]
element=int(input("enter an element to search"))
low=0
upper=(len(lst)-1)
flag=0
while(low<=upper):
        mid=(low+upper)//2
        if(element>lst[mid]):
            low=mid+1
        elif(element<lst[mid]):
            upper=mid-1
        elif(element==lst[mid]):
             flag=1
             break
if(flag>0):
    print("element found")
else:
    print("element not found")