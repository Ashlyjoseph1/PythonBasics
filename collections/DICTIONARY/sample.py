#dictionary

#1.how to define

dic={}
dic={"rollno":101,"name":'ashly',"age":23,"dept":'bigdata',"salary":1000,"marks":9.0}
print(dic)

#2.heterogeneous data are supported

#3.duplicate value support

#but duplicate value do not suported

dic1={"rollno":101,"name":'ashly',"age":23,"dept":'bigdata',"salary":1000,"marks":23,"marks":34}
print(dic1)

#collect value from a dictionary


dic1={"rollno":101,"name":'ashly',"age":23,"dept":'bigdata',"salary":1000}
print(dic1["name"])
dic1["age"]=30
print(dic1)
