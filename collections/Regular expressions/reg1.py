import re
s="sssssccghccccccbbccbbcbb"
count=0
match=re.finditer('bb',s)
for i in match:
    count+=1
    print(i.start())
    print(i.group())
print(count)
