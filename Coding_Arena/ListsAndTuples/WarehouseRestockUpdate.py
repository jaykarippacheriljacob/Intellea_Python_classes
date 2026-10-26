""" 
    Warehouse Restock Update
    Hard
    Tuples
    Given a list inventory of (name, quantity, price) tuples, restock the item named restock_name by add units. A tuple cannot change, so replace that item with a new tuple. An item's value is quantity x price. If two items share the highest value, the one that comes first wins. Names are unique.

    Parameters

    inventory: list of (name, quantity, price) tuples
    restock_name: name of the item to restock
    add: units to add
    Returns

    A tuple (found, values, best_name, best_value, final):

    found: True if restock_name was in the inventory, else False
    values: list of item values after restocking, in inventory order
    best_name, best_value: the most valuable item and its value
    final: the inventory after restocking, as a tuple of tuples
    Examples

    Arguments: [('Pen', 10, 5), ('Book', 4, 120), ('Bag', 2, 450)] 'Book' 6
    Returns: (True, [50, 1200, 900], 'Book', 1200, (('Pen', 10, 5), ('Book', 10, 120), ('Bag', 2, 450)))
    Explanation: Book goes from 4 to 10 units, so its value becomes 1200, the highest.
    Arguments: [('Lamp', 3, 200), ('Fan', 2, 300)] 'Heater' 4
    Returns: (False, [600, 600], 'Lamp', 600, (('Lamp', 3, 200), ('Fan', 2, 300)))
    Explanation: Heater is not in the list, so nothing changes. Lamp and Fan tie at 600 and Lamp comes first.
    Constraints

    1 <= len(inventory) <= 20
    0 <= quantity, price <= 10000
    0 <= add <= 10000
    Use tuples and unpacking. Do not use dictionaries
 """

def restock(inventory, restock_name, add):
    # Whether the item to restock was found
    found = False
    # Stock value (qty × price) of each item, in order
    total = []
    # Names recorded each time a new highest value is found
    b_item = []
    # Highest stock value so far (starts below any possible value)
    b_value = -1
    for i, (n, qty, p) in enumerate(inventory):
        # Matching item: replace it with an updated tuple (tuples can't be changed)
        if n == restock_name:
           old = inventory.pop(i)
           inventory.insert(i, (n, qty + add, p))
           # Update the local qty so the value below uses the new quantity
           qty += add
           found = True
        # Stock value of this item
        total.append(qty * p)
        # Strictly greater, so on a tie the first item stays
        if b_value < total[-1]:
            b_value = total[-1]
            b_item.append(n)
    # The last name recorded has the highest value
    return (found, total, b_item[-1], b_value, tuple(inventory))


# Test cases
print(restock([("Pen", 10, 5), ("Book", 2, 100), ("Bag", 1, 500)], "Pen", 50))
# Output: (True, [300, 200, 500], 'Bag', 500, (('Pen', 60, 5), ('Book', 2, 100), ('Bag', 1, 500)))
print(restock([("Pen", 10, 5), ("Book", 2, 100)], "Lamp", 5))
# Output: (False, [50, 200], 'Book', 200, (('Pen', 10, 5), ('Book', 2, 100)))   (not found, unchanged)
print(restock([("Pen", 0, 5), ("Cap", 0, 20)], "Cap", 0))
# Output: (True, [0, 0], 'Pen', 0, (('Pen', 0, 5), ('Cap', 0, 20)))   (all zero → first item)

