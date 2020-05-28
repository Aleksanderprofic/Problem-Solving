class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        return self.describe_number(self.countAndSay(n - 1))

    def describe_number(self, n_str: str):
        count = 1
        actual_digit = n_str[0]
        result = ''
        for digit in n_str[1:]:
            if digit is not actual_digit:
                result += str(count) + actual_digit
                actual_digit = digit
                count = 1
            else:
                count += 1
        result += str(count) + actual_digit

        return result


sol = Solution()
print(sol.countAndSay(2))
print(sol.countAndSay(3))
print(sol.countAndSay(4))
print(sol.countAndSay(5))
print(sol.countAndSay(6))
print(sol.countAndSay(7))
