from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        try:
            j = nums.index(0)
        except ValueError:
            return
        nums_len = len(nums)
        i = j + 1
        while i < nums_len and nums[i] == 0:
            i += 1

        while i < nums_len:
            nums[j] = nums[i]
            nums[i] = 0
            j += 1
            while i < nums_len and nums[i] == 0:
                i += 1

    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1

        while i < len(nums):
            nums[i] = 0
            i += 1
