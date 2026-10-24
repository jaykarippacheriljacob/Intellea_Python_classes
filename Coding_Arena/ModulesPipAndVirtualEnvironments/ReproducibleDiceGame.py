""" 
    Reproducible Dice Game
    Medium
    Modules and Packages
    Implement a repeatable dice simulator with the random module.

    roll_dice(seed, n, sides) calls random.seed(seed) once, then returns a list of n rolls. Each roll is int(random.random() * sides) + 1. Do not use randint().
    face_counts(rolls, sides) returns a dictionary mapping every face from 1 to sides to how many times it appears, including faces that never appear.
    most_common_face(counts) returns the face with the highest count. On a tie, return the smaller face.
    roll_total(rolls) returns the sum of the rolls.
    is_repeatable(seed, n, sides, rolls) rolls again with the same seed and returns True if the new rolls equal rolls, else False.
    The function play_dice is already written. It uses your functions.

    Parameters

    seed: seed for the random generator
    n: number of rolls
    sides: number of sides on the dice
    Returns

    A list of five parts from play_dice:

    the list of rolls
    the face counts dictionary (face to count)
    the most common face
    the total of the rolls
    True or False for repeatable
    Examples

    Arguments: 42 5 6
    Returns: [[4, 1, 2, 2, 5], {1: 1, 2: 2, 3: 0, 4: 1, 5: 1, 6: 0}, 2, 14, True]
    Explanation: With seed 42 the first random() value is 0.6394..., and int(0.6394 * 6) + 1 is 4. Face 2 appears most often.
    Arguments: 7 3 2
    Returns: [[1, 1, 2], {1: 2, 2: 1}, 1, 4, True]
    Explanation: Face 1 appears two times and face 2 appears one time.
    Constraints

    0 <= seed <= 1000000
    1 <= n <= 100
    2 <= sides <= 20
    Use the random module. Use random.seed() and random.random() only
    Return the results. Do not print inside the functions
 """


import random as r


def roll_dice(seed, n, sides):
    # Fix the seed so the same seed always gives the same rolls
    r.seed(seed)
    result = []
    # Roll n times: random() gives 0 to <1, so this maps it to 1..sides
    for i in range(1, n+1):
        result.append(int((r.random() * sides) + 1))
    return result


def face_counts(rolls, sides):
    # Start every face from 1 to sides at a count of 0
    faces = {}
    for i in range(1, sides + 1):
        faces[i] = 0
    # Add one for each roll of that face
    for r in rolls:
        faces[r] += 1
    return faces


def most_common_face(counts):
    # Track the highest count and the face that has it
    highest = -1
    key = -1
    for k, v in counts.items():
        # Strictly greater, so on a tie the smaller face stays
        if v > highest:
            key = k
            highest = v
    return key


def roll_total(rolls):
    # Add up all the rolls
    sum = 0
    for r in rolls:
        sum += r
    return sum


def is_repeatable(seed, n, sides, rolls):
    # Re-seed and roll again the same way
    r.seed(seed)
    result = []
    for i in range(1, n+1):
        result.append(int((r.random() * sides) + 1))
    # Compare each new roll with the original; any mismatch means not repeatable
    for i in range(0, n):
        if not result[i] == rolls[i]:
            return False 
    return True


# Do not change the code below
def play_dice(seed, n, sides):
    rolls = roll_dice(seed, n, sides)
    counts = face_counts(rolls, sides)
    return [
        rolls,
        counts,
        most_common_face(counts),
        roll_total(rolls),
        is_repeatable(seed, n, sides, rolls),
    ]


# Test cases
print(play_dice(42, 5, 6))
# Output: [[4, 1, 2, 2, 5], {1: 1, 2: 2, 3: 0, 4: 1, 5: 1, 6: 0}, 2, 14, True]
print(play_dice(7, 10, 6))
# Output: [[2, 1, 4, 1, 4, 3, 1, 4, 1, 3], {1: 4, 2: 1, 3: 2, 4: 3, 5: 0, 6: 0}, 1, 24, True]
print(play_dice(1, 3, 4))
# Output: [[1, 4, 4], {1: 1, 2: 0, 3: 0, 4: 2}, 4, 9, True]
print(play_dice(0, 0, 6))
# Output: [[], {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}, 1, 0, True]   (no rolls)

