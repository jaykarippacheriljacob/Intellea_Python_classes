# Creating, Indexing, and Slicing Strings

#####
# Creating a string and
word = "PYTHON"

#####
# Printing the string using indexing
print(f"Substring of word {word} from index 2 to 5: {word[2:5]}")

# Foward and backward indexing
print(f"Character at index 0: {word[0]}")  # Output: P
print(f"Character at index -1: {word[-1]}")  # Output: N

#####
# Slicing the string
product_code = "LAPTOP2026PRO"

print(f"Slicing the {product_code} to get the year: {product_code[6:10]}")  # Output: 2026
print(f"Slicing the {product_code} to get the model: {product_code[0:6]}")  # Output: LAPTOP
print(f"Slicing the {product_code} to get the reverse order: {product_code[::-1]}")  # Output: ORP6202POTPAL

#####
# upper() - Returns a copy of the string with all characters converted to uppercase.
name = "ravi"
print(f"Actual name with us {name}. After using upper() the name is {name.upper()}")

# lower() - Returns a copy of the string with all characters converted to lowercase.
name = "RAVI"
print(f"Actual name with us {name}. After using lower() the name is {name.lower()}")

# capitalize()# capitalize() - Returns a copy of the string with the first character uppercased and the rest lowercased.
name = "ravi"
print(f"Actual name with us {name}. After using capitalize() the name is {name.capitalize()}")

# title() - Returns a copy of the string where the first letter of each word is uppercased.
name = "jay k jacob"
print(f"Actual name with us {name}. After using title() the name is {name.title()}")

# strip() - Returns a copy of the string with leading and trailing whitespace removed.
username = "     jay   k"
print(f"Actual name with us {username}. After using strip() the name is {username.strip()}")

# replace() - Returns a copy of the string with all occurrences of a substring replaced by another.
message = "Welcome to Java Training."
print(f"Actual name with us {message}. After using replace() the name is {message.replace("Java", "Python")}")

# find() - Returns the lowest index where the substring is found, or -1 if not found.
email = "student@gmail.com"
print(f"Actual name with us {email}. After using find() the result is {email.find("gmail")}, the starting index.")

# count() - Returns the number of non-overlapping occurrences of a substring in the string.
fruit = "banana"
print(f"Actual fruit with us {fruit}. After using count() the no.of a's present is {fruit.count("a")}.")

# startswith() - Returns True if the string starts with the given prefix, otherwise False.
emp_id = "EMP1025"
print(f"The employee id is {emp_id}. The employee id is {emp_id.startswith("EMP")} using startswith().")

# endswith() - Returns True if the string ends with the given suffix, otherwise False.
file_id = "string.py"
print(f"The filename is {file_id}. The filename is {file_id.endswith(".py")} using endswith().")

# split() - Splits the string into a list of substrings using whitespace (or a given separator).
name = "Jay K Jacob"
print(f"Actual name is {name}. After splitting using split() {name.split()}.")

# join() - Joins the items of an iterable into one string, using the calling string as the separator.
words = ["Python", "is", "easy", "."]
print(f"The set of words to be joined are {words}. After using the join() function {' '.join(words)}")

# isalpha() - Returns True if all characters are alphabetic and the string is not empty.
user1 = "Ravi12"
user2 = "Ravi"
print(f"Is {user1} isalpha? {user1.isalpha()}")
print(f"Is {user2} isalpha? {user2.isalpha()}")

# isdigit() - Returns True if all characters are digits and the string is not empty.
phone_no = "94959903012"
print(f"Is the phone number {phone_no} only digits? {phone_no.isdigit()} ")

# isalnum() - Returns True if all characters are letters or digits and the string is not empty.
print(f"Does {user1} only have alphabets and digits? {user1.isalnum()}")

#####
# f-string, Cleaning Text Input
product = "Laptop"
price = 10000
quantity = 3

print(f"{product} cost is ${price}.")
print(f"Total price of {quantity} {product} is ${price * quantity}.")

name = input("Enter name!")
name = name.strip().title()
print(f"Welcome, {name}!")
