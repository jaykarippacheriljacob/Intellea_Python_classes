""" 
    Ticket Number Iterator
    Easy
    Iterators, Generators and Decorators
    Implement TicketRange and ticket_stats.

    TicketRange(start, stop, step) gives the numbers from start, going up by step and stopping before stop.
    __iter__() returns self.
    __next__() returns the next number. Once the current number is at or past stop, it raises StopIteration, on every later call too.
    ticket_stats(tickets) loops over tickets and returns (numbers, count, total): the list, how many, and their sum.
    run_tickets is already written. It uses them.

    Parameters

    start: first ticket number
    stop: the numbers stop before this value
    step: amount added each time
    Returns

    A list [numbers, count, total, own_iterator, stopped] given by run_tickets.

    numbers, count, total: the result of ticket_stats
    own_iterator: True if iter(tickets) is tickets
    stopped: True if one more next(tickets) raises StopIteration
    Examples

    Arguments: 100 110 2
    Returns: [[100, 102, 104, 106, 108], 5, 520, True, True]
    Explanation: The numbers go up by 2 from 100. 110 is the stop, so it is not given out. There are 5 tickets with sum 520.
    Arguments: 5 5 1
    Returns: [[], 0, 0, True, True]
    Explanation: The start is already at the stop, so the very first __next__() raises StopIteration and the list is empty.
    Constraints

    -1000 <= start <= 1000 and -1000 <= stop <= 1000
    1 <= step <= 1000
    The range gives at most 50 tickets
    Do not use range(), yield or a list inside the class
 """

class TicketRange:
    def __init__(self, start, stop, step):
        # start doubles as the "next number to hand out"
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        # An iterator returns itself, so it works in for loops
        return self

    def __next__(self):
        # At or past stop: no more tickets (and start never changes after this)
        if self.start >= self.stop:
            raise StopIteration
        # Save the current number, then move forward for the next call
        value = self.start
        self.start += self.step
        return value


def ticket_stats(tickets):
    num = []
    count = 0
    total = 0
    # The for loop calls next() automatically and stops at StopIteration
    for t in tickets:
        count += 1
        total += t
        num.append(t)
    return (num, count, total)

    # Shorter alternative using built-ins:
    # num = list(tickets)
    # return (num, len(num), sum(num))


# Do not change the code below
def run_tickets(start, stop, step):
    tickets = TicketRange(start, stop, step)
    numbers, count, total = ticket_stats(tickets)
    own_iterator = iter(tickets) is tickets
    stopped = False
    try:
        next(tickets)
    except StopIteration:
        stopped = True
    return [numbers, count, total, own_iterator, stopped]


# Test cases
print(run_tickets(100, 110, 2))   # Output: [[100, 102, 104, 106, 108], 5, 520, True, True]
print(run_tickets(5, 5, 1))       # Output: [[], 0, 0, True, True]   (start already at stop)
print(run_tickets(1, 10, 4))      # Output: [[1, 5, 9], 3, 15, True, True]   (13 steps past stop)
print(run_tickets(-3, 2, 2))      # Output: [[-3, -1, 1], 3, -3, True, True]   (negative start)
print(run_tickets(10, 5, 1))      # Output: [[], 0, 0, True, True]   (start already past stop)

