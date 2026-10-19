"""
ASSIGNMENT SUBMITTED BY: JAY K JACOB
Due Mon 19 Oct, 11:00 am
E-Commerce Inventory Management System
Set by Hemalatha · marked out of 10
Scenario: 

A company needs a simple inventory management program to maintain product names, stock quantities, and product prices. Your task is to develop a program using Python Lists and Tuples.
Assignment Requirements

Write a Python program that performs the following operations:
1. Create a list of product names: ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"].
2. Create a list of stock quantities: [10, 25, 15, 8, 20].
3. Create a tuple containing the product prices: (45000, 500, 1200, 12000, 1800).
4. Display the first three products using list slicing.
5. Display the last two products using negative indexing or slicing.
6. Add a new product "Webcam" to the product list and add its stock quantity 12 to the stock list.
7. Update the stock quantity of "Mouse" to 30.
8. Remove "Keyboard" from the product list and remove its corresponding stock quantity.
9. Display the total number of products using len().
10. Count how many products have a stock quantity greater than or equal to 15.
11. Display the product list in alphabetical order using sort().
12. Display the product names and their corresponding stock quantities and prices.

Expected Output Format
First Three Products: ['Laptop', 'Mouse', 'Keyboard']
Last Two Products: ['Monitor', 'Headphones']

Updated Product List:
['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones', 'Webcam']

Updated Mouse Stock: 30

After Removing Keyboard:
['Laptop', 'Mouse', 'Monitor', 'Headphones', 'Webcam']

Total Products: 5
Products with Stock >= 15: 3

Products in Alphabetical Order:
['Headphones', 'Laptop', 'Monitor', 'Mouse', 'Webcam']

--- Inventory Report ---
Laptop - Stock: 10 - Price: 45000
Mouse - Stock: 30 - Price: 500
Monitor - Stock: 8 - Price: 12000
Headphones - Stock: 20 - Price: 1800
Webcam - Stock: 12 - Price: Not Available


Note: The output is illustrative. Students should ensure that the product, stock, and price information remains correctly matched after updates and removals.

Concepts Covered
- Lists and tuples
- Indexing and negative indexing
- Slicing
- append(), remove(), sort()
- len() and count() where applicable
- Updating list elements
- Nested or parallel list handling
- Iterating through list data using loops

Student instruction: Write the complete program independently using only the Day 5 concepts taught in class. Do not use dictionaries, functions, classes, external libraries, or advanced concepts.
"""

# 1. Creating a list of product names:
pdt_lst = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]

# 2. Creating a list of stock quantities:
stk_qty = [10, 25, 15, 8, 20]

# 3. Creating a tuple containing the product prices: 
pdt_prices = (45000, 500, 1200, 12000, 1800)

# 4. Displaying the first three products using list slicing.
print(f"First Three Products: {pdt_lst[:3]}")

# 5. Displaying the last two products using negative indexing or slicing.
print(f"Last Two Products: {pdt_lst[-2:]}")

# 6. Adding a new product "Webcam" to the product list and add its stock quantity 12 to the stock list.
pdt_lst.append("Webcam")
stk_qty.append(12)
print(f"Updated Product List:")
print(pdt_lst)

# 7. Updating the stock quantity of "Mouse" to 30.
# print(stk_qty)
stk_qty[pdt_lst.index("Mouse")] = 30
print(f"Updated Mouse Stock: {stk_qty[pdt_lst.index("Mouse")]}")
# print(stk_qty)

# 8. Removing "Keyboard" from the product list and removing its corresponding stock quantity.
# print(stk_qty)
r_index = pdt_lst.index("Keyboard")
# print(stk_qty)
pdt_lst.remove("Keyboard")
r_qty = stk_qty.pop(r_index)
print(f"After Removing Keyboard:")
print(pdt_lst)

# 9. Displaying the total number of products using len().
print(f"Total Products: {len(pdt_lst)}")

# 10. Counting how many products have a stock quantity greater than or equal to 15.
# Alternative
# c = sum(1 for x in stk_qty if x >= 15)
c = 0
for qty in stk_qty:
    if qty >= 15:
        c += 1
print(f"Products with Stock >= 15: {c}")
# print(stk_qty)
# Note: the answer might vary from the expected output. Its not because the code or logic is wrong,
#       it is because one order quantity thats greater than 15 is keyboard and it has been popped.

# 11. Displaying the product list in alphabetical order using sort().
# Note: since copy() is not allowed:
s_pdt_lst = []
for i in range(len(pdt_lst)):
    s_pdt_lst.append(pdt_lst[i])
s_pdt_lst.sort()
print(f"Products in Alphabetical Order:")
print(s_pdt_lst)
# print(pdt_lst)

# 12. Displaying the product names and their corresponding stock quantities and prices.
print(f"--- Inventory Report ---")
j = 0
for i in range(len(pdt_lst)):
    print(f"{pdt_lst[i]} -", end = " ")
    if j == r_index:
        j += 1
    print(f"Stock: {stk_qty[i]}", end = " ")
    print(f"- Price:", end = " ")
    if j >= len(pdt_prices):
        print(f"Not Available", end = "")
    else:
        print(f"{pdt_prices[j]}", end = "")
    print()
    j += 1
