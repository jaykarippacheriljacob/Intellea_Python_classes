# #Loops

# print("customer 1")
# print("customer 2")
# print("customer 3")
# for , while

#For loop
# for i in range():
#     statement

# for i in range():
#     print(i)

# range() - range(stop) , range(start,stop), range(start,stop,step)

# for i in range(5):
#     print(i)

# for i in range(1,6):
#     print(i)

# for i in range(1,10,2):
#     print(i)
# # 1 2 3 4 5 6 7 8 9 10

# for i in range(2,11,2):
#     print(i)

# for i in range(1,0,-1):
#     print(i)

#Loop with user input

# for i in range(3):
#     name = input("enter your name:")
#     print("registered:",name)

# #break statement
# for i in range(1,11):
#     if i==5:
#         break
#     print(i)

# # Real time example - search emplotee id
# emp_ids = [101,102,103,104,105]
# search_id = int(input("enter employee id:"))

# for emp_id in emp_ids:
#     print("checking:",emp_id)
    
#     if emp_id == search_id:
#         print("employee found!")

# #Continue
# for i in range(1,6):
#     if i==3:
#         continue # skip the value
#     print(i)

# real time example - skip inactive employees

# employees = [
#     ("Arun","Active"),
#     ("Priya","Inactive"),
#     ("karthick","Inactive"),
#     ("Divya","Active")
# ]

# for name , status in employees:
#     if status == "Inactive":
#         continue
#     print(name,":",status)

#while loop :
# while condition:
#     #code


# count = 1 #2 #3 #4 #5 #6
# while count<=5:
#     print(count)
#     # count+=1 # count = count+1

# real time eaxmple - password login attempt

# password = ""
# while password != "python123":
#     password = input("enter your password again:")
# print("login successfull")


# #break with while 

# while True:
#     command = input("enter command:")
    
#     if command == "exit":
#         break
#     print("command received",command)

#Nested loops - pattern printing

# * * *
# * * *
# * * *

# #pattern analysis
# 1 - 3
# 2 - 3
# 3 - 3
# row change - start count does not change

#outer loop - row 
#inner loop - star print

# for i in range(3):  
#     for j in range(3):
#         print("*",end = " ")
#     print()

# # 0 - * * * 
# # 1 - * * *
# # 2 - * * *
        
# increase triangle 

# *
# * *
# * * *
# * * * *

# #pattern analysis , row == no of stars in the row

# for i in range(1,5):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# decrease triangle or Reverse triangle
# * * * * *
# * * * *
# * * *
# * * 
# *

#pattern analysis , step -1
for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

# * * * * - 0
# *     *  13 - row = 1 , column =3 (j)
# *     *
# * * * *  -3

# # hallowen pattern
# i = row , j=column  , rows == column


rows = int(input("enter number of rows:")) # 4 
for i in range(rows): #4
    for j in range(rows): #4  - 0 1 -- 3 (rows-1 4-1)
        if i==0 or i==rows-1 or j==0 or j==rows-1:
            print("*",end = " ")
        else:
            print(" ",end=" ")
    print()