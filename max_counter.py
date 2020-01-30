"""Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1]."""

def solution(N, A):
    counter = [0] * N
    initial_count = 0
    current_count = 0
    list_set = set(A)
    set_list = list(list_set)
    if len(set_list) == 1 and set_list[0] == N + 1:
        return counter
    for value in A:
        if 1 <= value <= N:
            # initial_count = counter[value - 1]
            current_count = counter[value - 1] + 1
            counter[value - 1] += 1
            if initial_count < current_count:
                initial_count = current_count
        if value == N + 1:
            counter = [initial_count] * N
    return counter


print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
