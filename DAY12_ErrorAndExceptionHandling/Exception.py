
'''
price = 500
qty = int(input("enter the qty"))
cal = price / qty
print(cal)

#zero division error 
try:
    a=10
    b=0
    result = a / b
    print(result)

except ZeroDivisionError:
    print(" b cannot 0")


# ValueError

try:
    age = int(input("enter your age :"))
    print("your age is :" , age)
except ValueError:
    print("please enter a valid type")


#handling multiple excpetions

try:
    a=int(input("enter the value of a:"))
    b = int(input("enter the value of b:"))
    print("result : " , a/b)
except ValueError:
    print("enter the valid type")
except ZeroDivisionError:
    print(" Second number cannot be 0")


try:
    num = int(input("enter a number:"))

except ValueError:
    print("num should be an integer")

else:
    print("you entered :",num)
    print("Square:", num**2)
# usage of finally

try:
    num = int(input("enter a number:"))
    print("the  number is :",num)
    
except ValueError:
    print("num should be an integer")

else:
    print("you entered :",num)
    print("Square:", num**2)

finally:
    print("programming ended")




RAISE - manullay raising an exception


age = int(input("enter the age:"))
if age < 18:
    raise ValueError("you must be 18 or older")
print("you are eligible")



try :
    num = int(input("enter the number:"))

    if num <= 0:
        raise ValueError("number must be positive")
    print("it is positive")

except ValueError as e:
    print("Error: ",e)


numbers = [ 10 , 20 , 30]
try :
    index = int(input("enter the index"))
    print(numbers[index])

except IndexError:
    print("Index not found")

except ValueError:
    print("enter a valid integer")

'''

student = {
    "name":"Manoj",
    "age" : 22,
    "course": "DATA ENGINEERING"
}
try:
    key = input("enter a key: ")
    print(student[key])

except KeyError:
    print("key not found!:")
