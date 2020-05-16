from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        s.add(nums[0])

        for num in nums[1:]:
            if num not in s:
                s.add(num)
            else:
                s.remove(num)
        return sum(s)


if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([2, 2, 1]))
    print(sol.singleNumber([4, 1, 2, 1, 2]))
