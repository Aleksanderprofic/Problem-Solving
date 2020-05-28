from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ''
        if len(strs) == 0:
            return ''
        first_word = strs[0]
        for prefix in (first_word[0:i] for i in range(1, len(first_word) + 1)):
            for word in strs[1:]:
                if not word.startswith(prefix):
                    return longest_prefix
            longest_prefix = prefix

        return longest_prefix


sol = Solution()
print(sol.longestCommonPrefix(['flower', 'flow', 'flight']))
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))
print(sol.longestCommonPrefix(["", "racecar", "car"]))
print(sol.longestCommonPrefix(["yoy", "yoykk", "yowkjqw"]))
