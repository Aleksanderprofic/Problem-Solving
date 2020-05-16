from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            seeking_number = target - num
            j = i + 1
            for num2 in nums[j:]:
                if num2 == seeking_number:
                    return [i, j]
                j += 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 18))
