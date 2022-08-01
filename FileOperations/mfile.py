# f=open("C:/Users/user/Downloads/customer","r")
# for i in f:
#    # print(i)
#   data=i.rstrip("\n").split(",")


  # collect fname,lnmae and age
  # fname=data[1]
  # lname = data[2]
  # age = data[3]
  # print(fname,",",lname,",",age)
  # print(data[1],data[2],data[3])
  # print(data[1:4])
  # print(data[0:4:2])

#age above 50 fname,lname,age,prof

  # if(data[3]>'50'):
  #        print(data[1:5])

#age above 50 and location india print fname lname,age prof

  # if(data[3]>'50') and (data[-1]=='india'):
  #    print(data[1:5])

#each prof count

# f=open("C:/Users/user/Downloads/customer","r")
# dic={}
# for i in f:
#    data=i.rstrip("\n").split(",")
#    prof=data[4]
#    if prof not in dic:
#       dic[prof]=1
#    else:
#       dic[prof]+=1
# print(dic)

#each location count
f=open("C:/Users/user/Downloads/customer","r")
dic={}
for i in f:
   data=i.rstrip("\n").split(",")
   loc=data[-1]
   if loc not in dic:
      dic[loc]=1
   else:
      dic[loc]+=1
print(dic)



