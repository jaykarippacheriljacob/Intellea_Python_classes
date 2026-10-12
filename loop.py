#####
# FOR LOOP

# below is the simple for loop in python for 3 employee ids,
# employee_id : 1001
# employee_id : 1002
# employee_id : 1003

# Below is the simple for loop in python for 5 employee ids,
for employeeid in range(1001, 1006):
    print("employee_id :", employeeid)

#####
# WHILE LOOP

# while: user has 3 login attempts, if user enters wrong password 3 times, then the account will be locked.
login_attempts = 1
while login_attempts <= 3:
    print("Login Attempt:", login_attempts)
    login_attempts += 1