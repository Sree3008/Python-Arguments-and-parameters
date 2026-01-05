# class and objects
'''
Core concepts of oops:

1)class 
2)objects
3)inheritance 
4)polymorphsim
5)abstraction
6)encapsulation
7)composition

Design Concepts of oops
1)Composition
2)Aggregation
3)Association


'''
# class and Object
print("Class and Objects : ")
class student:
    def say_hello(self):
        print("Hi")
s1=student()
s1.say_hello()
# we can also create an multiple obj
s2=student()
s2.say_hello()
print()
# inheritance
'''

types of inheritence:
*single 
*multiple 
*multi level
*hiarchical
*diamond (available only in the python)

'''
print("Inheritance : ")
# example for single inheritence:
class Student:
    def student_details(self,name,age):
        self.name=name
        self.age=age
class Staff(Student):
    def collect_details(self):
        print("name : ",self.name)
        print("Age : ",self.age)
s2=Staff()
s2.student_details("Subha",21)
s2.collect_details()

print()

# example for multiple inheritence
class Student:
    def study_subjects(self,*args):
        self.args=args
    def assignments(self,assignment_name):
        self.assignment_name=assignment_name
class Teacher:
    def teach(self,subject_to_teach):
        self.subject_to_teach=subject_to_teach
    def take_attendance(self,attendance):
        self.attendance=attendance
class TeacherAssistant(Student,Teacher):
    def Print_all_details(self):
        print("Study_subjects")
        for i in self.args:
            print(i)
        print("Assignments")
        print(self.assignment_name)
        print("Staff Teaching Subjects")
        print(self.subject_to_teach)
        print("Attendance")
        print(self.attendance)
TA=TeacherAssistant()
TA.study_subjects("tamil","English","Maths")
TA.assignments("Maths")
TA.teach("English")
TA.take_attendance("Present")
TA.Print_all_details()

#Multi level Inheritance

class Person:
    def person_info(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
class Teacher(Person):
    def teacher_info(self,subject):
        self.subject=subject
class HeadTeacher(Teacher):
    def resposibility(self,resposibile):
        self.resposibile=resposibile
        print("Complete details")
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.subject)
        print(self.resposibile)
hod=HeadTeacher()
hod.person_info("Prakash",21,"Female")
hod.teacher_info("Python")
hod.resposibility("Head of the Department")

# hiarchical

class Parent:
    def skin_color(self,color):
        self.color=color
class Child1(Parent):
    def voice(self,tone):
        self.tone=tone
        print("Child1")
        print(self.color)
        print(self.tone)
class Child2(Parent):
    def height(self,inch):
        self.inch=inch
        print("Child2")
        print(self.color)
        print(self.inch)
c1=Child1()
c1.skin_color("White")
c1.voice("rugged")

c2=Child2()
c2.skin_color("Black")
c2.height("small")
        

# diamond
class A:
    def show(self):
        print("class A")
class B(A):
    def show(self):
        print("Class B")
class C(A):
    def show(self):
        print("class c")
class D(C,B):
    # def show(self):
    #     print("class D")
    pass
        
d=D()
d.show()

print()
print("Polymorphism : ")
# in python there is only presence of methos overriding not over loading
# It achieves similar behavior using default arguments and *args.
class A:
    def write(self):
        print("This is class A")
class B(A):
    def write(self):
        print("This is overriding methos of class B")
b=B()
b.write()

# abstractions
print()
print("Abstractions")
from abc import ABC,abstractmethod
class Abstractions(ABC):
    @abstractmethod
    def login(self):
        print("this is an abstract class")
    def logout(self):
        print("Logout class and not an abstract class")
class MainClass(Abstractions):
    def login(self):
        print("I am login")
    def new_user(self):
        print("I am new User")
m=MainClass()
m.login()
m.logout()
m.new_user()

# encapsulation
class BankAccount:
    def __init__(self,balance):
        self._balance=balance
    def deposit(self,amount):
        self._balance+=amount
    def get_balance(self):
        return self._balance
b=BankAccount(1000)
print(b.get_balance())
