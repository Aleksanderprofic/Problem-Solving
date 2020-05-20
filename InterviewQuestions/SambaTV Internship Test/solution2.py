# def solution(A):
#     a_length = len(A)
#     if a_length < 3:
#         return 0
#     stable_periods = 0
#
#     for i in range(a_length - 2):
#         j = i + 2
#         diff = A[i + 1] - A[i]
#         while j < a_length and A[j] - A[j - 1] == diff:
#             stable_periods += 1
#             if stable_periods > 1_000_000_000:
#                 return -1
#             j += 1
#     return stable_periods
"""
First solution (commented code) is just iterating over the list and checking every scenario.

Second solution (uncommented code) is the better and faster version where I skip some of the
computations which are obvious for example:
    1) Periods of size 3, e.g [1, 2, 3] have 1 stable period
    2) Periods of size 4, e.g [1, 2, 3, 4] have 3 stable periods -> [1, 2, 3], [2, 3, 4]
    and [1, 2, 3, 4], but first one was included in 1st scenario that's why we add 3-1 = 2
    3) Periods of size 5, e.g [1, 2, 3, 4, 5] have 6 stable periods but first one and the
    second one were included in 1st and 2nd scenarios that's why we add 6 - 2 - 1 = 3
    and so on"""

def solution(A):
    a_length = len(A)
    stable_periods = 0
    i = 0
    while i < a_length - 2:
        j = i + 2
        diff = A[i + 1] - A[i]
        number_of_periods_to_add = 1
        while j < a_length and A[j] - A[j - 1] == diff:
            stable_periods += number_of_periods_to_add
            if stable_periods > 1_000_000_000:
                return -1
            j += 1
            number_of_periods_to_add += 1
        i = j - 1
    return stable_periods
