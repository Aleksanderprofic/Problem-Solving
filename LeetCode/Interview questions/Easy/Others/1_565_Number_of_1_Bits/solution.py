class Solution:
    def hammingWeight(self, n: int) -> int:
        bit_count = 0
        while n:
            bit_count += n & 1
            n >>= 1
        return bit_count

    def hammingWeight2(self, n: int) -> int:
        bit_count = 0
        while n > 0:
            bit_count += n % 2
            n //= 2
        return bit_count


sol = Solution()
print(sol.hammingWeight(1011))
print(sol.hammingWeight(10000000))
print(sol.hammingWeight(11111111111111111111111111111101))
