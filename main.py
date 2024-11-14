class Student:

    class_year = 2024   #defined outside the constructor.
    num_students = 0
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_students +=1



student1 = Student('kamau',30)
student2 = Student('nnave',40)
student3 = Student('melvin',27)

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)
print(Student.class_year)
     #access the class student,make sure the 's' is caps.
print(Student.num_students)
print(f'my gratuating class of {Student.class_year} has {Student.num_students} students.')