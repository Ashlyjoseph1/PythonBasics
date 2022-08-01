#Regular expression

#python package

 #Pattern package

 #string

 #validation

#finditer:characterwise iteration

#finditer (argument1,aegument2)

#argument1:find_apattern

#argument:string_name

import re

count = 0
s="abcdcccababfabfhjjabjabhy"
matcher=re.finditer('ab',s)
for i in matcher:
    count+=1
    print(i.group())
    print(i.start())
print(count)



