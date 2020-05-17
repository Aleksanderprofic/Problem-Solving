import re


class Solution:
    """
    Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

    Note: For the purpose of this problem, we define empty string as valid palindrome.

    Example 1:

    Input: "A man, a plan, a canal: Panama"
    Output: true
    Example 2:

    Input: "race a car"
    Output: false
    """
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = last_index = len(s) - 1

        while i < j:
            while i <= last_index and not s[i].isalnum():
                i += 1
            while j >= 0 and not s[j].isalnum():
                j -= 1

            if i < j:
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1
        return True

    def is_palindrome_with_regex(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]', '', s).lower()
        return s == s[::-1]


sol = Solution()
print(sol.is_palindrome_with_regex("A man, a plan, a canal: Panama"))
print(sol.is_palindrome_with_regex("race a car"))
print(sol.is_palindrome_with_regex("0P"))
