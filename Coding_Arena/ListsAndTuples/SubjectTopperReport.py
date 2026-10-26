"""     
    Subject Topper Report
    Hard
    Lists
    Given the list names and the nested list marks, where marks[i] holds the 3 subject marks of names[i], work out three things:

    Each student's total, in input order.
    For each subject, the topper and their mark. On a tie, the student listed first wins.
    The names from the highest total to the lowest. All totals are different.
    Parameters

    names: list of student names
    marks: list of lists; marks[i] has 3 marks for names[i]
    Returns

    A tuple (totals, toppers, ranking):

    totals: list of totals, in input order
    toppers: 3 pairs (name, mark), one per subject
    ranking: list of names, highest total first
    Examples

    Arguments: ['Charu', 'Asha', 'Bala'] [[70, 60, 100], [80, 70, 90], [60, 95, 80]]
    Returns: ([230, 240, 235], [('Asha', 80), ('Bala', 95), ('Charu', 100)], ['Asha', 'Bala', 'Charu'])
    Explanation: The totals are 230, 240 and 235. Asha tops subject 1, Bala subject 2 and Charu subject 3, and the ranking is Asha, Bala, Charu.
    Constraints

    1 <= number of students <= 10
    0 <= mark <= 100
    Names have only letters and no spaces
    Use lists and nested lists. Do not use dictionaries, sum(), max(), min() or sorted()
"""

def topper_report(names, marks):
    # Total marks for each student, in input order
    total = []
    # Topper's name for each of the 3 subjects
    topper = ["", "", ""]
    # Highest mark in each subject (starts below any possible mark)
    m = [-1, -1, -1]
    # i is the student's position; m1, m2, m3 are their three marks
    for i, (m1, m2, m3) in enumerate(marks):
        t = m1 + m2 + m3
        total.append(t)
        # Subject 1: strictly greater, so the first student keeps a tie
        if m1 >  m[0]:
            m[0] = m1
            temp = topper.pop(0)
            topper.insert(0, names[i])
        # Subject 2
        if m2 >  m[1]:
            m[1] = m2
            temp = topper.pop(1)
            topper.insert(1, names[i])
        # Subject 3
        if m3 >  m[2]:
            m[2] = m3
            temp = topper.pop(2)
            topper.insert(2, names[i])
    # Totals sorted highest first (a copy, so total stays in input order)
    temp = total.copy()
    temp.sort(reverse = True)
    # Copies of names and totals in input order; the same index means the same student
    tn = names.copy() 
    tt = total.copy()                    
    highest_mark_name = []
    # For each total from highest to lowest, find the matching student
    for mark in temp:
        for i in range(len(tt)):
            if tt[i] == mark:
                # Remove from both copies, so a tied student is found next time
                highest_mark_name.append(tn.pop(i))
                tt.pop(i)
                break
    # Pair each subject's topper with their mark
    combo = [(topper[i], m[i]) for i in range(len(m))]
    return (total, combo, highest_mark_name)


# Test cases
print(topper_report(['Charu', 'Asha', 'Bala'], [[70, 60, 100], [80, 70, 90], [60, 95, 80]]))
# Output: ([230, 240, 235], [('Asha', 80), ('Bala', 95), ('Charu', 100)], ['Asha', 'Bala', 'Charu'])
print(topper_report(['Zoya', 'Arun'], [[90, 90, 90], [50, 50, 50]]))
# Output: ([270, 150], [('Zoya', 90), ('Zoya', 90), ('Zoya', 90)], ['Zoya', 'Arun'])   (one student tops every subject)
print(topper_report(['Ravi', 'Meena', 'Dev'], [[80, 70, 60], [60, 70, 80], [70, 70, 70]]))
# Output: ([210, 210, 210], [('Ravi', 80), ('Ravi', 70), ('Meena', 80)], ['Ravi', 'Meena', 'Dev'])   (all totals tie → input order)
print(topper_report(['Kiran'], [[0, 0, 0]]))
# Output: ([0], [('Kiran', 0), ('Kiran', 0), ('Kiran', 0)], ['Kiran'])   (all zeros: -1 start still records Kiran)

            
