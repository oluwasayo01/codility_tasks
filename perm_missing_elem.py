"""
Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
"""

def solution(A):
    arr_set = set(A)
    arr_set.add(0)
    complete_set = set(range(len(arr_set) + 1))
    result = list(complete_set.difference(arr_set))
    return result[0]

print(solution([2, 3, 1, 5]))