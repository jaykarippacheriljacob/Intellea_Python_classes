#####
# Creating, Acessing and Modifying Lists

# list - An ordered, mutable collection of items enclosed in square brackets [].
# type() - Returns the data type of the given object.
# Indexing - Accesses a single item by its position, starting at 0 (negative indexes count from the end).
products = ["Laptop", "Mouse", "Keyboard", "Headphone", "Webcam"]

print(f"Type of products {type(products)}")

# Accessing the items inside a list
print(f"First product: {products[0]}")
print(f"Second product: {products[1]}")

# Slicing the list
# Slicing - Extracts a portion of the list using [start:stop:step], where stop is excluded.
print(f"Slicing the first 3 products: {products[:3]}")
print(f"Sllicing the last 2 products: {products[-2:]}")
print(f"Printing the products in the reverse order {products[::-1]}")

# Modifying an item in the list
# Modifying an item - Replaces the value at a given index by assigning a new value to it.
products[1] = "Wireless mouse"
print(f"Modified list: {products}")

# appending an item to the end of the list
# append() - Adds a single item to the end of the list.
products.append("usb cable")
print(f"New product appended product list: {products}")

# removing an item from the list by value use of remove()
# remove() - Deletes the first occurrence of the given value from the list.
products.remove("Laptop")
print(f"After removing Laptop from the list using remove(): {products}")

# removing an item from the list by index using the pop()
# pop() - Removes and returns the item at the given index (the last item by default).
removed_product = products.pop()
# removed_product = products.pop(4)
print(f"Removed an item using pop() function from the end {removed_product} is: {products}")

#####
# Sorting, Reversing and Tuples

prices = [1499, 799, 2999, 999, 1999]
print(f"The existing list of prices: {prices}")

# sort() in ascending order
# sort() - Sorts the list in place in ascending order.
prices.sort()
print(f"After sorting in ascending: {prices}")

# sort() in decending order
# sort(reverse=True) - Sorts the list in place in descending order.
prices.sort(reverse=True)
print(f"Sorted in decending order: {prices}")

# reverse() - it just reverses the order of the items
# i.e, last element to first and first element to last so and so forth for all the elements.
# reverse() - Reverses the current order of the items in place, without sorting.
prices = [1499, 799, 2999, 999, 1999]
print(f"Before reversing the order of price: {prices}")
prices.reverse()
print(f"After reversing the order of the prices: {prices}")

# Tuples - they are immutable
# tuple - An ordered, immutable collection of items enclosed in parentheses ().
# Immutability - Once created, a tuple's items cannot be changed, added or removed.
# Creating a tuple
employee = ("emp2002", "priya", "developer")
print(f"Printing the tuple: {employee}")
#employee[1] = "Arun"
#print(f"Trying to modify a value in the tuple: {employee}")

#####
# Nested Lists
# 3 students - 3 subjects { Math Python SQL }

student1 = [80, 75, 90]
student2 = [80, 75, 79]
student3 = [70, 82, 91]

marks = [[80, 75, 90],
         [80, 75, 79],
         [70, 82, 91]]

print(f"Mark obtained by 2 student for SQL: {marks[1][2]}")

# Modifying the values inside a nested list
print(f"Old mark list for student 2: {marks[1]}")
marks[1][2] = 88
print(f"Revised mark list for student 2: {marks[1]}")

# Appending a new student to the exisitng nested mark list
marks.append([67, 89, 50])
print(f"Displaying the appened marklist of new student: {marks[-1]}")

# Accessing the marks of different students using loop
i = 0
for student in marks:
    print(f"Marks of student {i}: {student}")
    i += 1

# Accessing using nested loop in nested list to print the marks one by one
i = 0
subjects = ["Maths", "Python", "SQL"]
for student in marks:
    print(f"Marks of student {i}:")
    j = 0
    for mark in student:
        print(f"{subjects[j]}: {mark}")
        j += 1
    i += 1