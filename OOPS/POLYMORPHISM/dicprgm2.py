employee=['vinay','anu']
default={"designation":'bigdata',"salary":1000}

# {'vinay':{designation:bigdata,"salary":1000},}anu...
#fromkeys
res=dict.fromkeys(employee,default)
print(res)
print(res['vinay'])