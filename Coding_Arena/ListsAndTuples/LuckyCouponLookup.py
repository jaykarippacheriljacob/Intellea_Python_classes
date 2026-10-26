"""
    Lucky Coupon Lookup
    Medium
    Tuples
    Given a tuple coupons and a number query, count how many times query appears and find the index of its first appearance. If query is not in the tuple, the position is the text Not found. Also build the tuple reversed, and the tuple without its first and last items.

    Parameters

    coupons: tuple of coupon numbers
    query: number to search for
    Returns

    A tuple (count, position, reversed_coupons, middle):

    count: how many times query appears
    position: index of the first appearance, or Not found
    reversed_coupons: the coupons in reverse order
    middle: the coupons without the first and last item
    Examples

    Arguments: (7, 3, 7, 9, 1) 7
    Returns: (2, 0, (1, 9, 7, 3, 7), (3, 7, 9))
    Explanation: 7 appears twice and first at index 0.
    Arguments: (1, 2, 3) 9
    Returns: (0, 'Not found', (3, 2, 1), (2,))
    Explanation: 9 is missing, so the count is 0 and the position is "Not found". A one item tuple shows a trailing comma.
    Constraints

    1 <= len(coupons) <= 50
    -1000 <= coupon number <= 1000
    Use tuple methods and slicing
"""

def coupon_lookup(coupons, query):
    # Convert the tuple to a list so it can be reversed
    coupon = list(coupons)
    # Count how many times the query appears
    count = 0
    for item in coupon:
        if item == query:
            count += 1
    # Find the first position of the query, -1 if not found
    position = -1
    for i in range(len(coupon)):
        if coupon[i] == query:
            position = i
            break
    # All coupons except the first and last
    middle = coupon[1:len(coupon)-1]
    # Reverse the coupon list in place
    coupon.reverse()
    # Not found: return the message instead of a position
    if position == -1:
        result = (count, "Not found", tuple(coupon), tuple(middle))
    # Found: return the first position
    else:
        result = (count, position, tuple(coupon), tuple(middle))
    return result


# Test cases
print(coupon_lookup(("SAVE10", "FREESHIP", "SAVE10", "NEW50"), "SAVE10"))
# Output: (2, 0, ('NEW50', 'SAVE10', 'FREESHIP', 'SAVE10'), ('FREESHIP', 'SAVE10'))
print(coupon_lookup(("SAVE10", "FREESHIP", "NEW50"), "NEW50"))
# Output: (1, 2, ('NEW50', 'FREESHIP', 'SAVE10'), ('FREESHIP',))
print(coupon_lookup(("SAVE10", "FREESHIP", "NEW50"), "BIG20"))
# Output: (0, 'Not found', ('NEW50', 'FREESHIP', 'SAVE10'), ('FREESHIP',))
print(coupon_lookup(("SAVE10",), "SAVE10"))
# Output: (1, 0, ('SAVE10',), ())   (single coupon, empty middle)
