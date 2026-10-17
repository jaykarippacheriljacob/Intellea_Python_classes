# List and Tuples
#List - different type of datas stored together inside the [] , (,)

# student1 = "Hema"
# student2 = "priya"
# student3 = "dinesh"

# names = ["Hema","Priya","Arun"]
# marks = [89,78,98]
# details = ["Hema",25,30000.00,True]

# print(names)
# print(type(names))
# # print(marks)
# # print(type(marks))
# # print(details)
# # print(type(details))

# # #Accessing the list - index 0 
# # products = ["laptop","mouse","keyboard","monitor"]
# # print(products[0])
# # print(products[3])
# # print(products[-1])


# #List slicing

# # # list_name[start:stop:step]
# # products = ["laptop","mouse","keyboard","monitor","printer","camera","charger"]
# # print(products[:3])
# # print(products[2:])
# # print(products[1:4])
# # print(products[::-1])
# # print(products[-3:])

# # #List - mutable 
# # products = ["laptop","mouse","keyboard","monitor","printer","camera","charger"]
# # products[1] = "wireless mouse"
# # print(products)

# # #append() addoing an itel at the end of the list
# # cart = ["laptop","mouse"]
# # new_product = input("enter desire product:")
# # cart.append(new_product)
# # print(cart)

# #insert() - adding an item at a specific position
# # products = ["laptop","mouse","keyboard","monitor","printer","camera","charger"]
# # products.insert(1,"mobile")
# # print(products)

# # #industry example
# # tickets = ["T100","1101","T102"]
# # tickets.insert(0,"URGENT100")
# # print(tickets)

# # # #remove() - Remove an item ina list by value
# # products = ["laptop","mouse","keyboard","monitor","printer","camera","charger"]
# # removed_product = products.remove("keyboard")
# # print(removed_product)
# # print(products)
# # print("keyboard" in products)

# # #pop() - removing an item by index
# # products = ["laptop","mouse","keyboard","monitor","printer","camera","charger"]
# # removed_product = products.pop()
# # print(removed_product)
# # print(products)

# #sort () and sort(reverse = True)
# #reverse
# marks = [85,60,95,70]
# marks.sort()
# print(marks)

# marks = [85,60,95,70]
# marks.sort(reverse=True)
# print(marks)

# marks = [85,60,95,70]
# marks.reverse()
# print(marks)

# #len() , count() , index()

# feedback = ["Good","Excellent","Average","Good","Average","Poor","Good"]
# print(len(feedback))
# print(feedback.count("Good"))
# print(feedback.index("Good")) #first occurance index


#Tuples

# employee = ("EMP101","Arun",35000)
# print(employee)
# print(type(employee))

# age = (21)
# print(type(age))
# age1= (21,)
# print(type(age1))

# products = ("Phone","power bank","charger","mouse")
# products[2] = "wireless charger"
# print(products) #typeerror 

#nested lists - list inside another list
students = [
    ["priya",85,90],
    ["Arun",78,88],
    ["Arun",92,95]
]

# print(students)
# #access
# print(students[0])
# print(students[0][0])
print(students[:2]) # start and stop both will be a row
print(students[0][1:2]) # priya , 85,90
print(len(students))
print(len(students[0]))



