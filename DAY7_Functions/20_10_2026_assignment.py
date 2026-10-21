"""
    ASSIGNMENT SUBMITTED BY: JAY K JACOB
    Due Wed 21 Oct, 6:00 pm
    Commerce Order Billing System
    Set by Hemalatha · marked out of 10
    Problem statement

    An e-commerce company needs a billing program to calculate a customer's order total, discount, delivery charge, and final payable amount. Write a Python program using reusable functions.

    Requirements
    1. Create a function that accepts a product price and quantity and returns the subtotal.
    2. Create a function that calculates a discount. Use a default discount of 10% if no discount percentage is supplied.
    3. Create a function that calculates the delivery charge, with a default delivery fee of 50.
    4. Create a function that calculates the final payable amount using the returned subtotal, discount, and delivery charge.
    5. Accept the product name, price, quantity, discount percentage, and delivery fee from the user.
    6. Display a formatted bill containing the product name, subtotal, discount amount, delivery charge, and final payable amount.
    7. Use parameters and return values to connect the functions. Do not place the entire calculation inside one function.
    Sample input
    Product name: Keyboard
    Price: 1200
    Quantity: 2
    Discount percentage: 10
    Delivery charge: 50


    Expected output
    --- E-Commerce Bill ---
    Product: Keyboard
    Subtotal: 2400.0
    Discount: 240.0
    Delivery Charge: 50.0
    Final Payable Amount: 2210.0


    Rules: Use only functions, parameters, arguments, return values, default parameters, input, output, arithmetic operators, and conditional statements covered so far. Do not use classes, external libraries, or advanced topics.
"""

# 1. Function that returns the subtotal from price and quantity
def subtotal(PdtPrice, Qty):
    return PdtPrice * Qty

# 2. Function that returns the discount amount (default 10%)
def discount(Amount, Discount = 10):
    return Amount * Discount / 100

# 3. Function that returns the delivery charge (default fee 50)
def deliverycharge(Fee = 50):
    return float(Fee)

# 4. Function that returns the final payable amount from the returned values
def finalpayable(Subtotal, DiscountAmt, Delivery):
    return Subtotal - DiscountAmt + Delivery

# 5. Receive the order details from the user
PdtName = input("Product name: ")
Price = float(input("Price: "))
Qty = int(input("Quantity: "))
DisInput = input("Discount percentage: ")
DelInput = input("Delivery charge: ")

# Connect the functions using return values
SubAmt = subtotal(Price, Qty)
# Use the default discount if the user leaves the input blank
if DisInput == "":
    DisAmt = discount(SubAmt)
else:
    DisAmt = discount(SubAmt, float(DisInput))
# Use the default delivery fee if the user leaves the input blank
if DelInput == "":
    DelAmt = deliverycharge()
else:
    DelAmt = deliverycharge(float(DelInput))
Final = finalpayable(SubAmt, DisAmt, DelAmt)

# 6. Display the formatted bill
print("\n--- E-Commerce Bill ---")
print(f"Product: {PdtName}")
print(f"Subtotal: {SubAmt}")
print(f"Discount: {DisAmt}")
print(f"Delivery Charge: {DelAmt}")
print(f"Final Payable Amount: {Final}")
