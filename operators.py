#####
# Arithematic operators for Arithema expressions.

a = 10
b = 6

# Addition
print(a+b)
# Subtraction
print(a-b)
# Multiplication
print(a*b)
# Division
print(a/b)
# Floor Division
print(a//b)
# Modulus
print(a%b)
# Exponentiation
print(a**b)

#####
# Comparison operators for Arithema expressions.

a = 20
b = 6

# Equal operator
print(a==b)
# Not equal operator
print(a!=b)
# Greater than operator
print(a>b)
# Less than operator
print(a<b)
# Greater than or equal to operator
print(a>=b)
# Less than or equal to operator
print(a<=b)

#####
# Logical operators for Arithema expressions.

# AND operator
# Checking if the student is an honor student
name = "John"
age = 20
gpa = 8.0
is_honor = age>= 18 and gpa >= 8.0
print(f"Is {name} a honor student: {is_honor}")  # Output: True

# OR operator
# Checking if the student has an ID or has passed the exam
has_id = True
has_pass = False
is_allowed = has_id or has_pass
print(f"Is {name} allowed to enter: {is_allowed}")  # Output:

# NOT operator
# Checking if the student is blocked from entering
is_blocked = True
can_access = not is_blocked #False
print(f"Is {name} allowed to enter: {can_access}")  # Output: False

#####
# Assignment operators for Arithema expressions.

score = 10

# Addition assignment operator
score += 5  # score = score + 5
print(f"Score after addition assignment: {score}")  # Output: 15

# Subtraction assignment operator
score -= 3  # score = score - 3
print(f"Score after subtraction assignment: {score}")  # Output: 12

# Multiplication assignment operator
score *= 2  # score = score * 2
print(f"Score after multiplication assignment: {score}")  # Output: 24

# Division assignment operator
score /= 4  # score = score / 4
print(f"Score after division assignment: {score}")  # Output: 6.0

# Floor division assignment operator
score //= 2  # score = score // 2
print(f"Score after floor division assignment: {score}")  # Output: 3.

# Modulus assignment operator
score %= 2  # score = score % 2
print(f"Score after modulus assignment: {score}")  # Output: 1

#####
# Membership operators for Arithema expressions.

allowed_departments = ["CSE", "ECE", "MECH", "IT"]
dept = input("Enter your department: ")

# IN operator
# Checking if the department is allowed
is_allowed = dept in allowed_departments
print(f"Is {dept} department allowed: {is_allowed}")  # Output: True

# NOT IN operator
# Checking if the department is not allowed
is_not_allowed = dept not in allowed_departments
print(f"Is {dept} department not allowed: {is_not_allowed}")  # Output