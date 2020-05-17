class Solution:
    def firstUniqChar(self, s: str) -> int:
        occurences = set()

        for i, char in enumerate(s, 1):
            if char not in occurences:
                if char not in s[i:]:
                    return i - 1
                occurences.add(char)
        return -1


sol = Solution()
print(sol.firstUniqChar('leetcode'))
print(sol.firstUniqChar('loveleetcode'))
print(sol.firstUniqChar('l'))
print(sol.firstUniqChar('aaaaaaad'))

