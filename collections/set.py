#set
#1.how to define
# variable_name=set_function

st=set()


st={10,20,True,'bigdata'} # it support heterogeneous data and insertion order is not allowed
print(st)
st={10,10,20,20,True,'bigdata'}
print(st)

#special case
st3={1,2,3,4,True,'bigdata'}
print(st3) #True=1 so,it will not print in the output
#set i smutable