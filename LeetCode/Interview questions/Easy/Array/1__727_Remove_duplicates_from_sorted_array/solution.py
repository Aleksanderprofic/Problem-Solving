from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        index = 0
        actual_value = None

        for n in nums:
            if actual_value != n:
                nums[index] = n
                actual_value = n
                index += 1

        return index
