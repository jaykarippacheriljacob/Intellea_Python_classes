#Dictionary and sets

#Dictionary 

# # variable_name = {
# #     "key1":"value1",
# #     "key2":"value2"
# # }

# # student = {
# #     "name" : "Priya",
# #     "age" : 21,
# #     "course":"python",
# #     "mark":92
# #     }

# # # {} , key : value , pairs seperated by commas , keys unique,value must be anything,
# # dictionary mutable 

# # #empty dictionary

# # student ={}

# # student = dict()

# #accessing dictionary value:
# # #using key
# # student = {
# #     "name" : "Priya",
# #     "age" : 21,
# #     "course":"python",
# #     "mark":92
# #     }
# # print(student["name"])
# # print(student["course"])

# # #using get()
# # student = {
# #     "name" : "Priya",
# #     "age" : 21,
# #     "course":"python",
# #     "mark":92
# #     }

# # print(student.get("name"))
# # print(student.get("age"))
# # print(student.get("Course","Not available"))


# # #Adding new element
# # employee= {
# #     "name":"Arun",
# #     "department" : "IT"
# # }
# # employee ["salary"]= 35000
# # employee ["location"] = "chennai"
# # print(employee)

# # #updating existing value 
# # employee= {
# #     "name":"Arun",
# #     "department" : "IT",
# #     "salary" : 35000
# # }
# # employee ["salary"] = 40000
# # employee["department"] = "Data Analytics"
# # # print(employee)

# # #remove using pop()
# # employee= {
# #     "name":"Arun",
# #     "department" : "IT",
# #     "salary" : 35000
# # }

# # # removed = employee.pop("salary")
# # # print("removed value:",removed)
# # # # print(employee)

# # # # #using del 
# # # # del employee["salary"]
# # # # print(employee)

# # # #using clear()
# # # employee.clear()
# # # print(employee)

# # #keys() , values() , items()

# # employee= {
# #     "name":"Arun",
# #     "department" : "IT",
# #     "salary" : 35000
# # }

# # print(employee.keys())
# # print(employee.values())
# # print(employee.items())

# # #update() - add or update multiple items

# # employee= {
# #     "name":"Arun",
# #     "department" : "IT",
    
# # }
# # employee.update({"salary":40000,"department":"Data Analytics"})
# # print(employee)

# # #Looping through dictionary 
# # employee= {
# #     "name":"Arun",
# #     "department" : "IT",
# #     "salary" : 35000
# # }
# # # for key in employee:
# # #     print(key)

# # # for value in employee.values():
# # #     print(value)

# # for key,value in employee.items():
# #     print(key,":",value)

# #check whether the key exists or not
# # employee= {
# # #     "name":"Arun",
# # #     "Department" : "IT",
# # #     "salary" : 35000
# # # }
# # # # if "department" in employee:
# # # #     print("department is available")
# # # # else:
# # # #     print("departmnet is not available")
# # # print("Arun" in employee.values())

# # #dictionary with condiitonal statements
# # employee= {
# #     "name":"Arun",
# #     "department" : "IT",
# #     "salary" : 35000
# # }
# # if employee["salary"] >= 30000:
# #     print("eligible for promotion",employee["name"])
# # else:
# #     print("not eligible")

# employees = {
#    101: {
#         "name" :"Arun",
#         "departmnet":"IT",
#         "salary":35000
#     },
#    102:{
#         "name" :"Aruna",
#         "departmnet":"Support",
#         "salary":30000
#    },
#    103:{
#         "name" :"Priya",
#         "departmnet":"Development",
#         "salary":40000
#    }
# }
# # print(employees[101]["name"])
# # print(employees[103]["salary"])

# employees[101]["salary"] = 50000
# print(employees)

#Sets {}

# skills = {"python","sql","java","python"}
# print(skills)

# #using set()
# numbers = set([10,20,10,20,40,30])
# print(numbers)

# #empty set
# empty_set = set()
# print(type(empty_set))

# a= {}
# b = set()
# print(type(a))
# print(type(b))

#set properties 
#Set store unique elements
#sets are mutable
#sets are unordered , it does not support indexing and slicing
# #sets store multiple datatypes

# data = {10,"python",True,24000.00}
# print(data[0]) #TypeError: 'set' object is not subscriptable

#Add() - adding an new element to set

# skills ={"python","sql"}
# skills.add("java")
# skills.add("python")
# print(skills)

# #update() - adding multiple elements
# skills = {"python","java"}
# skills.update(["java","power bi","excel"])
# print(skills)

# #remove() - remove elemnet from a set
# skills = {"python","java","sql","power bi"}
# skills.remove("SQL") # KeyError: 'SQL'
# print(skills)
 
#  #discard()
# skills = {"python","java","sql","power bi"}
# skills.discard("c++")
# print(skills)

# # pop()
# skills = {"python","java","sql","power bi"}
# removed = skills.pop()
# print(removed)
# print(skills)

# #clear()
# skills = {"python","java","sql","power bi"}
# skills.clear()
# print(skills)

#set operations - most important concept

python_stu = {"Arun","Priya","kumar","Divya"}
sql_stu = {"Priya","Divya","Ravi","Meena"}

#Union - | - combine all and give unique students from both group
# # print(python_stu | sql_stu)
# print(python_stu.union(sql_stu))

# #intersection - & Find students present in both groups
# # print(python_stu & sql_stu)
# print(python_stu.intersection(sql_stu))

# #Difference  -  Find the students in first group who not in second
# print(python_stu - sql_stu)
# print(sql_stu - python_stu)
# print(python_stu.difference(sql_stu))
# print(sql_stu.difference(python_stu))

# #symmetric difference - ^
# print(python_stu ^ sql_stu)
# print(python_stu.symmetric_difference(sql_stu))

# #issubset()
# candidate_skills = {"python","sql","excel","power bi"}
# required_skills = {"python","sql"}
# print(required_skills.issubset(candidate_skills))
# print(candidate_skills.issubset(required_skills))


# #membership operators in set
# registered_students = {"Arun","Priya","Kumar"}
# print("Arun" in registered_students)

# #issuperset()
# candidate_skills = {"python","sql","excel","power bi"}
# required_skills = {"python","sql"}
# print(required_skills.issuperset(candidate_skills))

# A <= B - subset()
# B>= A - issuperset()

