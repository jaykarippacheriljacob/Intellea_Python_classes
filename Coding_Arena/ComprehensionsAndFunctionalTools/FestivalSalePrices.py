"""     
    Festival Sale Prices
    Easy
    Comprehensions
    Implement three functions using list comprehensions.

    discount_all(prices) returns every price after a 10 percent discount, in the same order. The discounted price is price - price * 10 // 100.
    prices_above(prices, limit) returns the prices greater than limit, in the same order.
    count_above(prices, limit) returns how many prices are greater than limit.
    The function sale_report is already written. It uses your functions with a limit of 500.

    Parameters

    prices: list of prices
    Returns

    A list [discounted, above, count]:

    discounted: the prices after the 10 percent discount
    above: the original prices greater than 500
    count: how many prices are greater than 500
    Examples

    Arguments: [450, 800, 1200]
    Returns: [[405, 720, 1080], [800, 1200], 2]
    Explanation: The discounts are 45, 80 and 120. Only 800 and 1200 are above 500.
    Arguments: [10, 20, 30]
    Returns: [[9, 18, 27], [], 0]
    Explanation: No price is above 500, so the list is empty and the count is 0.
    Constraints

    1 <= number of prices <= 30
    1 <= price <= 10000
    Use list comprehensions to build the lists. Do not use sum(), min(), max(), sorted(), map() or filter()
"""

def discount_all(prices):
    # Apply a 10% discount to every price, flooring the discount with //
    return [x-x*10//100 for x in prices]


def prices_above(prices, limit):
    # Keep only the prices strictly greater than the limit
    return [x for x in prices if x>limit]


def count_above(prices, limit):
    # Build the list of prices above the limit, then count them
    result = [x for x in prices if x>limit]
    return len(result)


# Do not change the code below
def sale_report(prices):
    return [discount_all(prices), prices_above(prices, 500), count_above(prices, 500)]


# Test cases
print(sale_report([200, 750, 1200, 499]))
# Output: [[180, 675, 1080, 450], [750, 1200], 2]   (499 * 10 // 100 = 49 → 450)
print(sale_report([500, 501]))
# Output: [[450, 451], [501], 1]   (500 is not above 500)
print(sale_report([99, 15]))
# Output: [[90, 14], [], 0]
print(sale_report([]))
# Output: [[], [], 0]
