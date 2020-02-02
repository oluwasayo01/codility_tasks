"""
    Write a function:

def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

Result array should be returned as an array of integers.

For example, given the string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
the function should return the values [2, 4, 1], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
M is an integer within the range [1..50,000];
each element of arrays P, Q is an integer within the range [0..N − 1];
P[K] ≤ Q[K], where 0 ≤ K < M;
string S consists only of upper-case English letters A, C, G, T. """


def solution(S, P, Q):
    number_pairs = list(zip(P, Q))
    result = []
    for i, j in number_pairs:
        gap = S[i:j+1]
        if 'A' in gap:
            result.append(1)
            continue

        if 'C' in gap:
            result.append(2)
            continue

        if 'G' in gap:
            result.append(3)
            continue

        if 'T' in gap:
            result.append(4)
            continue
    return result

# Example
print(solution("CAGCCTA", [2, 5, 0], [4, 5, 6]))