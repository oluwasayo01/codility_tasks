def solution(A):
    arr_set = set(A)
    arr_set.add(0)
    complete_set = set(range(len(arr_set) + 1))
    result = list(complete_set.difference(arr_set))
    return result[0]

# print(solution([2, 3, 1, 5]))