line='cat rat bus cat car rat bus car bus cat'
print(line)
data=line.split(' ')
print(data)
dic={}
for i in data:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)

