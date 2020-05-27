class Solution:

    def my_atoi(self, s: str) -> int:
        s = s.lstrip()
        s_len = len(s)
        if s_len == 0:
            return 0
        sign = None
        i = 0
        if s[i] == '-' or s[i] == '+':
            if s_len == 1:
                return 0
            sign = s[i]
            i += 1

        j = i
        while j < s_len and s[j].isdigit():
            j += 1

        str_number = s[i:j]
        number = (int(str_number) if str_number else 0)
        number = number if sign is None or sign == '+' else -number
        return max(-2**31, min(2**31 - 1, number))


sol = Solution()
print(sol.my_atoi("42"))
print(sol.my_atoi("     -42"))
print(sol.my_atoi("4193 with words"))
print(sol.my_atoi("words and 987"))
print(sol.my_atoi("-91283472332"))
print(sol.my_atoi("91283472332"))

