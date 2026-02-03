"""
Given a string s, return true if the string is palindrome, otherwise false.

A string is called palindrome if it reads the same forward and backward.
"""


class Solution(object):
    def is_palindrome(self, s: str):
        left, right = 0, len(s) - 1
        return self._validate_left_right(s, left, right)

    def _validate_left_right(self, s: str, left, right):
        if left > right:
            return True

        if s[left] == s[right]:
            return self._validate_left_right(s, left + 1, right - 1)
        else:
            return False


if __name__ == "__main__":
    s = "hannah"
    t = Solution().is_palindrome(s)
    print(t)
