
#binary search using function

def binarysearch(lst,key):
    low=0
    high=len(lst)-1
    mid=0
    while(low<=high):
        mid=(low+high)//2
        if lst[mid]<key:
            low=mid+1
        elif lst[mid]>key:
            high=mid-1
        else:
            return mid
    return -1
lst=[23,90,66,25,45,78]
key=45
r=binarysearch(lst,key)
if(r==-1):
    print("not found")
else:
    print("not found")




