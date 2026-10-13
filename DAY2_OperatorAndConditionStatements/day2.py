#Operators and Conditional statements

#Arithmetic operators
# operator - value does not change  +,-
# operand - value will be change  a , b

# a=int(input("Enter A value:"))
# b=int(input("Enter B value:"))
# c=a+b
# print(c)

# # + , - ,*, / , //(floor division) , %(Remainder) , power 2**3 

# product_price = float(input("Enter price:"))
# quantity = int(input("enter quantity:"))
# total_price = product_price * quantity
# print("Total price :",total_price)

#Comparision operator
#== 

# otp_entered = 1234
# otp_saved = 1234
# print(otp_entered == otp_saved)

# # != not equal to - password valisation
# current_password = "python123"
# old_password = "java123"
# print(current_password != old_password)

# #greater than >

# sales = 50000
# target = 50000
# # print(sales >= target)

# # #less than < 

# # minimum_stock = 10
# # stock = int(input("enter current stock :"))
# # print(stock<=minimum_stock)


# #Logical opeartors  - and,or ,not
# #and multiplication
# # age = 25
# # degree_completed = False
# # print(age>=23 and degree_completed)

# # #or addition

# # skill = "python"
# # print(skill == "python" or skill =="java")

# # #not , not True = False , not False = True
# # account_blocked = False
# # if not account_blocked:
# #     print("access denied")

# #Assigment opearots , += , -= , *= , /=,//= ,**=

# score = 10
# # score = score+10
# score+=10
# print(score)
# score-=5
# print(score)
# score*=2
# print(score)
# score/=3
# print(score)
# # score//=3
# # print(score)
# score/=3
# print(score)

# #membership operator - in , not in
# email = "studentgmail.com"
# if "@" in email:
#     print("valid")
# else:
#     print("invalid email") 

# if else

# if condition:
#     statement
# # else:
# #     statement

# # current_year = 2026
# # user_birth_year = int(input("enter birth year:"))
# # age = current_year - user_birth_year

# # if age>=18:
# #     print("Vote eligible")
# # else:
# #     print("not eligible")

# #elif

# # if condition1:
# #     statement
# # elif condition2:
# #     statemnet
# # elif condition3:
# #     statement
# # ------------

# # else:
# #     statement

# mark = int(input("enter your mark:"))
# if mark < 0 or mark > 100:
#     print("invalid mark and enter correct mark")
# elif mark >=90:
#     print("Grade A")
# elif mark >=80:
#     print("Grade B")
# elif mark >=60:
#     print("Grade C") 
# elif mark >=40:
#     print("Grade D")
# else:
#     print("Fail")   

#nested if :
# if condition: # outer if 
#     if condition: #inner if 
#         statemnent
#     else: # for inner if
#         statement
# else: # outer if
#     statement

# degree = input("enter your degree:")
# passed_out_year = int(input("enter your passed out year:"))
# if degree == "CSE":
#     if passed_out_year == 2026:
#         print("eligible")
#     else:
#         print("passed out year not matched")
# else:
#     print("degree and passedout  year not matched")

# A shopping store calculates discounts based on the user enter purchased amount

# rules
# 1.purchase amount should not in negative - invalid amount
# 2.amount greater than or equal to 5000 give 20% discount 
# 3.greater equal to 2000 but less that 5000 10%
# 4.otherwise no discout 
# 5.display the final amount

# enter amount = 6000

# discount :1200
# final amount : 4800


amount = float(input("Enter amount: "))

if amount < 0:
    print("Invalid Amount")

elif amount >= 5000:
    discount = amount * 20 / 100
    final_amount = amount - discount

    print("Discount:", discount)
    print("Final amount:", final_amount)

elif amount >= 2000:
    discount = amount * 10 / 100
    final_amount = amount - discount

    print("Discount:", discount)
    print("Final amount:", final_amount)

else:
    discount = 0
    final_amount = amount

    print("Discount:", discount)
    print("Final amount:", final_amount)f