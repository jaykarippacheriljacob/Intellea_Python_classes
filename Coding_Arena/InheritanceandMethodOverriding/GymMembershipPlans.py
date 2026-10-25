""" 
    Gym Membership Plans
    Medium
    super() and Encapsulation
    Implement the member classes and two functions.

    Member(name, fee) keeps public self.name, private self.__fee and protected self._visits = 0. visit() adds a visit, get_visits() returns it, label() returns Basic, monthly_bill() returns the fee, describe() returns "<label> <name>: <visits> visits, bill <bill>".
    PremiumMember(name, fee, trainer_fee): label Premium. Bill is fee + trainer_fee, less total // 10 at 20+ visits.
    StudentMember(name, fee, college): label Student (<college>). Bill is fee minus 100 (300 at 10+ visits), never below 0.
    total_collected(members) sums all bills.
    most_visits(members) gives the name with most visits (first on a tie).
    gym_report is already written and uses your code.

    Parameters

    members: list of tuples: (basic, name, fee), (premium, name, fee, trainer_fee) or (student, name, fee, college)
    visits: list of (name, times) records; each one makes that member visit times times
    Returns

    A list [lines, total, top]: lines is the describe() text of each member in order, total is total_collected(members) and top is most_visits(members).

    Examples

    Arguments: [('premium', 'Asha', 1500, 2000), ('student', 'Ravi', 1000, 'Anna University'), ('basic', 'Meena', 800)] [('Asha', 12), ('Ravi', 12), ('Meena', 3), ('Asha', 10)]
    Returns: [['Premium Asha: 22 visits, bill 3150', 'Student (Anna University) Ravi: 12 visits, bill 700', 'Basic Meena: 3 visits, bill 800'], 4650, 'Asha']
    Explanation: Asha has 22 visits, so her 1500 + 2000 = 3500 loses 350 and becomes 3150. Ravi has 12 visits, so he pays 1000 - 300 = 700. The total is 3150 + 700 + 800 = 4650.
    Constraints

    1 <= number of members <= 10 and 0 <= number of visit records <= 20
    Member names have only letters and numbers, and all names are different
    0 <= fee, trainer_fee <= 100000
    0 <= times <= 100 in one record
    A college name can have spaces and symbols
    Use super() in the child classes. A child class must not read self.__fee
 """

class Member:
    def __init__(self, name, fee):
        # Public: free to use anywhere
        self.name = name
        # Private: only Member's own methods can read it (child classes use monthly_bill())
        self.__fee = fee
        # Protected: meant for this class and its children
        self._visits = 0

    def visit(self):
        # Record one more visit
        self._visits += 1

    def get_visits(self):
        # Getter for the protected visit count
        return self._visits

    def label(self):
        # Default label; child classes override this
        return "Basic"

    def monthly_bill(self):
        # The only way children can reach the private fee (through super())
        return self.__fee

    def describe(self):
        # Uses each object's own label() and monthly_bill() (polymorphism)
        return f"{self.label()} {self.name}: {self.get_visits()} visits, bill {self.monthly_bill()}"


class PremiumMember(Member):
    def __init__(self, name, fee, trainer_fee):
        # Parent sets name, fee and visits; the child adds its own private trainer fee
        super().__init__(name, fee)
        self.__trainer_fee = trainer_fee

    def label(self):
        # Overrides the parent's label
        return "Premium"

    def monthly_bill(self):
        # Parent fee (via super(), not self.__fee) plus the trainer fee
        amount = super().monthly_bill() + self.__trainer_fee
        # 20 or more visits: subtract 10% of the total, floored
        if self.get_visits() >= 20:
            amount -= (amount // 10)
        return amount


class StudentMember(Member):
    def __init__(self, name, fee, college):
        # Parent sets name, fee and visits; the child adds the college
        super().__init__(name, fee)
        self.college = college

    def label(self):
        # e.g. "Student (Anna University)"
        return f"Student ({self.college})"

    def monthly_bill(self):
        # Discount of 300 at 10 or more visits, otherwise 100
        amount = 0
        if self._visits >= 10:
            amount =  super().monthly_bill() - 300
        else:
            amount =  super().monthly_bill() - 100
        # The bill can never go below 0
        if amount < 0:
            amount = 0
        return amount

        # Shorter alternative using a conditional expression and max():
        # discount = 300 if self._visits >= 10 else 100
        # return max(super().monthly_bill() - discount, 0)


def total_collected(members):
    # Add up every member's bill
    total = 0
    for mem in members:
        total += mem.monthly_bill()
    return total

    # Shorter alternative using sum() with a generator expression:
    # return sum(mem.monthly_bill() for mem in members)


def most_visits(members):
    # Start below any possible visit count, so the first member is always recorded
    name = []
    v = -1
    for mem in members:
        # Strictly greater, so on a tie the first member stays
        if mem.get_visits() > v:
            v = mem.get_visits()
            name.append(mem.name)
    # The last name recorded has the most visits
    return name[-1]

    # Shorter alternative using max() with a key (returns the first on a tie):
    # return max(members, key=lambda mem: mem.get_visits()).name


# Do not change the code below
def gym_report(members, visits):
    people = []
    by_name = {}
    for entry in members:
        kind, name, fee = entry[0], entry[1], entry[2]
        if kind == "premium":
            member = PremiumMember(name, fee, entry[3])
        elif kind == "student":
            member = StudentMember(name, fee, entry[3])
        else:
            member = Member(name, fee)
        people.append(member)
        by_name[name] = member
    for name, times in visits:
        for j in range(times):
            by_name[name].visit()
    lines = []
    for member in people:
        lines.append(member.describe())
    return [lines, total_collected(people), most_visits(people)]


# Test cases
print(gym_report([('premium', 'Asha', 1500, 2000), ('student', 'Ravi', 1000, 'Anna University'), ('basic', 'Meena', 800)],
                 [('Asha', 12), ('Ravi', 12), ('Meena', 3), ('Asha', 10)]))
# Output: [['Premium Asha: 22 visits, bill 3150', 'Student (Anna University) Ravi: 12 visits, bill 700', 'Basic Meena: 3 visits, bill 800'], 4650, 'Asha']
print(gym_report([('premium', 'Dev', 1000, 999), ('student', 'Zoya', 250, 'IIT-M & Co.')], [('Dev', 20), ('Zoya', 20)]))
# Output: [['Premium Dev: 20 visits, bill 1800', 'Student (IIT-M & Co.) Zoya: 20 visits, bill 0'], 1800, 'Dev']
# (exactly 20 visits: 1999 - 1999 // 10 = 1800; student bill 250 - 300 floors at 0; college with symbols)
print(gym_report([('basic', 'Arun', 500), ('student', 'Kiran', 80, 'CET')], []))
# Output: [['Basic Arun: 0 visits, bill 500', 'Student (CET) Kiran: 0 visits, bill 0'], 500, 'Arun']
# (no visit records: everyone at 0, the case that needed v = -1)
print(gym_report([('basic', 'A1', 100), ('basic', 'B2', 200)], [('B2', 5), ('A1', 5)]))
# Output: [['Basic A1: 5 visits, bill 100', 'Basic B2: 5 visits, bill 200'], 300, 'A1']
# (tie on visits: A1 comes first in the members list, so A1 wins)
