"""
Write a function:

def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.

"""

from collections import Counter

def solution(A):
    result = 0
    counts = Counter(A)
    for value in counts:
        if counts[value]%2 == 1:
            result = value
    return result
        
print(solution([9, 3, 9, 3, 9, 7, 9]))