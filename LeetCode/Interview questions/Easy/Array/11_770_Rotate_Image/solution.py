from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i, l in enumerate(zip(*matrix)):
            matrix[i] = list(l[::-1])


sol = Solution()
mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
mat2 = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
sol.rotate(mat)
sol.rotate(mat2)

print(mat)
print(mat2)
