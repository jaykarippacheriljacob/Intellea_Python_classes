"""
    Assign Letter Grades
    Easy
    General Programming
    You are given a list of numerical scores. Your task is to process this list and return a new list containing formatted strings that pair each score with its corresponding letter grade.

    Grading Scale

    The letter grade is determined based on the following scale:

    A: 90 or above
    B: 80 to 89
    C: 70 to 79
    F: Below 70
    Output Format

    Each string in the output list must follow the exact format "Score: Letter", with a colon and a space separating the score and the grade.

    Examples

    Arguments: [95, 72, 45, 88]
    Returns: ["95: A", "72: C", "45: F", "88: B"]
    Explanation: The list contains scores for grades A, C, F, and B. Each score is converted to its corresponding grade and formatted into the required string format.
    Arguments: [90, 89, 70, 69]
    Returns: ["90: A", "89: B", "70: C", "69: F"]
    Explanation: This example tests the boundary conditions for each grade. 90 is an A, 89 is a B, 70 is a C, and 69 is an F.
    Arguments: [100]
    Returns: ["100: A"]
    Explanation: A single score of 100 correctly maps to an 'A' and is formatted as a single-element list.
    Constraints

    The input list `scores` will contain between 0 and 100 elements.
    Each score will be an integer between 0 and 100, inclusive.
"""

def assign_grades(scores):
    """
        Assign letter grades to a list of numerical scores.

        Parameters:
        scores (list): A list of integers representing the scores.

        Returns:
        list: A list of strings formatted as "Score: Letter" for each score.
    """
    # Initialize an empty list to hold the formatted score-grade pairs
    score_with_grades = []
    # Iterate through each score in the input list
    for score in scores:
        if score >=90:
            g = "A"
        elif score >=80 and score <=89:
            g = "B"
        elif score >=70 and score <=79:
            g = "C"
        else:
            g = "F"
        # Append the formatted string to the result list
        score_with_grades.append((f"{score}: {g}"))
    return score_with_grades

# Example usage
scores = [95, 72, 45, 88]
print(assign_grades(scores))  # Output: ["95: A", "72: C", "45: F", "88: B"]
scores = [90, 89, 70, 69]
print(assign_grades(scores))  # Output: ["90: A", "89: B", "70: C", "69: F"]
scores = [100]
print(assign_grades(scores))  # Output: ["100: A"]