from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        first_price = prices[0]

        for second_price in prices[1:]:
            diff = second_price - first_price
            if diff > 0:
                profit += diff
            first_price = second_price

        return profit


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7, 6, 4, 3, 1]))
    print(sol.maxProfit([1, 2, 3, 4, 5]))
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
