# OOP - Object oriented programming

#data/Attributes- student(name,roll no , mark)
# #behaviour/Methods- Display student deatils,Update student info , Calculate total mark
# #class - Blue print /template

# class Student:
#     pass

#object - actual instance for class

# class Student:
#     pass
# student1=Student()
# student2 = Student()
# print(student1)
# print(student2)

#__init___() method and self - current object

# class Student:
#     def __init__(self,name,reg):
#         self.name=name
#         self.reg = reg
# s1 = Student("Ravi",101)
# s2 = Student("Priya",102)

# print(s1.name)
# print(s1.reg)

# # print(s2.name)
# print(s2.reg)

# class Student:
#     def display(self):
#         print(self.name)
#         print(self.marks)
# s1=Student()
# s1.name = "Ravi"
# s1.marks=90
# s1.display()


#instance attributes - 

# class Student:
#      def __init__(self,name,reg):
#          self.name = name
#          self.reg=reg
# s1=Student("ravi",90)
# s2=Student("Priya",99)
# # print(s1.name,s1.reg)
# # print(s2.name,s2.reg)

# # #Instance methods
# # class Student:
# #     def __init__(self,name,marks):
# #         self.name=name
# #         self.marks=marks
# #     def display_details(self):
# #         print("name:",self.name)
# #         print("marks:",self.marks)
# # s1=Student("Ravi",90)
# # s2=Student("Priya",85)
# # s1.display_details()
# # s2.display_details()

# # #Class attribute

# # class Student:
# #     college="ABC college" #class attribute
# #     def __init__(self,name):
# #         self.name=name #instance attribute
# # s1=Student("Ravi")
# # s2=Student("Priya")
# # print(s1.name)
# # print(s1.college) 
# # print(Student.college)

# #Inheritance

# # #Employee(class) - developer , trainer , tester - id , name , role
# # parent class - employee (name,id,role)
# #     developer , trainer , tester (child class)

# #base class / parent class - the class whose feature are inherited 
# #child class / derived class : the class that inherits features and may add its own behaviour


# # class Employee:
# #     def __init__(self,name,id):
# #         self.name = name
# #         self.id=id
# #     def display(self):
# #         print("Employee name:",self.name)
# #         print(self.id)
# # class Developer(Employee):
# #     def write_code(self):
# #         print(self.name ,"is writing code")
# # dev1 = Developer("Ravi",101)
# # dev1.display()
# # dev1.write_code()

# #super() method
# class Employee:
#     def __init__(self,name):
#         self.name=name
# class Developer(Employee):
#     def __init__(self, name,language):
#         super().__init__(name)
#         self.language = language
#     def display_details(self):
#         print(self.name)
#         print(self.language)
        
# d1 = Developer("Ravi","Python")
# d1.display_details()
#single inheritance - one child inherits from one parent

# #multilevel inheritance 
# #A class inherits from a child class forming a chain
# # person - employee(person) - manager(employee)
# class Person:
#     def introduce(self):
#         print("I am a person")
# class Employee(Person):
#     def work(self):
#         print("I am working")
# class Manager(Employee):
#     def manage(Self):
#         print("I manage a team")
# manager = Manager()
# manager.introduce()
# manager.work()

# #Multiple inheritance - programmer / trainer (TechnicalMentor)

# class Programmer:
#     def code(self):
#         print("Writing code")
# class Trainer:
#     def teach(self):
#         print("Teaching Students")
# class TechnicalMentor(Programmer,Trainer):
#     pass
# mentor =TechnicalMentor()
# mentor.code()
# mentor.teach()