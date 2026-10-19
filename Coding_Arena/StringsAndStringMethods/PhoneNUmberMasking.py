"""
    Phone Number Masking
    Medium
    Strings
    Given a phone number as typed, print it masked, or print Invalid number.

    Remove all spaces and hyphens.
    Then, if it starts with +91, remove those 3 characters.
    It is valid only if exactly 10 characters remain and all are digits.
    The masked form is the first 2 digits, six * symbols, then the last 2 digits.
    Input Format

    Line 1: phone number as typed
    Output Format

    Line 1: Masked: <masked number>
    or Line 1: Invalid number
    Examples

    Input: +91 98765 43210
    Output: Masked: 98******10
    Explanation: Without spaces it is +919876543210. Removing +91 leaves 9876543210, which is valid.
    Input: 98765-4321
    Output: Invalid number
    Explanation: Without the hyphen only 9 digits remain.
    Constraints

    The input has 1 to 25 characters
    Use string methods, indexing and slicing. Do not use lists or loops
"""

# Read the phone number as typed
number = input()

# Remove all spaces and hyphens first
number = number.replace("-", "")
number = number.replace(" ", "")
# Remove the country code only if it's at the start
if number.startswith("+91"):
    number = number[3:]
# Valid only if exactly 10 characters remain and all are digits
if len(number) != 10 or not number.isdigit():
    print("Invalid number")
else:
    # Keep the first 2 digits
    m1 = number[:2]
    # Keep the last 2 digits
    m3 = number[-2:]
    # Hide the middle 6 digits
    m2 = "******"
    # Join the parts to form the masked number
    masked = m1 + m2 + m3
    print(f"Masked: {masked}")

# Test cases (written without loops or lists, since the problem doesn't allow them)
# Test 1: spaces with country code → Masked: 98******10
t = "+91 98765 43210".replace("-", "").replace(" ", "")
t = t[3:] if t.startswith("+91") else t
print("Invalid number" if len(t) != 10 or not t.isdigit() else f"Masked: {t[:2]}******{t[-2:]}")

# Test 2: only 9 digits → Invalid number
t = "98765-4321".replace("-", "").replace(" ", "")
t = t[3:] if t.startswith("+91") else t
print("Invalid number" if len(t) != 10 or not t.isdigit() else f"Masked: {t[:2]}******{t[-2:]}")

# Test 3: hyphens with country code → Masked: 98******10
t = "+91-98765-43210".replace("-", "").replace(" ", "")
t = t[3:] if t.startswith("+91") else t
print("Invalid number" if len(t) != 10 or not t.isdigit() else f"Masked: {t[:2]}******{t[-2:]}")

# Test 4: separator between + and 91 → Masked: 98******10
t = "+ 91 9876543210".replace("-", "").replace(" ", "")
t = t[3:] if t.startswith("+91") else t
print("Invalid number" if len(t) != 10 or not t.isdigit() else f"Masked: {t[:2]}******{t[-2:]}")

# Test 5: letters inside → Invalid number
t = "98765abc10".replace("-", "").replace(" ", "")
t = t[3:] if t.startswith("+91") else t
print("Invalid number" if len(t) != 10 or not t.isdigit() else f"Masked: {t[:2]}******{t[-2:]}")
