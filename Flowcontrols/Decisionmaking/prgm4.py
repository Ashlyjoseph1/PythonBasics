sub1=int(input("enter the mark of subject1"))
sub2=int(input("enter the mark of subject2"))
sub3=int(input("enter the mark of subject3"))
sub4=int(input("enter the mark of subject4"))
total_mark=sub1+sub2+sub3+sub4
print(total_mark)
if(total_mark>=180):
    print("grade is A+")
elif(160<=total_mark<=179):
    print("grade is A")
elif(140<=total_mark<=159):
    print("grade is B+")
elif (120 <= total_mark<=139):
    print("grade is B")
elif (100 <= total_mark<=119):
    print("grade is C+")
elif(80<=total_mark<=99):
    print("grade is C")
else:
    print("Failed")


