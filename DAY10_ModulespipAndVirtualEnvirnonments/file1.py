'''
file = open("demo.txt","w")
file.write("welcome again")
file.close()
print(" Overrr ")


file = open("demo.txt","r")
print(file.read())
file.close()


file = open("demo.txt","w")
file.write("welcome again\n")
file.write("welcome\n")
file.write("Hello\n")
file.close()
print(" Overrr ")



with open("demo.txt","r") as f:
    data = f.read()
print(data)



file = open("demo.txt","r")
content = file.read()
print("number of character:", len(content))
file.close()



CSV - COMMA SEPERATED VALUES



import csv 

file = open("student.csv" , "w", newline="")

writer = csv.writer(file)

writer.writerow(["Name","Age","Mark"])
writer.writerow(["Manoj",10,100])
writer.writerow(["RAM",11,95])
writer.writerow(["ROM",12,88])

file.close()

print("CSV FILE CREATED")


import csv 
file = open("student.csv" , "r")
reader = csv.reader(file)
for row in reader:
    print(row)
file.close()



JSON - JAVASCRIPT OBJECT NOTATION 


import json

student = {
    "name" : "Arun",
    "age"  : 20,
    "mark" : 85
}

file = open("student.json" , "w")
json.dump(student , file , indent = 4 )
file.close()

'''

import json
file = open("student.json","r")
data = json.load(file)
print(data)
file.close()

