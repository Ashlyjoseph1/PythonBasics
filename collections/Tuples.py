#tuples
#1.how to define

 #using paranthesis
tu=()
#using tuple function
tu1=tuple()
print(tu)
print(tuple(tu1))

tu=(1,10,56,9)
print(tu)

#2. heterogenous supported or not

tu1=(10,'bigdata',True,10.5)
print(tuple(tu1))

#3.duplicates allowed or not

tu1=(10,10,'bigdata,''bigdata',True,10.5)
print((tu1))

#4. insertion order is preserved

#5.immutable

 # does'nt allow to insert new vaues