
def solution(A):
    found = [0] * len(A)
    for value in A:
        if 0 < value <= len(A):
            found[value%len(A)-1] = 1
    for index, value in enumerate(found):
        if value == 0:
            return index + 1
    return len(A) + 1

print(solution([1, 3, 6, 4, 1, 2]))