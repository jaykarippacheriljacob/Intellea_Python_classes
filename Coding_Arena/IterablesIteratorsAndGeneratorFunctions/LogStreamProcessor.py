""" 
    Log Stream Processor
    Medium
    Iterators, Generators and Decorators
    Write four generator functions that form a lazy pipeline. Each one must use yield and must not build a list.

    clean(lines) yields each line with spaces stripped from both ends, skipping lines that are empty after stripping.
    only_errors(lines) yields only the lines that start with ERROR (capital letters only).
    numbered(lines) yields <k>. <line> with k starting at 1.
    first_n(items, n) yields the first n items, then stops without asking for another item. If n is 0 or less, it yields nothing and asks for no item at all.
    The function run_pipeline is already written. It reads the log through a counting source, so a lazy pipeline reads only as many lines as it needs.

    Parameters

    log_lines: list of log lines; a line can have spaces at either end or be empty
    wanted: how many error lines are wanted
    Returns

    A list [result, reads] given by run_pipeline.

    result: the wanted error lines, numbered, in log order
    reads: how many log lines were read from the source
    Examples

    Arguments: ['INFO server started', ' ERROR disk almost full', '', 'WARN low memory', 'ERROR login failed for admin', 'ERROR timeout', 'INFO stopped'] 2
    Returns: [['1. ERROR disk almost full', '2. ERROR login failed for admin'], 5]
    Explanation: The second error is on log line 5, and first_n stops right there, so the last two lines are never read. The result has 2 lines and reads is 5.
    Arguments: ['ERROR a', 'ERROR b', 'ERROR c'] 0
    Returns: [[], 0]
    Explanation: n is 0, so first_n returns before asking for any line. The result is empty and reads is 0.
    Constraints

    1 <= number of log lines <= 50
    0 <= wanted <= 60
    Each of the four functions must use yield. Do not call list() on the input
 """

def clean(lines):
    for line in lines:
        # strip() returns a new string, so store it back
        line = line.strip()
        # An empty string is falsy, so blank lines are skipped
        if line:
            yield line


def only_errors(lines):
    for line in lines:
        # Keep only lines starting with "ERROR" (case-sensitive)
        if line.startswith("ERROR"):
            yield line


def numbered(lines):
    # Line number, starting at 1
    counter = 1
    for line in lines:
        # e.g. "1. ERROR disk almost full"
        yield str(counter) + ". " + line
        counter += 1

    # Shorter alternative using enumerate() and an f-string:
    # for k, line in enumerate(lines, start=1):
    #     yield f"{k}. {line}"


def first_n(items, n):
    # n is 0 or less: end before asking for any item
    if n <= 0:
        return
    # How many items have been handed over so far
    count = 0
    for item in items:
        yield item
        count += 1
        # Stop right after the nth item, before the loop fetches another
        if count == n:
            return


# Do not change the code below
def run_pipeline(log_lines, wanted):
    reads = 0

    def source():
        nonlocal reads
        for text in log_lines:
            reads = reads + 1
            yield text

    errors = only_errors(clean(source()))
    result = []
    for line in numbered(first_n(errors, wanted)):
        result.append(line)
    return [result, reads]


# Test cases
print(run_pipeline(['INFO server started', '  ERROR disk almost full', '', 'WARN low memory', 'ERROR login failed for admin', 'ERROR timeout', 'INFO stopped'], 2))
# Output: [['1. ERROR disk almost full', '2. ERROR login failed for admin'], 5]
print(run_pipeline(['ERROR a', 'ERROR b', 'ERROR c'], 0))
# Output: [[], 0]   (n = 0: nothing is read)
print(run_pipeline(['ERROR a', 'INFO b', 'ERROR c'], 10))
# Output: [['1. ERROR a', '2. ERROR c'], 3]   (fewer errors than wanted: whole log read)
print(run_pipeline(['error lower', 'Error mixed', '   ', 'ERRORS spelled'], 1))
# Output: [['1. ERRORS spelled'], 4]   (only capital ERROR counts; spaces-only line skipped)
