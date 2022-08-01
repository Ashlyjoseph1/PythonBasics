# jumping

# break

# continue

# pass

#break

# for i in range(1,51):
#     if(i==25):
#         break
#     print(i)

#continue

# for i in range(1,51):
#     if(i==25):
#         continue
#     print(i)

#pass

#do nothing


#example
# for i in range(1,51):
#     if(i==25):
#         pass
#     print(i)

for i in range(1,51):
     if(i%2==0):
         pass
     else:
         print(i**2)

#another method

for i in 'luminar':
    print(i)

#interview questions

#1

for num in range(-2,-5,-1):
     print(num,end=' ')

#2

x=0
for i in range(10):
    for j in range(-1,-10,-1):
        x+=1
        print(x)
#3

for l in 'john':
    if l=='o':
        pass
    print(l,end=' ')

#4

for l in 'john':
    if l=='o':
        break
    print(l,end=' ')

#5

for l in 'john':
    if l=='o':
        continue
    print(l,end=' ')

 #6

x=0
a=0
b=-5
if(a>0): #0>0
    if(b<0):
        x+=5
    elif(a>5):
        x+=4
    else:
        x+=3
else:
    x+=2

 #7

x=0
a=5
b=-5

if(a>0):
    if(b<0):
        x=x+5
    elif(a>5):
        x=+4
    else:
        x=x+2
else:
    x=x+4

 #8

a,b=12,5
if a+b:
    print("true")
else:
    print("false")