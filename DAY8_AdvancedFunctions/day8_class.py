#Advanced Functions

# #Local variable
# def stu_detail():
#     name = "Manoj"
#     marks =80
#     print("mark inside",name)
#     print("inside marks",marks)
# # stu_detail()
# # print(name) #

# #global var
# college = "ABC College"
# def display_college():
#     print("INside:",college)
# display_college()
# print("outside",college)

# #global keyword - We need to change the global variable value inside the function
# balance = 1000
# def deposit():
#     global balance # modify variable value
#     balance+=500
#     print("updated balance:",balance)
# deposit()
# print(balance)
    
    
# *args in python - number of positional arguments not fixed
# def add(a,b):
#     print(a+b)
# add(10,20,30)

# def add_numbers(*numbers): #args acts like a tuple inside function
#     print(numbers)
#     print("total",sum(numbers)) #inbuilt 
# add_numbers(10,20)
# add_numbers(10,20,30)
# add_numbers(10,20,30,40)

# def stu_result(name,*marks):
#     print("student name:",name)
#     print(marks)
#     print("total",sum(marks))
# stu_result("Manoj",90,85,85)
# stu_result("Arun",78,89,76,90,99)

#**kwargs - it collects values as dictionary

# def stu_details(**kwargs): 
#     print(kwargs)
# stu_details(name="Manoj",age=22,course="Python",mark=90)
# stu_details(name="Manoj",age=22,course="Python")

# def product_info(**product):
#     print("product name:",product.get("name"))
#     print("product price:",product.get("price"))
#     print("product brand:",product.get("brand"))
    
# product_info(name="laptop",price=55000,brand="hp")

# #example - combine student report
# def stu_report(name,*mark,**add_detail):
#     print("Student name:",name)
#     print(mark)
#     print("total mark:",sum(mark))
#     print(add_detail)
# stu_report(
#     "Manoj",90,90,98,95,department="IT",city="chennai"
# )

#lambda function - "lambda" - small ananymous function

# def square(number):
#     return number*number
# print(square(5))

# #syntax - lamda arguments : expression
# square = lambda number: number*number
# print(square(5))

# #add two numbers 
# add = lambda a,b:a+b
# print(add(10,20))
# print(add(30,50))

# #lambda with conditions
# largest = lambda a,b: a if a>b else b
# print(largest(10,20))
# print(largest(50,30))

# #lambda for product discount
# dis_price =lambda price:price *0.90
# print(dis_price(1000))
# print(dis_price(2500))

#Recursive in python - its a programming technique  in which function calls itself again and again to solve a problem

#1.Base case - stop
#2.Recursive case - call itself again and again

# def countdown(n): #function define #5 -4
#     if n==0: #base case
#         print("GO!")
#         return
#     print(n)
#     countdown(n-1) # 5-1 ,4,3 ,2,1 ,0 # recursive case
# countdown(5) #function call

#factorial using recursion - 5! 5x4x3x2x1
def factorial(n): #n=5
    if n<0:
        return"Negative number not allowed"
    if n==0 or n==1:
        return 1 
    return n*factorial(n-1) # 5*4*3*2*1 #recursive case
number = int(input("enter a number:"))
result = factorial(number)
print(result)

# factorial(5) - 5*4!
# factorial(4) - 4*3!
# factorial(3) - 3*2!
# factorial (2) - 2*1!
# factoriall(1) - 1

