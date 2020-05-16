from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length <= k:
            k %= length
        if k == 0:
            return

        j = k
        remembered_value = nums[j]

        if length % 2 == 0:
            moved_numbers = 0
            while moved_numbers != length:
                i = j
                next_index = (i + k) % length

                while next_index != j:
                    temp = nums[next_index]
                    nums[next_index] = remembered_value
                    remembered_value = temp
                    moved_numbers += 1
                    i = next_index
                    next_index = (i + k) % length

                nums[next_index] = remembered_value
                j = (j + 1) % length
                remembered_value = nums[j]
                moved_numbers += 1
        else:
            i = j
            next_index = (i + k) % length

            while next_index != j:
                temp = nums[next_index]
                nums[next_index] = remembered_value
                remembered_value = temp
                i = next_index
                next_index = (i + k) % length

            nums[next_index] = remembered_value


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    sol.rotate(nums, 3)

    print(nums == [5, 6, 7, 1, 2, 3, 4])
