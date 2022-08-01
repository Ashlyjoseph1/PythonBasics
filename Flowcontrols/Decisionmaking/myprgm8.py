sub1=int(input("enter mark of subject1"))
sub2=int(input("enter mark of subject2"))
sub3=int(input("enter mark of subject3"))
total_mark=sub1+sub2+sub3
if(total_mark>=180):
    print("A+")
elif(160<=total_mark<=179):
    print("A")
elif(140<=total_mark<=159):
    print("B+")
else:
    print("failed")
