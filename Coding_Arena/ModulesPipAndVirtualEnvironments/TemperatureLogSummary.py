""" 
    Temperature Log Summary
    Easy
    Built-in Functions
    Given a list of temperature readings, build a summary dictionary with these keys.

    count: the number of readings
    total: the sum of the readings
    average: total // count
    highest and lowest: the largest and the smallest reading
    ordered: the readings sorted from highest to lowest
    Parameters

    readings: list of whole-number temperature readings, at least one
    Returns

    A dictionary with the keys count, total, average, highest, lowest and ordered. ordered is a list.

    Examples

    Arguments: [31, 35, 28, 33]
    Returns: {'count': 4, 'total': 127, 'average': 31, 'highest': 35, 'lowest': 28, 'ordered': [35, 33, 31, 28]}
    Explanation: The total is 127, and 127 // 4 is 31. Sorted from high to low the readings are 35, 33, 31, 28.
    Arguments: [-3, -4]
    Returns: {'count': 2, 'total': -7, 'average': -4, 'highest': -3, 'lowest': -4, 'ordered': [-3, -4]}
    Explanation: -7 // 2 is -4, because // always rounds down.
    Constraints

    1 <= number of readings <= 50
    -50 <= each reading <= 60
    Use len(), sum(), min(), max() and sorted()
 """

def summarize(readings):
    # Dictionary holding all the summary values
    dict = {
        "count": 0,
        "total": 0,
        "average": 0,
        # Start highest and lowest with the first reading
        "highest": readings[0],
        "lowest": readings[0],
        # Note: this points to the same list as readings, not a copy
        "ordered": readings
        }
    # Sort from highest to lowest (this also reorders the caller's list)
    dict["ordered"].sort(reverse = True)
    for t in readings:
        # Count the reading and add it to the total
        dict["count"] += 1
        dict["total"] += t
        # Update the highest and lowest seen so far
        if t > dict["highest"]:
            dict["highest"] = t
        if t < dict["lowest"]:
            dict["lowest"] = t
    # Whole-number average using floor division
    dict["average"] = dict["total"] // dict["count"]
    return dict


# Test cases
print(summarize([30, 25, 32, 28]))
# Output: {'count': 4, 'total': 115, 'average': 28, 'highest': 32, 'lowest': 25, 'ordered': [32, 30, 28, 25]}
print(summarize([-5, 0, 5]))
# Output: {'count': 3, 'total': 0, 'average': 0, 'highest': 5, 'lowest': -5, 'ordered': [5, 0, -5]}
print(summarize([7]))
# Output: {'count': 1, 'total': 7, 'average': 7, 'highest': 7, 'lowest': 7, 'ordered': [7]}

# Shows that the original list gets reordered
data = [1, 3, 2]
summarize(data)
print(data)
# Output: [3, 2, 1]
