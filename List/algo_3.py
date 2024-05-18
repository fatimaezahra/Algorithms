'''
Algorithm used => Kadane's Algorithm

kadane's algorithm is used for finding the maximum sum of contiguous subsequence in a sequence.
It is considered a greedy/dp algorithm but I think they more greedy than dp
here are some of the examples to understand the use case more clearly
Example1 => [-2, 3, 8, -1, 4]
result =>  {3, 8, -1, 4} => 14
Example2 => [-1, 1, 0]
result => {1} => 1
Example3 => [-1, -3, -4]
result => -1
Example1 => [-2, 3, 8, -12, 8, 4]
result =>  {8, 4} => 12
'''

# def solution(L):
#     count = {}
#     for idx, item in enumerate(L):
#         count[sum(L[idx:])] = L[idx:]
#     count[L[0]] = L[:1]   
#     key = max(count.keys())
#     if count[key][-1] == 0:
#         del count[key][-1]
#     return(key, count[key])


# print(solution([-2, 3, 8, -1, 4]))
# print(solution([-1, 1, 0]))
# print(solution([-1, -3, -4]))
# print(solution([-2, 3, 8, -12, 8, 4]))


def solution_1(L):
    if not L:
        return
    max_item = L[0]
    for idx, item in enumerate(L):
        max_item = max(item, max_item, sum(L[idx:]))

    return max_item


print(solution_1([-2, 3, 8, -1, 4]))
print(solution_1([-1, 1, 0]))
print(solution_1([-1, -3, -4]))
print(solution_1([-2, 3, 8, -12, 8, 4]))
