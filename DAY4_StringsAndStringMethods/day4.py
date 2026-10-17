# #Strings: - Sequence of character, it contains , letter , numbers , symbols ,spaces, 
# # string is declare is " "

# # name = "Hema"
# # role = 'trainer'
# # message = """ This is the welcome message for all students
# # those who are enrolled cpurse"""

# # #Accessing a string using index 
# # course = "Python"
# # # P-0,y-1,t-2,h-3,o-4,n-5
# # # n -1 , o-2 , h-3 t-4 , y-5 , p-6 - negative indexing

# # print(course[0])

# # print(course[1])

# # print(course[5])
# # print(course[-1])

# name = "python"
# print(len(name))

# #slicing
# # string[start:stop:step]
# product_code = "LAPTOP2026PRO" # LPO22PO
# print(product_code[:3])
# print(product_code[3:])
# print(product_code[6:10])
# print(product_code[::2])
# print(product_code[::-1])
# print(product_code[2:2])

#1.Common string methods
#1.lower() and upper()
email="HEMA@GMAIL.COM"
print(email.lower())
name = "hemalatha"
print(name.upper())

# #Industry use  - standardizing user input for compare

# user_role = input("enter user role:")
# if user_role.lower() == "admin":
#     print("Access granted")
# else:
#     print("restricted")


# #Strip()
# email = "   hema@gmail.com    "
# print(email)
# print(email.strip())

#replace() - replace(old,new)
# message = "Python is easy"
# updated = message.replace("easy","moderate")
# print(updated)

# phone = "98766-54321"
# after_clean = phone.replace("-","")
# print(after_clean)

# name = "python"
# name[0] = "j"
# print(name) #TypeError: 'str' object does not support item assignment

# #split() - convert string into list
# skills = "python,sql,powerbi"
# print(skills.split(","))

# #join() - list to string
# message =["welcome","to","python"]
# result = " ".join(message)
# print(result)

# # #find() - returs the first occurence of the substring
# # message = "python programming"
# # print(message.find("programming"))
# # print(message.find("java"))

# #startswith() and endswith()
# # email = input("enter your email:")
# # print(email.endswith(".com"))
# # emp_id = input("enter your employee id:")
# # print(emp_id.startswith("EMP"))

# # industry example -file validation

# file = input("enter your file name:")

# if file.lower().endswith(".pdf"):
#     print("it is a pdf file")
# elif file.lower().endswith(".csv"):
#     print("it is a csv file")
# elif file.lower().endswith(".docs"):
#     print("it is a word file")
# else:
#     print("invalid file format")

# # #isdigit() and isalpha

# # age = "twenty"
# # print(age.isdigit())

# # name = "hema"
# # print(name.isalpha())

# username = "Hema123"
# print(username.isalnum())

#f string - fromatted string

# name =input("enter your name:")
# course = input("enter chosen course:")
# print(f"Thank you {name} Welcome to {course} course")

# espression inside the fstring

# price = int(input("enter product price:"))
# quantity = int(input("enter quantity:"))
# print(f"Total amount:{price*quantity}")