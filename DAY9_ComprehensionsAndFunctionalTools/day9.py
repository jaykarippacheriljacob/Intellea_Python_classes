#List and Dictionary comprehension
#syntax
# # [expression for item in iteratable if condition]
# numbers = [10,25,20,25,30,35]
# even_numbers =[n for n in numbers if n%2==0]
# print(even_numbers)

# num=[1,2,3,4,5]
# square=[n*n for n in num]
# print(square)

#dictionary comprehension

# students = ["Manoj","Arun","Priya"]
# marks=[90,85,89]
# student_mark={students[i]:marks[i] for i in range(len(marks)) }
# print(student_mark)

# squares ={n:n*n for n in range(1,6)}
# print(squares)
# #output - {1:1,2:4,3:9}

# #map()- #map(call function,pass list)
# price_dollar=[10,20,30]
# def convert_to_rupees(price): #10
#     return price*85
# price_rupees=list(map(convert_to_rupees,price_dollar))
# print(price_rupees)

# #filter()
# salaries=[25000,35000,28000,45000,50000]
# def high_salary(salary):
#     return salary>30000
# result =list(filter(high_salary,salaries))
# # print(result)

# #reduce()
# from functools import reduce
# prices=[50,100,200,250]
# total=reduce(lambda a,b:a+b,prices)
# print(total)

#len(),sum(),min(),max(),sorted()

# marks=[85,70,95,60,80]
# result=sorted(marks)
# print(result)
# print(marks)
# # print("Number of elements:",len(marks))
# # print("total:",sum(marks))
# # print("lowest mark:",min(marks))
# # print("highest mark:",max(marks))
# # print("Ascending order:",sorted(marks))
# # print("Descending order",sorted(marks,reverse=True))

#module - every python fine is an module that bcontains reusable code
#inbuilt modules-import
# import math

# print(math.sqrt(64))
# print(math.pi)
# print(math.factorial(5))

# from math import sqrt
# print(sqrt(81))

# import math as m
# radius = float(input("enter the radius:"))
# area =m.pi*m.pow(radius,2)
# print(area)

# # #random module
# # import random
# # # number =random.randint(1,50)
# # # print("random number:",number)
# # colors=["blue","red","green","yellow"]
# # print("selected color:",random.choice(colors))
# # random.shuffle(colors)
# # print("shuffled colors:",colors)

# import datetime
# today =datetime.date.today()
# current =datetime.datetime.now()
# print(today)
# print(current)
# print(today.year)
# print(today.month)
# print(today.day)

# formatted=today.strftime("%m-%Y")
# print(formatted)