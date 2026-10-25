""" 
    Company Payroll Classes
    Medium
    Inheritance and Method Overriding
    Implement the Employee classes and two functions.

    Employee(name, base_salary): role() returns Employee, monthly_pay() returns base_salary, describe() returns <role()>: <name> earns <monthly_pay()>.
    Manager(name, base_salary, team_size), Developer(name, base_salary, bug_fixes) and Intern(name, base_salary) override role() with their class name. monthly_pay() adds 1000 per team member (Manager) or 200 per bug fix (Developer) to the parent pay, or halves the parent pay with // 2 (Intern).
    total_payroll(staff) returns the sum of all monthly_pay().
    highest_paid(staff) returns the name with the highest monthly_pay(), first on a tie.
    payroll_report is already written and uses your code.

    Parameters

    staff: list of tuples: (kind, name, base_salary) for employee and intern, (kind, name, base_salary, team_size) for manager, (kind, name, base_salary, bug_fixes) for developer; kind is employee, manager, developer or intern
    Returns

    A list [lines, total, top]: lines is the list of describe() texts in input order, total is total_payroll(staff) and top is highest_paid(staff).

    Examples

    Arguments: [('manager', 'Asha', 50000, 5), ('developer', 'Ravi', 40000, 10), ('intern', 'Meena', 10000), ('employee', 'Dev', 30000)]
    Returns: [['Manager: Asha earns 55000', 'Developer: Ravi earns 42000', 'Intern: Meena earns 5000', 'Employee: Dev earns 30000'], 132000, 'Asha']
    Explanation: Asha earns 50000 + 5 x 1000, Ravi earns 40000 + 10 x 200 and Meena earns half of 10000. One describe() method gives all four lines, the total is 132000 and Asha is the highest paid.
    Constraints

    1 <= number of staff <= 20
    Names have only letters and no spaces
    0 <= base_salary <= 1000000
    0 <= team_size, bug_fixes <= 1000
    Use super() in the child classes. Do not copy the base salary logic into them
 """

class Employee:
    def __init__(self, name, base_salary):
        # Store the shared details for every kind of employee
        self.name = name
        self.base_salary = base_salary

    def role(self):
        # Default role name; child classes override this
        return "Employee"

    def monthly_pay(self):
        # Base pay; child classes build on this with super()
        return self.base_salary

    def describe(self):
        # Calls role() and monthly_pay(), so each child's overrides are used automatically (polymorphism)
        return f"{self.role()}: {self.name} earns {self.monthly_pay()}"


class Manager(Employee):
    def __init__(self, name, base_salary, team_size):
        # Parent sets name and base_salary; the child adds team_size
        super().__init__(name, base_salary)
        self.team_size = team_size

    def role(self):
        # Overrides the parent's role
        return "Manager"

    def monthly_pay(self):
        # Parent pay plus 1000 per team member
        return (super().monthly_pay() + 1000 * self.team_size)


class Developer(Employee):
    def __init__(self, name, base_salary, bug_fixes):
        # Parent sets name and base_salary; the child adds bug_fixes
        super().__init__(name, base_salary)
        self.bug_fix = bug_fixes

    def role(self):
        # Overrides the parent's role
        return "Developer"

    def monthly_pay(self):
        # Parent pay plus 200 per bug fix
        return super().monthly_pay() + 200 * self.bug_fix


class Intern(Employee):
    # No __init__ needed: the parent's (name, base_salary) already fits

    def role(self):
        # Overrides the parent's role
        return "Intern"

    def monthly_pay(self):
        # Half the parent pay, floored with //
        return super().monthly_pay() // 2


def total_payroll(staff):
    # Add up everyone's monthly pay
    total = 0
    for s in staff:
        total += s.monthly_pay()
    return total

    # Shorter alternative using sum() with a generator expression:
    # return sum(s.monthly_pay() for s in staff)
    # Or using sum() with map():
    # return sum(map(lambda s: s.monthly_pay(), staff))


def highest_paid(staff):
    # Track the highest pay so far and record a name each time it's beaten
    m = 0
    hp = []
    for s in staff:
        # Strictly greater, so on a tie the first person stays
        if s.monthly_pay() > m:
            m = s.monthly_pay()
            hp.append(s.name)
    # The last name recorded belongs to the highest pay
    return hp[-1]

    # Shorter alternative using max() with a key (returns the first one on a tie):
    # return max(staff, key=lambda s: s.monthly_pay()).name

# Do not change the code below
def payroll_report(staff):
    people = []
    for entry in staff:
        kind, name, base = entry[0], entry[1], entry[2]
        if kind == "manager":
            people.append(Manager(name, base, entry[3]))
        elif kind == "developer":
            people.append(Developer(name, base, entry[3]))
        elif kind == "intern":
            people.append(Intern(name, base))
        else:
            people.append(Employee(name, base))
    lines = []
    for person in people:
        lines.append(person.describe())
    return [lines, total_payroll(people), highest_paid(people)]


# Test cases
print(payroll_report([('manager', 'Asha', 50000, 5), ('developer', 'Ravi', 40000, 10), ('intern', 'Meena', 10000), ('employee', 'Dev', 30000)]))
# Output: [['Manager: Asha earns 55000', 'Developer: Ravi earns 42000', 'Intern: Meena earns 5000', 'Employee: Dev earns 30000'], 132000, 'Asha']
print(payroll_report([('employee', 'Arun', 40000), ('developer', 'Zoya', 38000, 10)]))
# Output: [['Employee: Arun earns 40000', 'Developer: Zoya earns 40000'], 80000, 'Arun']   (tie → first)
print(payroll_report([('intern', 'Kiran', 15001)]))
# Output: [['Intern: Kiran earns 7500'], 7500, 'Kiran']   (15001 // 2 = 7500)
# print(payroll_report([('employee', 'Nila', 0)]))
# Expected: [['Employee: Nila earns 0'], 0, 'Nila']
# Your code: IndexError, since 0 > 0 is never true and hp stays empty
