''''
def greet():
    print("welcome to intellea")
greet()

def calculate(salary):
    return salary + 50000
result = calculate(100000)
print(result)


def calculate_salary(salary):
    return salary
salary = int(input("enter the salary:"))
print(calculate_salary(salary))


def employee(name , age):
    print(name,age)
employee(name="Alice", age=25)

def square():
    n = int(input("enter the number: "))
    return n*n
print(square())



def reverse(n):
    return int(str(n)[::-1])

print(reverse(1234))
'''

def digit_sum(n):
    total = 0

    for digit in str(abs(n)):
        total += int(digit)

    return total
print(digit_sum(-1234))  # Output: 10