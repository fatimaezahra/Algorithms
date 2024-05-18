"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.
"""


def solution(L, new_l=[]):
    for i in L:
        if not isinstance(i, list):
            new_l.append(i)
        else:
            solution(i, new_l)
    return new_l


print(solution([12, [3, 4, [5, 7]], 8, [9]]))
