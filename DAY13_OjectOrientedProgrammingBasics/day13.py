# #Advanced OOPs concept  - Encapsulation , Polymorphism and __str__ method

# # #Encapsulation - Provides a controlled way to access the data

# # # # #without encapsulation
# # # # class BankAccount:
# # # #     def __init__(self,balance):
# # # #         self.balance=balance
# # # # account=BankAccount(5000)
# # # # account.balance=-10000
# # # # print(account.balance)

# # # #Encapsulation - Private attribute
# # # class BankAccount:
# # #     def __init__(self,balance):
# # #         self.__balance=balance
# # #     def deposit(self,amount):
# # #         if amount > 0:
# # #             self.__balance += amount
# # #             print("Deposit successfull")
# # #         else:
# # #             print("Inavlid deposit amount")
# # #     def withdraw(self,amount):
# # #         if amount <=0:
# # #             print("Invalid withdrawal amount")
# # #         elif amount > self.__balance:
# # #             print("Insufficient balance")
# # #         else:
# # #             self.__balance -=amount
# # #             print("Withdrawal successfull")
# # #     def display_balance(self):
# # #         print("Available balance:",self.__balance)
    
# # # account = BankAccount(5000)
# # # account.deposit(5000)
# # # account.withdraw(1000)
# # # account.display_balance()
# # # print(account.__balance)

# # # balance - Public attribute - self.balance
# # # _balance - Protected - self._balance
# # # __balance - Private - self.__balance

# # # cpontrolled access using @property

# # class Employee:
# #     def __init__(self,salary):
# #         self.__salary = salary
# #     @property
# #     def salary(self):
# #         return self.__salary
# #     @salary.setter
# #     def salary(self,amount):
# #         if amount >0:
# #             self.__salary = amount
# #         else:
# #             print("Salary must be positive")
# # employee = Employee(30000)
# # print(employee.salary)
# # employee.salary = 40000
# # print(employee.salary)
# # employee.salary = -5000
# # print(employee.salary)

# #Ploymorphism - Many forms

# #Method overriding
# # different classes use same method name - No inheritance

# class Developer:
#     def work(self):
#         print("Developer writing code")
# class Tester:
#     def work(self):
#         print("Tester tests application")
# class Designer:
#     def work(self):
#         print("Creates Design")
# dev = Developer()
# test = Tester()
# design = Designer()

# dev.work()
# test.work()
# design.work()

#Method overloading but no private attribute

# class Developer:
#     def work(self,task1,task2=None):
#         if task2 is None:
#             print("Develeoper work on :",task1)
#         else:
#             print("Develoepr works on :",task1,task2)
# class Tester:
#     def work(self,task1,task2=None):
#         if task2 is None:
#             print("Tester work on :",task1)
#         else:
#             print("Tester works on :",task1,task2)
    
# dev=Developer()
# test = Tester()
# dev.work("Coding")
# dev.work("Coding","Debug")

# test.work("Testing")
# test.work("Testing","Bug reporting")

# # without __str__

# class Student:
#     def __init__(self,name):
#         self.name=name
# s1=Student("Ravi")
# print(s1)


# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def __str__(self):
#         return f"student Name:{self.name},Marks:{self.marks}"
# s1=Student("Ravi",90)
# print(s1)
        
        