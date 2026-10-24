""" 
    Loan EMI and Due Dates
    Hard
    Modules and Packages
    Implement these functions for a loan schedule using math and datetime.

    loan_summary(principal, rate, months) returns (emi, total, interest). If rate is 0, emi is math.ceil(principal / months). Otherwise let r = rate / 12 / 100 and growth = math.pow(1 + r, months), and emi is math.ceil(principal * r * growth / (growth - 1)). total is emi * months and interest is total - principal.
    add_months(start, k) returns the date k months after start (a datetime.date), on the same day number. If that month is too short, use its last day.
    format_date(d) returns the date like 05 Mar 2027.
    weekday_name(d) returns the full weekday name, like Tuesday.
    days_between(start, end) returns the number of days from start to end.
    The function loan_schedule is already written. It uses your functions.

    Parameters

    principal: loan amount
    rate: yearly interest rate in percent
    months: number of monthly payments
    year: start year
    month: start month, 1 to 12
    day: start day
    Returns

    A list of four parts from loan_schedule:

    (emi, total, interest)
    the due dates 1 to months as strings like 12 Nov 2026
    the weekday name of the last due date
    the days from the start to the last due date
    Examples

    Arguments: 120000 12 3 2026 10 12
    Returns: [(40803, 122409, 2409), ['12 Nov 2026', '12 Dec 2026', '12 Jan 2027'], 'Tuesday', 92]
    Explanation: The monthly rate is 0.01 and the EMI 40802.6... rounds up to 40803. 12 Jan 2027 is 92 days after the start.
    Arguments: 60000 0 4 2026 12 31
    Returns: [(15000, 60000, 0), ['31 Jan 2027', '28 Feb 2027', '31 Mar 2027', '30 Apr 2027'], 'Friday', 120]
    Explanation: February 2027 has 28 days, so Due 2 is 28 Feb. Due 3 goes back to day 31 because months are counted from the start date.
    Constraints

    1000 <= principal <= 1000000
    0 <= rate <= 36
    1 <= months <= 12
    The start date is a valid date between the years 2000 and 2100
    Import math and datetime. Do not install or use any other package
    Return the results. Do not print inside the functions
 """

import math
import datetime


def loan_summary(principal, rate, months):
    emi = 0
    # No interest: split the principal evenly, rounding up
    if rate == 0:
        emi = math.ceil(principal / months)
    # With interest: standard EMI formula, rounded up
    else:
        # Monthly rate as a decimal (yearly percent / 12 / 100)
        r = rate / 12 / 100
        # (1 + r) raised to the number of months
        growth = math.pow(1 + r, months)
        emi = math.ceil(principal * r * growth / (growth - 1))    
    # Total paid over all months, and the extra paid as interest
    total = emi * months
    interest = total - principal
    return (emi, total, interest)

def add_months(start, k):
    # Count months from 0 (Jan = 0) so // and % roll the year over correctly
    total = start.month + k - 1
    year = start.year + total // 12
    # Convert back to 1-12
    month = total % 12 + 1
    # Last day of the target month: the first of the next month, minus one day
    if month == 12:
        next_first = datetime.date(year + 1, 1, 1)
    else:
        next_first = datetime.date(year, month + 1, 1)
    last_day = (next_first - datetime.timedelta(days=1)).day
    # Keep the same day number, or use the last day if the month is too short
    day = min(start.day, last_day)
    # Dates can't be modified, so build and return a new one
    return datetime.date(year, month, day)


def format_date(d):
    # Day with leading zero, short month name, 4-digit year: 05 Mar 2027
    return d.strftime("%d %b %Y")


def weekday_name(d):
    # Full weekday name, like Tuesday
    return d.strftime("%A")


def days_between(start, end):
    # Subtracting dates gives a timedelta; .days is the whole number of days
    return (end - start).days


# Do not change the code below
def loan_schedule(principal, rate, months, year, month, day):
    start = datetime.date(year, month, day)
    last = add_months(start, months)
    dues = [format_date(add_months(start, k)) for k in range(1, months + 1)]
    return [
        loan_summary(principal, rate, months),
        dues,
        weekday_name(last),
        days_between(start, last),
    ]


# Test cases
print(loan_schedule(120000, 12, 3, 2026, 10, 12))
# Output: [(40803, 122409, 2409), ['12 Nov 2026', '12 Dec 2026', '12 Jan 2027'], 'Tuesday', 92]
print(loan_schedule(60000, 0, 4, 2026, 12, 31))
# Output: [(15000, 60000, 0), ['31 Jan 2027', '28 Feb 2027', '31 Mar 2027', '30 Apr 2027'], 'Friday', 120]
print(loan_schedule(50000, 10, 2, 2028, 1, 31))
# Output: [(25313, 50626, 626), ['29 Feb 2028', '31 Mar 2028'], 'Friday', 60]   (leap year: Feb has 29 days)
print(loan_schedule(1000, 36, 1, 2026, 5, 5))
# Output: [(1030, 1030, 30), ['05 Jun 2026'], 'Friday', 31]   (single month, highest rate)

