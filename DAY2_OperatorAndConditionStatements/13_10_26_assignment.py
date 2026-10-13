# A shopping store calcuates discount based on the user entered purchase amount
# Constraints:
#   1. Purchase amount should not be negative - invalid amount
#   2. Amount greater than or equal to 5000 give 20% discount
#   3. Greater than or equal to 2000 but less than 5000 10% discount
#   4. Otherwise no discount
#   5. Display the final amount

amount = float(input("Enter the amount"))

if amount < 0:
    print(f"The entered amount is invalid")
elif amount >= 5000:
    discount_amount = amount * 80/100
    print(f"The entered amount is eligible for 20% discount: {discount_amount}")
elif amount >= 2000:
    discount_amount = amount * 90/100
    print(f"The entered amount is eligible for 10% discount: {discount_amount}")
else:
    print("Ineligible for discount")