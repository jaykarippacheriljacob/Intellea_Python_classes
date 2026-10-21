#####
# List dictionary Comprehensions

# List Comprehension
# [expression for item in ListName]

numbers = [1, 2, 3, 4, 5]
squares = [x*x for x in numbers]
print(f"The list with us is {numbers}, and the new comprehensive list {squares}.")

# List comprehension with condition
# eg. even numbers
even_numbers = [x for x in numbers if x%2 == 0]
print(f"The list comprehension list created using condition for even numbers present in the list {even_numbers}.")

# Dictionary Comprehension
numbers = [1, 2, 3, 4, 5]
squares = {}
for x in numbers:
    squares[x] = x*x

print(f"The revised dictionary comprehension for numbers {numbers} is {squares}.")

# Dictionary comprehension using  one line expression
# {key : value/expression for item in list_name}
squares1 = {x : x*x for x in numbers}
print(f"Printing dictionary using single line expression {squares1}.")

# Dictionary comprehension using conditions
marks = {
    "ravi" : 85,
    "meena" : 72,
    "arun" : 45,
    "priya" : 90
}
passed = {
    name: mark for name, mark in marks.items() if mark >=60
    }
print(f"Passed students segregatted: {passed}")
