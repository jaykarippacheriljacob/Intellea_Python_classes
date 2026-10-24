""" 
    Round Table Order
    Easy
    Modules and Packages
    Given the radius of a round table top, implement these functions with the math module.

    circle_area(radius) returns pi * radius squared.
    circumference(radius) returns 2 * pi * radius.
    cloth_needed(radius) returns the area rounded up to a whole number.
    box_side(radius) returns the diameter rounded up to a whole number.
    The function table_report is already written. It uses your functions and rounds the area and circumference to 2 decimal places.

    Parameters

    radius: radius of the table in metres, a number
    Returns

    A list [area, circumference, cloth, box] from table_report: the area and circumference rounded to 2 decimals, then the cloth and box sizes as whole numbers.

    Examples

    Arguments: 7.0
    Returns: [153.94, 43.98, 154, 14]
    Explanation: The area is 153.938..., which rounds to 153.94 and up to 154 for the cloth. The diameter is exactly 14.
    Arguments: 2.5
    Returns: [19.63, 15.71, 20, 5]
    Explanation: The area is 19.634..., which rounds up to 20 for the cloth. The diameter is exactly 5.
    Constraints

    0 <= radius <= 1000, with at most 2 digits after the decimal point
    Use math.pi and math.ceil(). Do not type the value of pi yourself
    Return the results. Do not print inside the functions
 """

import math


def circle_area(radius):
    # Area of a circle: pi × r²
    return math.pi * math.pow(radius, 2)


def circumference(radius):
    # Distance around the circle: 2 × pi × r
    return 2 * math.pi * radius


def cloth_needed(radius):
    # Area rounded UP to a whole number, so there's always enough cloth
    return math.ceil(math.pi * math.pow(radius, 2))


def box_side(radius):
    # The box must fit the diameter (2 × r), rounded UP to a whole number
    return math.ceil(2 * radius)


# Do not change the code below
def table_report(radius):
    return [
        round(circle_area(radius), 2),
        round(circumference(radius), 2),
        cloth_needed(radius),
        box_side(radius),
    ]


# Test cases
print(table_report(1))     # Output: [3.14, 6.28, 4, 2]
print(table_report(2.5))   # Output: [19.63, 15.71, 20, 5]
print(table_report(0.3))   # Output: [0.28, 1.88, 1, 1]   (small values still round up to 1)
print(table_report(0))     # Output: [0.0, 0.0, 0, 0]
