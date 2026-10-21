#Functions 
#function is a reuable block of code designed to perform a particular task
#total prices = price*quantity
# p1 = 5000
# q1=3
# total1 = p1*q1
# print(total1)

# p2=4888
# q2=2
# total2=p2*q2
# # print(total2)

# def calculate_total (price,quantity): #paramneters
#     total = price * quantity #function define 
#     print(total)
# #function call
# calculate_total(500,2) #arguments
# calculate_total(800,3)

# # important of functions in industry
# #reusability,Maintainability,Redability,Testimg,Team development
#Two types of functions - inbuilt function - user defined functiom

# # 1.Builtin function
# numbers = [10,20,30,40,50]
# print(max(numbers)) # min ,() , len() ,sum() , type()

# #2.user defined function
# def welcome():
#     print("Welcome to python training")
# welcome()
# welcome()

# #function syntax:
# def function_name():  function define - parameters
#     #statement inside the function
    
# function_name() #function call - arguments

# #Functions with no parameters
# def show_company_name():
#     print("Intellea")
# show_company_name()
# show_company_name()
# show_company_name()

# #function with parameter 
# def greet_stu(name):
#     print("Welcome",name)
# greet_stu("Arun")
# greet_stu("Priya")

# #function with multiple parameter (pass agruments based on the position)
# def display_employee(name,department,salary): #based on position
#     print("Employee name:",name)
#     print("department",department)
#     print("salary",salary)
# display_employee("Arun","IT",35000)
# display_employee("IT","Arun",35000) # wrong

# # keyword arguments
# def display_employee(name,department,salary): 
#     print("Employee name:",name)
#     print("department",department)
#     print("salary",salary)
# display_employee(department="IT") #TypeError: display_employee() missing 2 required positional arguments: 'name' and 'salary'

# def stu_details():
#     pass

#return value
# def add(a,b):
#     return a+b
# result = add(10,20)
# print(result)

#receive values , calculate , return send the result 30 to the caller ,result is get value , then print value

# #print vs returun
# def add(a,b):
#     print(a+b)
# result = add(10,20)
# print("stored result",result)

# #resuing a returned value
# def cal_total(price,quantity):
#     return price*quantity
# def cal_dis(total):
#     return total*0.10
# total = cal_total(1000,2) #total = 2000
# discount = cal_dis(total) #2000
# final_amount = total-discount

# print("Total",total)
# # print("Discount",discount)
# # print("Final amount",final_amount)

# #returning different adattypes
# # def check_eligibility(age):
# #     if age>=18:
# #         return True
# #     else:
# #         return False
# # status = check_eligibility(21)
# # print(status)

# def get_employee():
#     return{
#         "name":"Arun",
#         "department":"salary",
#         "salary":35000
#     }
# employee= get_employee()
# print(employee)
# # print(employee["name"])
# print(employee["department"])

# #returning multiple values

# def calculate(a,b): #a=20,b=5
#     return a+b,a-b
# addition,subtraction =calculate(20,5)
# print("addition",addition)
# print("subtraction",subtraction)

# #default parameter
# def cal_total(total,delivery=50):
#     return total+delivery
# print(cal_total(1000))
# print(cal_total(1000,100))

# local variable and global variable
# def cal_salary():
#     salary=35000
#     print("Inside function",salary)
# cal_salary()
# print(salary)

# #global variable
# company_name="ABC tech"
# def display():
#     print(company_name)
# display()
# print("outside function",company_name)

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Errror : Cannot divide by zero"
    return a/b

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = input("enter your choice:")
a=float(input("enter your first number:"))
b=float(input("enter second number:"))

if choice == "1":
    result = add(a,b)
elif choice == "2":
    result = subtract(a,b)
elif choice == "3":
    result=multiply(a,b)
elif choice =="4":
    result = divide(a,b)
else:
    result = "Invalid choice"
print("Result",result)
    