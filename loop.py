#####
# FOR LOOP

# below is the simple for loop in python for 3 employee ids,
# employee_id : 1001
# employee_id : 1002
# employee_id : 1003

# Below is the simple for loop in python for 5 employee ids,
for employeeid in range(1001, 1006):
    print(f"employee_id : {employeeid}")

#####
# WHILE LOOP

# while: user has 3 login attempts, if user enters wrong password 3 times, then the account will be locked.
login_attempts = 1
while login_attempts <= 3:
    print(f"Login Attempt: {login_attempts}")
    login_attempts += 1

# Example for while loop - Password validation
password = "" # The empty string is necessary ot else the compiler gives NameError, password variable not defined.
while password != "python123":
    password = input("Enter the password: ")
print("Login Successfull!")

#####
# BREAK STATEMENT

employees = ["ravi", "sachin", "rahul", "rohit", "virat"]
for employee in employees:
    print(f"Checking employee: {employee}")
    if employee == "rahul":
        print(f"Employee found")
        break

#####
# CONTINUE STATEMENT

marks = [45, 67, -1, 89, 34, 56, 78]

for mark in marks:
    if mark == -1:
        continue
    print(f"Mark: {mark}")

# Pattern Printing using for loop
#         - 1star
# #       - 2star 
# # #     - 3star
# # # #   - 4star
# # # # # - 5star

stars = int(input("Enter the number of starts to print: "))
for i in range(1,stars + 1):
    for j in range(1, i + 1):
        print(f"# ", end="")
    print()  # Print a newline after each row

# Print the below pattern:
# * * * *
# * * *
# * *
# *
stars = int(input("Enter the number of rows of stars: "))
for i in range(stars, 0, -1):
    for j in range(i):
        print("* ", end = "")
    print()

# Print the below pattern:
# * * * * 
# *     *
# *     *
# * * * * 
rows = int(input("Enter the number of rows: "))

for i in range(rows):
    for j in range(rows):
        if i != 0 and i != rows-1 and j != 0 and j != rows-1:
            print("  ", end = "")
        else:
            print("* ", end = "")
    print()
  