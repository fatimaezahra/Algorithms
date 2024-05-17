"""
Given a list lst and a number N, create a new list
that contains each number of the list at most N times without reordering.

For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], 
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, 
which leads to [1,2,3,1,2,3]
"""
import collections

def solution(L, N):
    new_list = []
    count = collections.defaultdict(int)
    for item in L:
        if count[item] < N:
            new_list.append(item)
            count[item] += 1
    return new_list


print(solution([], 0))
print(solution([], 2))
print(solution([1,2,3,1,2,1,2,3], 2))
        