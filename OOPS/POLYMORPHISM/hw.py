student=[('anu',67),('vinu',35),('vipin',56),('amal',65)]
marks=[]
for i in student:
    marks.append(i[1])
maximum=max(marks)
for j in student:
 if j[1]==maximum:
     print(j[0])