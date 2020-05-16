from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


if __name__ == "__main__":
    sol = Solution()
    string = ['h', 'a', 'n', 's']
    sol.reverseString(string)
    print(string)
