#Error and Exception Handling

#Types of errors
# #Syntax error
# print("Welcome"

#Runtime exception/error
# print(10/0) #ZeroDivisionError: division by zero

# #Logical error
# price = 100
# quantity = 3
# total = price+quantity
# print(total)

# #Understanding Tracebacks
# price = 100
# quantity = 0
# total = price/quantity
# print(total)
# #File name,line number , exception type , error message

# #value error
# age = int("twenty")
# print(age)

# #type error
# result = "20" + 10
# print(result)

# #index error
# marks =[80,90,75]
# print(marks[5])

# #keyerror
# student={"name":"Ravi","mark":90}
# print(student["age"])

#Try and except:
# Try - The code that may raise an error/Exception
# except- To handle ther exception
# try:
#     number = int(input("enter the number:"))
#     print("number:",number)
# except ValueError:
#     print("Please enter a valid integer")

# #Handling multiple exceptions
# try:
#     a=int(input("enter first number:"))
#     b=int(input("enter second number:"))
#     result=a/b
#     print(result)
# except ValueError:
#     print("Please enter number only")
# except ZeroDivisionError:
#     print("Cannot divide by zero")

# #else block
# try:
#     mark=int(input("enter mark:"))
# except ValueError:
#     print("Enter a valid number")
# else:
#     print("Your mask is",mark)
#     print("input accepted")

# #finally block
# try:
#     number = int(input("enter a number:"))
#     print(number)
# except ValueError:
#     print("invalid input")
# finally:
#     print("program execution finished")

# #raise statement:
# age =int(input("enter your age:"))
# if age<18:
#     raise ValueError("Age must be 18 or above")
# print("registeration successfull")

#Combining raise with try and except

# try:
#     age=int(input("Enter your age:"))
#     if age<18:
#         raise ValueError("Age must be 18 or above")
# except ValueError as error:
#     print("Error:",error)
# else:
#     print("Registered")

#Practical Application - Billing application
try:
    price=float(input("enter product price:"))
    quantity = int(input("enter qunatity:"))
    
    if price <=0 or quantity <=0:
        raise ValueError("Price and qunatity cannot be zero")
    total=price*quantity
    print("total amount:",total)

except ValueError as error:
    print("Error:",error)
else:
    print("Billing Completed successfully")
finally:
    print("Thank you for using the billing system")
    

#Handle specific exception whenever possible
#display usefull message for uers
#avoid empty except blocks
#keep limited statements in try block that amy raise the exceptions
#validate user input and business rules
#read tracebacks
#test successfull and unsuccessfull scenarios

