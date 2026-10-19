"""
    Password Strength Checker
    Hard
    Strings
    Given a username and a password, check these rules in order:

    At least 8 characters.
    At least one capital letter.
    At least one small letter.
    At least one digit.
    At least one special character (not a letter and not a digit).
    Does not contain the username, ignoring case.
    If all pass, print Strong password. Otherwise print Weak password, then the message of each failed rule in rule order.

    Input Format

    Line 1: username
    Line 2: password
    Output Format

    Strong password
    or Weak password, then one line for each failed rule, using these exact messages:
    Needs at least 8 characters
    Needs a capital letter
    Needs a small letter
    Needs a digit
    Needs a special character
    Must not contain the username
    Examples

    Input: priya Priya123
    Output: Weak password Needs a special character Must not contain the username
    Explanation: There is no special character, and Priya123 contains priya when case is ignored.
    Input: dev abc
    Output: Weak password Needs at least 8 characters Needs a capital letter Needs a digit Needs a special character
    Explanation: abc is short and has only small letters.
    Constraints

    The username has only letters and is 3 to 20 characters long
    The password has 1 to 50 characters and no spaces
    Use a for loop over the string and string methods. Do not use lists
"""


username = input()
password = input()

# Flags for the character rules, all False until a matching character is found
has_upper = False
has_lower = False
has_digit = False
has_special = False

# Loop through each character once and record what types appear
for ch in password:
    # Capital letter found
    if ch.isupper():
        has_upper = True
    # Small letter found
    elif ch.islower():
        has_lower = True
    # Digit found
    elif ch.isdigit():
        has_digit = True
    # Not a letter and not a digit, so it's a special character
    else:
        has_special = True

# Rule 1: password must have at least 8 characters
long_enough = len(password) >= 8
# Rule 6: username must not appear in the password, ignoring case
no_username = username.lower() not in password.lower()

# All six rules passed
if long_enough and has_upper and has_lower and has_digit and has_special and no_username:
    print("Strong password")
# At least one rule failed: print the header, then each failed rule in order
else:
    print("Weak password")
    if not long_enough:
        print("Needs at least 8 characters")
    if not has_upper:
        print("Needs a capital letter")
    if not has_lower:
        print("Needs a small letter")
    if not has_digit:
        print("Needs a digit")
    if not has_special:
        print("Needs a special character")
    if not no_username:
        print("Must not contain the username")

# Test cases: (username, password) pairs, stored in a tuple since lists aren't allowed
test_cases = (
    ("priya", "Priya123"),      # Weak: special character, username
    ("dev", "abc"),             # Weak: 8 characters, capital, digit, special character
    ("jay", "Secure@2026"),     # Strong password
    ("arun", "ARUN@2026x"),     # Weak: username (case ignored)
    ("ravi", "Ab1@"),           # Weak: 8 characters
)

# Run the same checks for each test case
for t, (user, pwd) in enumerate(test_cases, start=1):
    print(f"\n--- Test {t}: {user} / {pwd} ---")
    up = lo = dg = sp = False
    for ch in pwd:
        if ch.isupper():
            up = True
        elif ch.islower():
            lo = True
        elif ch.isdigit():
            dg = True
        else:
            sp = True
    ln = len(pwd) >= 8
    nu = user.lower() not in pwd.lower()
    if ln and up and lo and dg and sp and nu:
        print("Strong password")
    else:
        print("Weak password")
        if not ln:
            print("Needs at least 8 characters")
        if not up:
            print("Needs a capital letter")
        if not lo:
            print("Needs a small letter")
        if not dg:
            print("Needs a digit")
        if not sp:
            print("Needs a special character")
        if not nu:
            print("Must not contain the username")
            