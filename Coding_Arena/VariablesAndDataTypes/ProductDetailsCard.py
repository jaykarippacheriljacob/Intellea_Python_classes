"""
    Product Details Card
    Easy
    Variables and Data Types
    Given a product name, a price and a quantity, print each value with its label. Store the price as a float and the quantity as an int.

    Input Format

    Line 1: product name
    Line 2: price (a whole or decimal number)
    Line 3: quantity (a whole number)
    Output Format

    Line 1: Product: <name>
    Line 2: Price: <price as a float>
    Line 3: Quantity: <quantity>
    Examples

    Input: Pen 10.5 20
    Output: Product: Pen Price: 10.5 Quantity: 20
    Explanation: 10.5 is stored as a float and 20 as an int.
    Input: Notebook 45 3
    Output: Product: Notebook Price: 45.0 Quantity: 3
    Explanation: The price 45 becomes 45.0 after float().
    Constraints

    0 <= price <= 100000
    0 <= quantity <= 1000
    Use only variables, input(), type casting and print()
"""

# Read the product name as a string
pdt_name = input()
# Read the price and convert it to a decimal number
price = float(input())
# Read the quantity and convert it to a whole number
qty = int(input())
# Display the product details
print(f"Product: {pdt_name}")
print(f"Price: {price}")
print(f"Quantity: {qty}")
