"""
    Cart Total with GST
    Easy
    Advanced Functions
    Write cart_total(*prices), which takes any number of prices and returns their sum. With no prices it returns 0.

    Also set add_gst to a lambda that takes an amount and returns amount + amount * 18 // 100.

    The function cart_report is already written. It calls cart_total(*prices) and add_gst.

    Parameters

    prices: list of item prices
    Returns

    A list [items, total, total_with_gst]: the number of prices, their sum, and the sum after adding GST.

    Examples

    Arguments: [120, 80, 50]
    Returns: [3, 250, 295]
    Explanation: The total is 250. The GST is 250 * 18 // 100 = 45, so the total with GST is 295.
    Arguments: [99]
    Returns: [1, 99, 116]
    Explanation: The GST is 99 * 18 // 100 = 17, so the total with GST is 116.
    Constraints

    0 <= number of prices <= 50
    Each price is between 0 and 100000
    Use *args for cart_total and a lambda for add_gst. Do not use sum()
"""

def cart_total(*prices):
    # *prices collects any number of arguments into a tuple; sum() adds them up
    return 0 + sum(prices)


# Lambda that adds 18% GST to the amount, with the tax floored using //
add_gst = None
add_gst = lambda amount : amount + amount * 18 // 100

# Do not change the code below
def cart_report(prices):
    total = cart_total(*prices)
    return [len(prices), total, add_gst(total)]


# Test cases
print(cart_report([100, 200]))       # Output: [2, 300, 354]   (300 * 18 // 100 = 54)
print(cart_report([99]))             # Output: [1, 99, 116]    (99 * 18 // 100 = 17)
print(cart_report([50, 25, 25]))     # Output: [3, 100, 118]
print(cart_report([]))               # Output: [0, 0, 0]       (empty cart)
print(cart_report([10, 10, 10, 5]))  # Output: [4, 35, 41]     (35 * 18 // 100 = 6)

