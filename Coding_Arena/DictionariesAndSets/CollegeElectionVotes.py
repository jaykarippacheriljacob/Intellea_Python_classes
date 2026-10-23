"""
    College Election Votes
    Medium
    Dictionaries
    Given a list ballots where each entry is a candidate name, count the votes of each candidate with a dictionary, with candidates in the order they first appear. The winner has the most votes. If candidates tie, the one who appears first wins.

    Parameters

    ballots: list of candidate names, one per vote
    Returns

    A tuple (votes, winner, winner_votes):

    votes: dictionary of candidate to vote count, in order of first appearance
    winner: name of the winner
    winner_votes: the winner's vote count
    Examples

    Arguments: ['Asha', 'Ravi', 'Asha', 'Meena', 'Ravi', 'Asha']
    Returns: ({'Asha': 3, 'Ravi': 2, 'Meena': 1}, 'Asha', 3)
    Explanation: Asha has 3 votes, Ravi 2 and Meena 1.
    Arguments: ['Ravi', 'Asha', 'Asha', 'Ravi']
    Returns: ({'Ravi': 2, 'Asha': 2}, 'Ravi', 2)
    Explanation: Ravi and Asha tie at 2, and Ravi appears first.
    Constraints

    1 <= len(ballots) <= 100
    Names have only letters and no spaces and are case sensitive
    Use a dictionary and get(). Do not use sum(), max(), min() or sorted()
"""

def count_votes(ballots):
    # Dictionary to count votes for each candidate
    votes = {}
    for vote in ballots:
        # First vote for this candidate: start at 1
        if vote not in votes:
            votes[vote] = 1
        # Already seen: add one more vote
        else:
            votes[vote] += 1
    # Candidate with the most votes
    winner = max(votes, key=votes.get)
    return (votes, winner, votes[winner])


# Test cases
print(count_votes(["Asha", "Ravi", "Asha", "Meena", "Asha", "Ravi"]))
# Output: ({'Asha': 3, 'Ravi': 2, 'Meena': 1}, 'Asha', 3)
print(count_votes(["Ravi"]))
# Output: ({'Ravi': 1}, 'Ravi', 1)
