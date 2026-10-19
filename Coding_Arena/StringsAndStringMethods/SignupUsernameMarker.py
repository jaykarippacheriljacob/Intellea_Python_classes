"""
    Signup Username Maker
    Easy
    Strings
    Given a full name, print a username and a welcome message.

    First remove the spaces at the start and end of the name.
    The username is the name in lowercase with each space replaced by _.
    The welcome message shows the name in title case.
    Input Format

    Line 1: full name (may have extra spaces at the start and end)
    Output Format

    Line 1: Username: <username>
    Line 2: Welcome, <Name In Title Case>!
    Examples

    Input: riya SHARMA
    Output: Username: riya_sharma Welcome, Riya Sharma!
    Explanation: After strip() the name is riya SHARMA. lower() and replace() build the username, and title() builds the welcome name.
    Input: arun
    Output: Username: arun Welcome, Arun!
    Explanation: A one word name has no spaces to replace.
    Constraints

    The name has 1 to 5 words of letters, with single spaces between words
    Use string methods and f-strings. Do not use lists or split()
"""

# Read the full name
full_name = input()

# Remove spaces at the start and end
full_name = full_name.strip()
# Capitalize the first letter of each word, e.g. "jay jacob" → "Jay Jacob"
full_name = full_name.title()
# Build the username in lowercase
username = full_name.lower()
# Replace spaces with underscores, e.g. "jay jacob" → "jay_jacob"
username = username.replace(" ", "_")
# Display the results
print(f"Username: {username}")
print(f"Welcome, {full_name}!")

# Test cases: different name inputs
test_cases = [
    "jay jacob",           # Username: jay_jacob, Welcome, Jay Jacob!
    "  PRIYA NAIR  ",      # Username: priya_nair, Welcome, Priya Nair!
    "arun",                # Username: arun, Welcome, Arun!
    "jay k jacob",         # Username: jay_k_jacob, Welcome, Jay K Jacob!
    "mIxEd CaSe NaMe",     # Username: mixed_case_name, Welcome, Mixed Case Name!
]

# Run the same steps for each test case
for t, name in enumerate(test_cases, start=1):
    print(f"\n--- Test {t}: '{name}' ---")
    name = name.strip().title()
    user = name.lower().replace(" ", "_")
    print(f"Username: {user}")
    print(f"Welcome, {name}!")
    