class Solution:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    def my_atoi(self, s: str) -> int:
        s = s.lstrip()
        s_len = len(s)
        if s_len == 0:
            return 0
        number = 0
        sign = None
        i = 0
        if s[i] == '-' or s[i] == '+':
            if s_len == 1:
                return 0
            sign = s[i]
            i += 1

        for char in s[i:]:
            if not char.isdigit():
                break
            number = number * 10 + int(char)

        number = number if sign is None or sign == '+' else -number
        if number > self.INT_MAX:
            return self.INT_MAX
        elif number < self.INT_MIN:
            return self.INT_MIN
        return number


sol = Solution()
print(sol.my_atoi("42"))
print(sol.my_atoi("     -42"))
print(sol.my_atoi("4193 with words"))
print(sol.my_atoi("words and 987"))
print(sol.my_atoi("-91283472332"))

