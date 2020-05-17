from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        occurrences_from_first_list = dict()
        list_to_return = []
        for num in nums1:
            if num in occurrences_from_first_list:
                occurrences_from_first_list[num] += 1
            else:
                occurrences_from_first_list[num] = 1

        for num in nums2:
            if num in occurrences_from_first_list and occurrences_from_first_list[num] > 0:
                list_to_return.append(num)
                occurrences_from_first_list[num] -= 1

        return list_to_return

    def intersect_using_counter(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1)
        list_to_return = []

        for num in nums2:
            if count[num]:
                list_to_return.append(num)
                count[num] -= 1

        return list_to_return


sol = Solution()
print(sol.intersect_using_counter(nums1=[1, 2, 2, 1], nums2=[2, 2]))
print(sol.intersect_using_counter(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))

cnt = Counter([1, 2, 5, 2, 2, 1, 5, 7])
print()
