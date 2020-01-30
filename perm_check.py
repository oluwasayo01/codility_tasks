def solution(A):
    actual_sum = sum(range(len(A) + 1))
    list_sum = sum(A)
    actual_length = len(set(A))
    if (list_sum == actual_sum) and (actual_length == len(A)):
        return 1
    return 0

# print(solution([4, 1, 3, 2]))
# print(solution([4, 1, 3]))