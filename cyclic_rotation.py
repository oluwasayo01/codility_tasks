def solution(A, K):
    for count in range(K):
        if len(A) > 0:
            popped = A.pop()
            A.insert(0, popped)
    return A

# print(solution([3, 8, 9, 7, 6], 3))