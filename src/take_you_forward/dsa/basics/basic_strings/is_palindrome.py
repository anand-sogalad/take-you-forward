"""
You are given a string s. Return true if the string is palindrome, otherwise false.

A string is called palindrome if it reads the same forward and backward.
"""


class Solution(object):
    def is_palindrome(self, s: str):
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    for i, j in ("hannah", True), ("aabbaaa", False):
        assert Solution().is_palindrome(i) == j
