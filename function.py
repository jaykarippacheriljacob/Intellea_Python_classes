#####
# Defining Functions, Parameters and Arguments

# Problem: make a greeting code for course enrolled students
# Defining functions with parameters
def student_details(name, course):
    print(f"Welcome, {name}")
    print(f"You are learning {course}")

# Calling the function using arguments
# Values by position
student_details("Jay", "Data Engineering")

# Values by name
student_details(course="Introduction to Python", name="Hemalatha")

#####
# Return Values, Default Parameters and Reusable Calculator Functions
# Problem: Mini-Calculator to add, substract, divide, multiply and power(default value = 2)
def add(a, b):
    return a+b

def substract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

def power(a, b=2):
    return a**b

num1 = 12
num2 =4

print(f"Addition of {num1} and {num2} is {add(12,4)}")

print(f"Substract of {num1} and {num2} is {substract(12,4)}")

print(f"Multiplication of {num1} and {num2} is {multiply(12,4)}")

print(f"Division of {num1} and {num2} is {divide(12,4)}")

print(f"Exponent of {num1} to {num2} is {power(12,4)}")

#####
# Variable Scope, args and kwargs
college = "Intellea" # Global variable

# Scope - inside can see out, but outside cannot see in
def show_student():
    name = "Ravi"
    print(f"Name: {name}")
    print(f"College name: {college}")

show_student()

# args - any number of values inside a tuple
def cal_total(*args):
    total = 0
    for value in args:
        total += value
    print(f"values: {args}")
    print(f"Total: {total}")

cal_total(10, 11, 12, 13, 15)
# kwargs - any number of key, values inside a dictionary
def student_details(**kwargs):
    print(f"student details:")
    for k, v in kwargs.items():
        print(f"{k}: {v}")

student_details(name="Ravi", age=20, city="chennai")

#####
# Lambda Functions and Recursion

# Factorial recursion
def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1)*n

n = 4
print(f"The {n}! = {factorial(n)}")

def countdown(n):
    if n == 0:
        print("Go!!!")
        return
    print("T - ", n, "...")
    return countdown(n-1)

print("Starting the count down -")
countdown(3)

# Sort names by list
names = ["Jay", "Ravi", "Arun", "Meena"]
names.sort()
print(names)
names.sort(key=lambda name:len(name))
print(names)