def solution(X, A):
    distances = set()
    for index, value in enumerate(A):
        distances.add(value)
        if len(distances) == X:
            return index
    return -1

print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))