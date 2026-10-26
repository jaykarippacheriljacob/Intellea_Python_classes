"""
    Train Ticket Details
    Easy
    Tuples
    Given a train name, coach, seat number and fare, store them in a tuple ticket in that order. Then slice the tuple to get a new tuple that holds only the seat number and the fare.

    Parameters

    train: name of the train
    coach: coach name
    seat: seat number
    fare: ticket fare
    Returns

    A tuple (ticket, seat_and_fare):

    ticket: the tuple (train, coach, seat, fare)
    seat_and_fare: a tuple with only the seat and the fare
    Examples

    Arguments: 'Chennai Express' 'S4' 23 745.5
    Returns: (('Chennai Express', 'S4', 23, 745.5), (23, 745.5))
    Explanation: ticket[2:] starts at index 2 and returns the last two items as a new tuple.
    Arguments: 'Vande Bharat' 'C1' 7 1200.0
    Returns: (('Vande Bharat', 'C1', 7, 1200.0), (7, 1200.0))
    Explanation: The fare is a float, so 1200 is given as 1200.0.
    Constraints

    1 <= seat <= 100
    0 <= fare <= 100000, given as a float
    Use a tuple and slicing. Do not use lists
"""

def train_ticket(train, coach, seat, fare):
    # Return two tuples: the full ticket details, and just the seat and fare
    return (train,  coach, seat, fare), (seat, fare)


# Test cases
print(train_ticket("Vande Bharat", "C4", 42, 1650))
# Output: (('Vande Bharat', 'C4', 42, 1650), (42, 1650))
print(train_ticket("Kerala Express", "S2", 17, 545))
# Output: (('Kerala Express', 'S2', 17, 545), (17, 545))

# Unpacking the two returned tuples into separate variables
ticket, booking = train_ticket("Jan Shatabdi", "D1", 5, 320)
print(ticket)    # ('Jan Shatabdi', 'D1', 5, 320)
print(booking)   # (5, 320)
