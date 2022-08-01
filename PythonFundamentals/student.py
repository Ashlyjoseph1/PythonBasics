class Course:
    def add_course(self,**kwargs):
        self.course=kwargs.get("course_name")
        self.status=kwargs.get("status")

    def __str__(self):
        return self.course_name



class Batch:

    def add_batch(self,**kwargs):
        self.course=kwargs.get("course")
        self.batch_code=kwargs.get("batch_code")
        self.start_date=kwargs.get("start_date")

    def __str__(self):
            return self.batch_code


class Student:
    def add_student(self,**kwargs):
        self.student_name=kwargs.get("student_name")
        self.email = kwargs.get("email")
        self.batch = kwargs.get("batch")

    def __str__(self):
        return self.student_name



dj=Course()
dj.add_course(course_name="django",status=True)


#
# bg=Course()
# bg.add_course(course_name="bigdata",status=True)

dj1=Batch()
dj1.add_batch(course=dj,batch_code="djapril20-22",start_date="27-04-2022")

s1=Student()
s1.add_student(student_name="rahul",email="rahul@gmail.com",batch=dj1)

s2=Student()
s2.add_student(student_name="anu",email="anu@gmail.com",batch=dj1)

s3=Student()
s3.add_student(student_name="mons",email="a@gmail.com",batch=dj1)

# print(s1)

ms=Course()
ms.add_course(course_name="meanstack",status=True)

ms1=Batch()
ms1.add_batch(course=ms,batch_code="msapril20-22",start_date="28-04-2022")

st1=Student()
st1.add_student(student_name="bibin",email="bibin@gmail.com",batch=ms1)

st2=Student()
st2.add_student(student_name="abin",email="abin@gmail.com",batch=ms1)

st3=Student()
st3.add_student(student_name="binu",email="binu@gmail.com",batch=ms1)

students=[]
students.append(st1)
students.append(s1)

#print students in mean stack

ms_stud=[stud.student_name for stud in students if stud.batch.course.course_name=="meanstack"]
print(ms_stud)





