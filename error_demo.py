# 1. Error (exception) - A problem detected while the program runs; if unhandled, the program stops with a traceback.

# 2. Common exceptions:
# ValueError        - Right type but invalid value, e.g. int("hello")
# ZeroDivisionError - Dividing by zero, e.g. 10 / 0
# FileNotFoundError - Opening a file that doesn't exist in "r" mode
# TypeError         - Operation on the wrong type, e.g. "5" + 5
# IndexError        - List index out of range, e.g. [1, 2][5]
# KeyError          - Missing dictionary key, e.g. {"a": 1}["b"]
# NameError         - Using a variable that isn't defined

# 3. try / except - Runs the code in try; if an error occurs, jumps to except instead of crashing.
print("\n--- 3. try/except: enter text (e.g. abc) to see the error handled ---")
try:
    number = int(input("Enter a number: "))
except:
    print("Invalid input")

# 4. Specific exception - Catches only the named error; preferred over a bare except.
print("\n--- 4. Specific exception: converting 'hello' to int ---")
try:
    number = int("hello")
except ValueError:
    print("Please enter a whole number")

# 5. Multiple except blocks - Handles different errors in different ways; only the first match runs.
print("\n--- 5. Multiple excepts: enter text for ValueError, or 0 for ZeroDivisionError ---")
try:
    result = 10 / int(input("Enter divisor: "))
except ValueError:
    print("Not a number")
except ZeroDivisionError:
    print("Cannot divide by zero")

# 6. Tuple of exceptions - Handles several errors with the same message.
print("\n--- 6. Tuple of exceptions: enter text or 0, both give the same message ---")
try:
    result = 10 / int(input("Enter divisor: "))
except (ValueError, ZeroDivisionError):
    print("Invalid divisor")

# 7. as e - Stores the error object so its message can be shown.
print("\n--- 7. as e: opening a file that doesn't exist ---")
try:
    open("unknown.txt", "r")
except FileNotFoundError as e:
    print("Error:", e)

# 8. else - Runs only if no error occurred in try.
print("\n--- 8. else: converting '25', which succeeds ---")
try:
    number = int("25")
except ValueError:
    print("Invalid")
else:
    print("Success:", number)

# 9. finally - Always runs, error or not; used for cleanup like closing a file.
print("\n--- 9. finally: runs whether students.txt exists or not ---")
try:
    file = open("students.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File missing")
finally:
    print("Done")

# 10. raise - Triggers an error yourself when a value breaks your rules; unhandled, it stops the program.
# (Kept as a comment, since running it would stop the program here.)
# marks = 150
# if marks > 100:
#     raise ValueError("Value must be between 0 and 100")

# 11. Exception - Catches almost any error; use it last, as a fallback after specific excepts.
print("\n--- 11. Exception: dividing by zero caught by the general fallback ---")
try:
    result = 10 / 0
except Exception as e:
    print("Something went wrong:", e)

# 12. raise inside try - Your own rule check is handled by the same except as Python's built-in errors.
print("\n--- 12. raise inside try: enter text, a mark outside 0-100, or a valid mark ---")
try:
    marks = int(input("Enter the mark: "))
    if marks > 100 or marks < 0:
        raise ValueError("Marks must be between 0 and 100")
    print(marks)
except ValueError as error:
    print(error)
else:
    print("Mark processed successfully")
finally:
    print("Program execution completed")
    