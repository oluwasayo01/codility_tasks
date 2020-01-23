def solution(N):
    binaries = []
    while N > 0:
        remainder = N%2
        N = N//2
        binaries.append(remainder)

    binaries = binaries[::-1]
    ones_index = [index for index, item in enumerate(binaries) if item == 1]
    zero_gaps = [ones_index[i] - ones_index[i - 1] - 1 for i in range(len(ones_index)) if i > 0]
    if len(zero_gaps) == 0:
        return 0
    return max(zero_gaps)

print(solution(1041))