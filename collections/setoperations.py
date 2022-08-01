#set operations
# 1.union #elements of set a and b
# 2.intersection #common elemnts
# 3.difference #element present in set a but not in setb
#union
st1={1,2,3,4,5,6,7,8,9,10}
st2={7,8,9,10,11,12,13,14,15}
st3=st1.union(st2)
print(st3)
#intersection
st4={2,6,7,10}
st5={6,0,10,7}
st6=st4.intersection(st5)
print(st6)
#difference
st7={4,8,9,10,20}
st8={1,5,10,20,32}
st9=st7.difference(st8)
print(st9)