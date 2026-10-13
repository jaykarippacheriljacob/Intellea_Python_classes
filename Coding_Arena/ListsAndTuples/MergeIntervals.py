"""
    Merge Intervals
    Medium
    Arrays & Lists
    Given a collection of intervals, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
    An interval is represented as a pair of integers [start, end].

    Details

    Two intervals [start1, end1] and [start2, end2] are considered overlapping if they have some common points. This includes cases where they touch at an endpoint. For example, [1,4] and [4,5] are considered overlapping.

    The input list of intervals is not guaranteed to be sorted.

    Examples

    Arguments: [[1, 3], [2, 6], [8, 10], [15, 18]]
    Returns: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlap, they are merged into [1,6].
    Arguments: [[1, 4], [4, 5]]
    Returns: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping because they touch at the number 4. They merge to form [1,5].
    Arguments: [[1, 4], [0, 2], [3, 5]]
    Returns: [[0,5]]
    Explanation: After sorting, the intervals are [[0,2],[1,4],[3,5]]. [0,2] overlaps with [1,4] to form [0,4]. Then, [0,4] overlaps with [3,5] to form [0,5].
    Constraints

    <ul><li><code>1 &lt;= intervals.length &lt;= 10<sup>4</sup></code></li><li><code>intervals[i].length == 2</code></li><li><code>0 &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt;= 10<sup>4</sup></code></li></ul>
"""

def merge(intervals: list[list[int]]) -> list[list[int]]:
   """
       Merge all overlapping intervals.

       Parameters:
       intervals (list): A list of [start, end] pairs.

       Returns:
       list: A list of non-overlapping intervals covering all input intervals.
   """
   # Sort intervals by start value so overlapping ones sit next to each other
   intervals.sort()
   # i points to the current interval, j to the next one to compare
   i = 0
   j = 1
   # Track the current length of the list as items get removed
   l = len(intervals)
   # Continue while both pointers are within the list
   while i < l and j < l:
       # Overlap: the next interval starts before or when the current one ends
       if intervals[i][1] >= intervals[j][0]:
           # Remove the overlapping interval; the following one slides into position j
           interval = intervals.pop(j)
           # Extend the current interval only if the removed one ends further right
           if intervals[i][1] < interval[1]:
               intervals[i][1] = interval[1]
           # The list is now one item shorter
           l -=1
       # No overlap: move both pointers one step forward
       else:
           i += 1
           j += 1
   return intervals

# Example usage
print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # Output: [[1, 6], [8, 10], [15, 18]]
print(merge([[1, 4], [4, 5]]))                     # Output: [[1, 5]]
print(merge([[1, 10], [2, 3], [4, 5]]))            # Output: [[1, 10]]
print(merge([[1, 4], [2, 6], [5, 8]]))             # Output: [[1, 8]]
print(merge([]))                                   # Output: []