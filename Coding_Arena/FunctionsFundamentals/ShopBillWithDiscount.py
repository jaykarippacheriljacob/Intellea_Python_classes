"""
    Shop Bill with Discount
    Easy
    Functions Fundamentals
    Implement two functions.

    item_total(price, quantity) returns price times quantity.
    apply_discount(amount, percent=10) returns amount minus the discount, where the discount is amount * percent // 100.
    The function shop_bill is already written. It uses your two functions.

    Parameters

    price: price of one item
    quantity: number of items
    coupon: coupon discount percent
    Returns

    A list [subtotal, after_default, after_coupon] given by shop_bill: the subtotal, the subtotal after the default 10 percent discount, and the subtotal after the coupon percent.

    Examples

    Arguments: 250 4 25
    Returns: [1000, 900, 750]
    Explanation: 250 x 4 = 1000. A 10 percent discount leaves 900 and a 25 percent discount leaves 750.
    Arguments: 99 3 5
    Returns: [297, 268, 283]
    Explanation: 297 * 10 // 100 = 29, leaving 268. 297 * 5 // 100 = 14, leaving 283.
    Constraints

    0 <= price <= 100000
    0 <= quantity <= 1000
    0 <= coupon <= 100
    Return the results. Do not print inside the functions
"""

def item_total(price, quantity):
    # Subtotal is the price of one item times the number of items
    return int(price * quantity)


def apply_discount(amount, percent=10):
    # Discount is floored with // (default 10 percent), then removed from the amount
    return int(amount - (amount * percent // 100))


# Do not change the code below
def shop_bill(price, quantity, coupon):
    subtotal = item_total(price, quantity)
    return [subtotal, apply_discount(subtotal), apply_discount(subtotal, coupon)]


# Test cases
print(shop_bill(250, 4, 25))   # Output: [1000, 900, 750]
print(shop_bill(99, 3, 5))     # Output: [297, 268, 283]
print(shop_bill(100, 1, 0))    # Output: [100, 90, 100]   (0% coupon, no discount)
print(shop_bill(50, 2, 100))   # Output: [100, 90, 0]     (100% coupon, free)
print(shop_bill(0, 10, 20))    # Output: [0, 0, 0]        (zero price)
print(shop_bill(7, 3, 33))     # Output: [21, 19, 14]     (21*10//100 = 2, 21*33//100 = 6)
