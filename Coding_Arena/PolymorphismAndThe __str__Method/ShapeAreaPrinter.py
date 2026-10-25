""" 
    Shape Area Printer
    Easy
    Polymorphism and __str__
    Implement the Shape classes and two functions.

    Shape(name): area() returns 0. __str__() returns <name> with area <area>.
    Rectangle(width, height), Square(side) and Triangle(base, height) inherit from Shape, pass their class name to super().__init__(), and override area() as width * height, side * side and base * height // 2.
    total_area(shapes) returns the sum of all areas.
    largest_shape(shapes) returns the largest shape, the first on a tie.
    shape_report is already written and uses your code.

    Parameters

    shapes: list of tuples: (rectangle, width, height), (square, side) or (triangle, base, height)
    Returns

    A list [lines, total, largest]: lines is str(shape) for each shape in order, total is total_area(shapes) and largest is the str() text of largest_shape(shapes).

    Examples

    Arguments: [('rectangle', 4, 3), ('square', 5), ('triangle', 6, 5)]
    Returns: [['Rectangle with area 12', 'Square with area 25', 'Triangle with area 15'], 52, 'Square with area 25']
    Explanation: The areas are 4 * 3 = 12, 5 * 5 = 25 and 6 * 5 // 2 = 15, so the total is 52. The square is the largest.
    Constraints

    1 <= number of shapes <= 20
    All numbers are whole numbers between 1 and 1000
    Write __str__ only in Shape, and use super().__init__() in the child classes
 """

class Shape:
    def __init__(self, name):
        # Store the shape's name
        self.name = name

    def area(self):
        # Default area; each child class overrides this
        return 0

    def __str__(self):
        # Calls each object's own area() (polymorphism), so one __str__ works for every shape
        return f"{self.name} with area {self.area()}"


class Rectangle(Shape):
    def __init__(self, width, height):
        # Parent sets the name; the child adds its dimensions
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        # Width × height
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        # Parent sets the name; the child adds its side
        super().__init__("Square")
        self.side = side

    def area(self):
        # Side squared
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        # Parent sets the name; the child adds base and height
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        # Half of base × height, floored to a whole number
        return self.base * self.height // 2


def total_area(shapes):
    # Add up the area of every shape
    total = 0
    for s in shapes:
        total += s.area() 
    return total

    # Shorter alternative using sum() with a generator expression:
    # return sum(s.area() for s in shapes)


def largest_shape(shapes):
    # Shape object with the biggest area; max() keeps the first one on a tie
    return max(shapes, key= lambda s:s.area())


# Do not change the code below
def shape_report(shapes):
    objects = []
    for entry in shapes:
        if entry[0] == "rectangle":
            objects.append(Rectangle(entry[1], entry[2]))
        elif entry[0] == "square":
            objects.append(Square(entry[1]))
        else:
            objects.append(Triangle(entry[1], entry[2]))
    lines = []
    for shape in objects:
        lines.append(str(shape))
    return [lines, total_area(objects), str(largest_shape(objects))]


# Test cases
print(shape_report([("rectangle", 4, 5), ("square", 3), ("triangle", 6, 4)]))
# Output: [['Rectangle with area 20', 'Square with area 9', 'Triangle with area 12'], 41, 'Rectangle with area 20']
print(shape_report([("square", 4), ("rectangle", 2, 8)]))
# Output: [['Square with area 16', 'Rectangle with area 16'], 32, 'Square with area 16']   (tie → first)
print(shape_report([("triangle", 5, 3)]))
# Output: [['Triangle with area 7'], 7, 'Triangle with area 7']   (15 // 2 = 7)
