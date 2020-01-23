def solution(A):
    first, *rest = A
    result = []
    rest_sum = sum(rest)
    for index, value in enumerate(A):
        if index < len(A) - 1:
            result.append(abs(first - rest_sum))
            first += A[index + 1]
            rest_sum -= A[index + 1]
    return min(result)

print(solution([3, 1, 2, 4, 3]))