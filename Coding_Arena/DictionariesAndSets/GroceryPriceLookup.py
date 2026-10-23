"""
    Grocery Price Lookup
    Easy
    Dictionaries
    Given lists product_names and product_prices, build a dictionary catalog that maps each name to its price. Also get its keys as a list and its size. Then look up query: its price if it is a key, otherwise the text <query> is not available.

    Parameters

    product_names: list of product names
    product_prices: list of prices, same order as the names
    query: name to search for
    Returns

    A tuple (catalog, names, total, result):

    catalog: dictionary of name to price
    names: list of the names (the keys)
    total: number of products
    result: the price of query, or the text <query> is not available
    Examples

    Arguments: ['Pen', 'Book', 'Bag'] [10, 120, 450] 'Book'
    Returns: ({'Pen': 10, 'Book': 120, 'Bag': 450}, ['Pen', 'Book', 'Bag'], 3, 120)
    Explanation: Book is a key, so the result is its value 120.
    Arguments: ['Tea', 'Coffee'] [15, 25] 'Milk'
    Returns: ({'Tea': 15, 'Coffee': 25}, ['Tea', 'Coffee'], 2, 'Milk is not available')
    Explanation: Milk is not a key, so the result is the text "Milk is not available".
    Constraints

    1 <= len(product_names) <= 30
    0 <= price <= 100000
    Product names are unique and case sensitive
    Use a dictionary. Do not use sets
"""

def price_lookup(product_names, product_prices, query):
    # Dictionary mapping each product name to its price
    result = {}
    for i in range(len(product_names)):
        result[product_names[i]] = product_prices[i]
    # Message used when the product isn't found
    t = " is not available"
    # Product missing: return the "not available" message
    if query not in product_names: 
        return (result, product_names, len(product_names), query+t)
    # Product found: return its price from the dictionary
    else:
        return (result, product_names, len(product_names), result[query])


# Test cases
print(price_lookup(["Pen", "Book", "Bag"], [10, 50, 400], "Book"))
# Output: ({'Pen': 10, 'Book': 50, 'Bag': 400}, ['Pen', 'Book', 'Bag'], 3, 50)
print(price_lookup(["Pen", "Book", "Bag"], [10, 50, 400], "Laptop"))
# Output: ({'Pen': 10, 'Book': 50, 'Bag': 400}, ['Pen', 'Book', 'Bag'], 3, 'Laptop is not available')
print(price_lookup(["Pen"], [10], "pen"))
# Output: ({'Pen': 10}, ['Pen'], 1, 'pen is not available')   (lookup is case-sensitive)
print(price_lookup([], [], "Pen"))
# Output: ({}, [], 0, 'Pen is not available')
