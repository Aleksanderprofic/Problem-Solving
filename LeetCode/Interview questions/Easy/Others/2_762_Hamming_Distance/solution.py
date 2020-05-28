class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0
        x = x ^ y
        while x != 0:
            distance += x & 1
            x >>= 1
        return distance

    def hammingDistance2(self, x: int, y: int) -> int:
        distance = 0
        while x > 0 or y > 0:
            if x & 1 != y & 1:
                distance += 1
            x >>= 1
            y >>= 1
        return distance


sol = Solution()
print(sol.hammingDistance(1, 4))
print(sol.hammingDistance(5, 10))
print(sol.hammingDistance(2, 7))
print(sol.hammingDistance(1, 5))
