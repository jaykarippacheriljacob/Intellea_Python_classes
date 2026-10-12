#####
# Conditional statements

# if statement
# Syntax:

# if condition:
#     # code to execute if condition is True

age = 20

if age >= 18:
    print("You are eligible to vote.")  # Output: You are eligible to vote.

# if-else statement
# Syntax:
# if condition:
#     # code to execute if condition is True
# else:
#     # code to execute if condition is False

age = 16

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")  # Output: You are not eligible to vote.

# if-elif-else statement
# Syntax:
# if condition1:
#     # code to execute if condition1 is True
# elif condition2:
#     # code to execute if condition2 is True
# else:
#     # code to execute if all conditions are False

cgpa = float(input("Enter your CGPA: "))

if cgpa <= 10 and cgpa >= 9:
    print("S grade")
elif cgpa <= 10 and cgpa >= 8:
    print("A grade")  # Output: A grade
elif cgpa <= 10 and cgpa >= 7:
    print("B grade")
elif cgpa <= 10 and cgpa >= 6:
    print("C grade")
elif cgpa <= 10 and cgpa >= 0:
    print("Fail")
else:
    print("Invalid CGPA")  # Output: Invalid CGPA

#####
# NESTED CONDITIONAL STATEMENTS

# Nested if statement
# Syntax:
# if condition1:
#     if condition2:
#         # code to execute if both conditions are True

cgpa = float(input("Enter your CGPA: "))
skill = input("Enter your skill (Python/Java): ")

if cgpa >= 8:
    if skill == "Python":
        print("You are shortlisted") # Output: You are shortlisted
    else:
        print("You are not shortlisted as cgpa is good but skill is not matching")
else:
    print("You are not shortlisted as cgpa is not good")