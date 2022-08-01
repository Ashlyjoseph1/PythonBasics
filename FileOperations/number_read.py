f=open("numbers","r")
lst=[]
for i in f:
    lst.append(int(i.rstrip("\n")))
print(lst)
print(sum(lst))

 #rstrip function

# line="hello\n"
# data=line.rstrip("\n")
# print(data)