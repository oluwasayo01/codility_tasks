from collections import Counter

def solution(A):
    result = 0
    counts = Counter(A)
    for value in counts:
        if counts[value]%2 == 1:
            result = value
    return result
        
# print(solution([9, 3, 9, 3, 9, 7, 9]))