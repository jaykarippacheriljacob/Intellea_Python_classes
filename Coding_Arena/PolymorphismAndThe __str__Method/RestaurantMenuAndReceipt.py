""" 
    Restaurant Menu and Receipt
    Hard
    Polymorphism and __str__
    Implement the menu classes. Combo and Order only call price() and str() on entries and never check their kind.

    Item(name, base_price): price() returns base_price. __str__() returns <name>: Rs <price>.
    Food(Item) has no __init__ of its own. price() is super().price() + 5.
    Drink(name, base_price, size) inherits from Item. size is S, M or L, and price() adds 0, 20 or 40 to super().price(). __str__() returns <name> (<size>): Rs <price>.
    Combo(name, parts) inherits from Item and calls super().__init__(name, 0). price() adds up the price() of all parts, then subtracts total // 10. __str__() returns <name> combo [<parts>]: Rs <price>, where parts are the part texts joined by a comma and a space. A part can be another combo.
    Order(): add(item, quantity) stores a line. __str__() returns one row <quantity> x <name>: Rs <price * quantity> per line, then Total: Rs <sum of rows>, joined with newlines.
    menu_receipt is already written and uses your classes.

    Parameters

    entries: list of menu entries: (food, name, base_price), (drink, name, base_price, size) or (combo, name, part_names) where part_names is a list of names of entries defined earlier
    orders: list of (name, quantity) pairs, one per order line
    Returns

    A list [menu_lines, receipt]: menu_lines is str(entry) for each menu entry in order, and receipt is str(order) of the finished order.

    Examples

    Arguments: [('food', 'Burger', 100), ('drink', 'Cola', 40, 'M'), ('combo', 'Meal', ['Burger', 'Cola']), ('combo', 'Party', ['Meal', 'Meal', 'Burger'])] [('Meal', 2), ('Burger', 1), ('Party', 1)]
    Returns: [['Burger: Rs 105', 'Cola (M): Rs 60', 'Meal combo [Burger: Rs 105, Cola (M): Rs 60]: Rs 149', 'Party combo [Meal combo [Burger: Rs 105, Cola (M): Rs 60]: Rs 149, Meal combo [Burger: Rs 105, Cola (M): Rs 60]: Rs 149, Burger: Rs 105]: Rs 363'], '2 x Meal: Rs 298\n1 x Burger: Rs 105\n1 x Party: Rs 363\nTotal: Rs 766']
    Explanation: Meal is 105 + 60 = 165 minus 165 // 10 = 16, so 149. Party is 149 + 149 + 105 = 403 minus 40, so 363, and its text contains the full text of each part. The receipt total is 298 + 105 + 363 = 766.
    Constraints

    1 <= number of entries <= 15 and 1 <= number of order lines <= 15
    Names are unique, and can have letters, digits, spaces and the symbol +
    0 <= base_price <= 1000
    A combo has 1 to 5 parts. The same entry can appear more than once, and every part is defined before the combo
    1 <= quantity <= 1000
    Use super() in the child classes
 """

class Item:
    def __init__(self, name, base_price):
        # Store the name and base price shared by every menu entry
        self.name = name
        self.base_price = base_price

    def price(self):
        # Base price; child classes build on this with super()
        return self.base_price

    def __str__(self):
        # e.g. "Burger: Rs 105" (uses each object's own price())
        return f"{self.name}: Rs {self.price()}"


class Food(Item):
    # No __init__ of its own: the parent's (name, base_price) is used

    def price(self):
        # Parent price plus 5
        return super().price() + 5


class Drink(Item):
    def __init__(self, name, base_price, size):
        # Parent sets name and base price; the child adds the size
        super().__init__(name, base_price)
        self.size = size

    def price(self):
        # Size S adds 0, M adds 20, L adds 40 to the parent price
        p = super().price()
        if self.size == "S":
            return p
        elif self.size == "M":
            return p + 20
        elif self.size == "L":
            return p + 40

    def __str__(self):
        # e.g. "Cola (M): Rs 60"
        return f"{self.name} ({self.size}): Rs {self.price()}"


class Combo(Item):
    def __init__(self, name, parts):
        # A combo has no base price of its own, so the parent gets 0
        super().__init__(name, 0)
        self.parts = parts

    def price(self):
        # Sum of the parts' prices (each part uses its own price(), even nested combos)
        total = 0
        for p in self.parts:
            total += p.price()
        # Subtract a 10% discount, floored
        return total - (total // 10)

    def __str__(self):
        # Each part's own text, joined by a comma and a space
        parts_text = ", ".join(str(p) for p in self.parts)
        return f"{self.name} combo [{parts_text}]: Rs {self.price()}"


class Order:
    def __init__(self):
        # List of (item, quantity) pairs, one per order line
        self.lines = []

    def add(self, item, quantity):
        # Store a new line instead of replacing the previous one
        self.lines.append((item, quantity))

    def __str__(self):
        rows = []
        total = 0
        for item, quantity in self.lines:
            # Cost of this line: unit price × quantity
            line_total = item.price() * quantity
            rows.append(f"{quantity} x {item.name}: Rs {line_total}")
            total += line_total
        rows.append(f"Total: Rs {total}")
        # Rows joined with newlines (no newline after the last one)
        return "\n".join(rows)


# Do not change the code below
def menu_receipt(entries, orders):
    menu = {}
    menu_lines = []
    for entry in entries:
        kind, name = entry[0], entry[1]
        if kind == "food":
            item = Food(name, entry[2])
        elif kind == "drink":
            item = Drink(name, entry[2], entry[3])
        else:
            parts = []
            for part_name in entry[2]:
                parts.append(menu[part_name])
            item = Combo(name, parts)
        menu[name] = item
        menu_lines.append(str(item))
    order = Order()
    for name, quantity in orders:
        order.add(menu[name], quantity)
    return [menu_lines, str(order)]


# Test cases
print(menu_receipt([('food', 'Burger', 100), ('drink', 'Cola', 40, 'M'), ('combo', 'Meal', ['Burger', 'Cola']), ('combo', 'Party', ['Meal', 'Meal', 'Burger'])],
                   [('Meal', 2), ('Burger', 1), ('Party', 1)]))
# Output: [['Burger: Rs 105', 'Cola (M): Rs 60', 'Meal combo [Burger: Rs 105, Cola (M): Rs 60]: Rs 149',
#           'Party combo [Meal combo [Burger: Rs 105, Cola (M): Rs 60]: Rs 149, Meal combo [Burger: Rs 105, Cola (M): Rs 60]: Rs 149, Burger: Rs 105]: Rs 363'],
#          '2 x Meal: Rs 298\n1 x Burger: Rs 105\n1 x Party: Rs 363\nTotal: Rs 766']
print(menu_receipt([('drink', 'Tea', 10, 'S'), ('drink', 'Juice', 50, 'L'), ('food', 'Veg Roll+', 0), ('combo', 'Duo', ['Tea'])],
                   [('Juice', 3), ('Duo', 1), ('Veg Roll+', 2)]))
# Output: [['Tea (S): Rs 10', 'Juice (L): Rs 90', 'Veg Roll+: Rs 5', 'Duo combo [Tea (S): Rs 10]: Rs 9'],
#          '3 x Juice: Rs 270\n1 x Duo: Rs 9\n2 x Veg Roll+: Rs 10\nTotal: Rs 289']
