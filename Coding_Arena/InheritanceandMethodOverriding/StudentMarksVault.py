""" 
    Student Marks Vault
    Easy
    super() and Encapsulation
    Implement the Student class with private marks.

    Student(name, marks) stores name as self.name and the marks as self.__marks. It sets them to 0, then calls set_marks(marks), so an invalid starting mark leaves 0.
    set_marks(value) saves value and returns True when 0 <= value <= 100, else returns False and keeps the old marks.
    get_marks() returns the marks.
    grade() returns A for 90 or more, B for 75 or more, C for 50 or more, else F.
    run_student is already written and uses your class.

    Parameters

    name: student name
    start: starting marks
    commands: list of tuples: (SET, value), (GET,) or (GRADE,)
    Returns

    A list [lines, has_public, has_private]: lines has one message per command, has_public tells if the student object has a plain marks attribute and has_private tells if it has the private one.

    SET that worked: Marks updated to <marks>
    SET that failed: Invalid marks: <value>. Marks stay <marks>
    GET: Marks: <marks>
    GRADE: Grade: <letter>
    Examples

    Arguments: 'Asha' 72 [('GET',), ('SET', 95), ('GRADE',), ('SET', 120), ('GET',), ('SET', 49), ('GRADE',)]
    Returns: [['Marks: 72', 'Marks updated to 95', 'Grade: A', 'Invalid marks: 120. Marks stay 95', 'Marks: 95', 'Marks updated to 49', 'Grade: F'], False, True]
    Explanation: 95 is saved, so the grade is A. 120 is above 100 and is refused, so the marks stay 95. 49 is saved and is below 50, so the grade is F. The marks are private, so has_public is False and has_private is True.
    Constraints

    1 <= number of commands <= 30
    The name has only letters and no spaces
    -1000 <= starting marks and SET values <= 1000
    Store the marks as self.__marks, not self.marks or self._marks
 """

class Student:
    def __init__(self, name, marks):
        # Public attribute: name can be used freely
        self.name = name
        # Private attribute: start at 0, so it exists even if the starting marks are invalid
        self.__marks = 0
        # Set the starting marks through the validating method
        self.set_marks(marks)

    def set_marks(self, value):
        # Setter: only accept marks from 0 to 100
        if 0 <= value and value <= 100:
            self.__marks = value
        # Invalid value: leave the marks unchanged and report failure
        else:
            return False
        return True

        # Shorter alternative using a chained comparison:
        # if 0 <= value <= 100:
        #     self.__marks = value
        #     return True
        # return False

    def get_marks(self):
        # Getter: the only way to read the private marks from outside
        return self.__marks

    def grade(self):
        # Grade based on the current marks
        if self.get_marks() >= 90:
            return "A"
        elif self.get_marks() >= 75:
            return "B"
        elif self.get_marks() >= 50:
            return "C"
        else:
            return "F"


# Do not change the code below
def run_student(name, start, commands):
    student = Student(name, start)
    lines = []
    for command in commands:
        if command[0] == "SET":
            value = command[1]
            if student.set_marks(value):
                lines.append(f"Marks updated to {student.get_marks()}")
            else:
                lines.append(f"Invalid marks: {value}. Marks stay {student.get_marks()}")
        elif command[0] == "GET":
            lines.append(f"Marks: {student.get_marks()}")
        else:
            lines.append(f"Grade: {student.grade()}")
    return [lines, hasattr(student, "marks"), hasattr(student, "_Student__marks")]


# Test cases
print(run_student("Asha", 80, [("GET",), ("SET", 95), ("GRADE",), ("SET", 120), ("GET",)]))
# Output: [['Marks: 80', 'Marks updated to 95', 'Grade: A', 'Invalid marks: 120. Marks stay 95', 'Marks: 95'], False, True]
print(run_student("Ravi", 150, [("GET",), ("GRADE",)]))
# Output: [['Marks: 0', 'Grade: F'], False, True]   (invalid starting marks stay at 0)
print(run_student("Meena", 50, [("GRADE",), ("SET", -1), ("SET", 75), ("GRADE",)]))
# Output: [['Grade: C', 'Invalid marks: -1. Marks stay 50', 'Marks updated to 75', 'Grade: B'], False, True]   (boundaries)
