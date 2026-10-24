""" 
    Tournament Leaderboard
    Hard
    Built-in Functions
    Each player is a tuple (name, scores) with three round scores. A player's total is the sum of the scores. Implement these functions.

    rank_players(players) returns (name, total) tuples sorted by total, highest first. Equal totals are ordered by name alphabetically. Use map() and sorted().
    rank_lines(ranked) returns lines like Rank 1: Asha (240), using enumerate().
    top_scorer(players) returns (score, name) for the highest single round score, using max(). On a tie, the player entered first wins.
    consistent_players(players) returns, in input order, the names of players whose lowest score is at least 50, using filter().
    team_code(ranked) joins the first letter of each name in rank order, using reduce().
    average_total(players) returns the sum of all totals // the number of players.
    The function run_tournament is already written. It uses your functions.

    Parameters

    players: list of (name, scores) pairs; scores is a list of three whole numbers
    Returns

    A list of five parts from run_tournament:

    the rank lines
    the (score, name) of the top scorer
    the consistent player names
    the team code
    the average total
    Examples

    Arguments: [('Asha', [80, 70, 90]), ('Ravi', [98, 20, 60]), ('Meena', [60, 65, 70])]
    Returns: [['Rank 1: Asha (240)', 'Rank 2: Meena (195)', 'Rank 3: Ravi (178)'], (98, 'Ravi'), ['Asha', 'Meena'], 'AMR', 204]
    Explanation: The totals are Asha 240, Ravi 178 and Meena 195. Ravi's lowest score is 20, so he is not consistent. 613 // 3 is 204. The team code is the first letters A, M, R.
    Constraints

    1 <= number of players <= 15
    Names have only letters, no spaces, and all names are different
    0 <= each score <= 100
    Use map(), filter(), reduce(), sorted(), enumerate(), max(), min() and sum(). Convert the results of map() and filter() to lists
    Return the results. Do not print inside the functions
"""

from functools import reduce


def rank_players(players):
    # Build (name, total) for each player
    result = []
    for p in players:
        total = 0
        # p[0] is the name, p[1] is the list of three scores
        for i in range(len(p[1])):
            total += p[1][i]
        result.append((p[0], total))
    # Sort by name A-Z first, then by total highest first
    # (sort is stable, so equal totals keep the A-Z order)
    result.sort(key=lambda t: t[0])
    result.sort(key=lambda t: t[1], reverse=True)
    return result

    # Alternative using map(), sum() and sorted() (as the question asks):
    # totals = list(map(lambda p: (p[0], sum(p[1])), players))
    # return sorted(totals, key=lambda t: (-t[1], t[0]))


def rank_lines(ranked):
    # One line per player, numbered from 1 in rank order (uses enumerate as required)
    result = []
    for i, (n, s) in enumerate(ranked):
        result.append("Rank " + str(i+1) + ": " + n + " (" + str(s) + ")" )
    return result


def top_scorer(players):
    # Track the highest single round score and who scored it
    top = -1
    name = []
    for (n, score) in players:
        for s in score:
            # Strictly greater, so on a tie the player entered first stays
            if top < s:
                name.append(n)
                top = s
    # The last name added belongs to the highest score
    return (top, name[-1])

    # Alternative using max() (as the question asks):
    # pairs = [(s, n) for n, scores in players for s in scores]
    # return max(pairs, key=lambda t: t[0])


def consistent_players(players):
    # Names of players whose every score is at least 50, in input order
    result = []
    for (n, score) in players:
        l = len(score)
        c = 0
        # Count the scores that are 50 or more
        for s in score:
            if s >= 50:
                c += 1
        # Consistent only if all scores passed
        if c == l:
            result.append(n)
    return result

    # Alternative using filter(), min() and map() (as the question asks):
    # consistent = list(filter(lambda p: min(p[1]) >= 50, players))
    # return list(map(lambda p: p[0], consistent))


def team_code(ranked):
    # Start with "" and add the first letter of each name, in rank order (uses reduce as required)
    code = reduce(lambda code, t: code + t[0][0], ranked, "")
    return code


def average_total(players):
    # Add up every score of every player (the sum of all totals)
    avg = 0
    for (p, score) in players:
        for s in score:
            avg += s
    # Floor-divide by the number of players
    return avg // len(players)

    # Alternative using sum() and map() (as the question asks):
    # return sum(map(lambda p: sum(p[1]), players)) // len(players)


# Do not change the code below
def run_tournament(players):
    ranked = rank_players(players)
    return [
        rank_lines(ranked),
        top_scorer(players),
        consistent_players(players),
        team_code(ranked),
        average_total(players),
    ]


# Test cases
print(run_tournament([('Asha', [80, 70, 90]), ('Ravi', [98, 20, 60]), ('Meena', [60, 65, 70])]))
# Output: [['Rank 1: Asha (240)', 'Rank 2: Meena (195)', 'Rank 3: Ravi (178)'], (98, 'Ravi'), ['Asha', 'Meena'], 'AMR', 204]
print(run_tournament([('Zoya', [50, 50, 100]), ('Arun', [100, 60, 40])]))
# Output: [['Rank 1: Arun (200)', 'Rank 2: Zoya (200)'], (100, 'Zoya'), ['Zoya'], 'AZ', 200]
print(run_tournament([('Dev', [0, 0, 0])]))
# Output: [['Rank 1: Dev (0)'], (0, 'Dev'), [], 'D', 0]
