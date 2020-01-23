def solution(X, Y, D):
    gap = (Y - X)
    count = gap//D
    remainder = gap%D
    if remainder > 0:
        count+=1
    return count

print(solution(10, 85, 30))