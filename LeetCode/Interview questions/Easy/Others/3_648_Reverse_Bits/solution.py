class Solution:
    def reverseBits(self, n: int) -> int:
        mult = 2 ** 31
        reversed_bits = 0
        breakpoint()
        while n > 0:
            if n & 1:
                reversed_bits += mult
            n >>= 1
            mult >>= 1
        return reversed_bits

    def reverseBits2(self, n: int) -> int:
        reversed_bits = 0
        for _ in range(32):
            reversed_bits <<= 1
            reversed_bits |= n & 1
            n >>= 1
        return reversed_bits



sol = Solution()
sol.reverseBits(10010101)