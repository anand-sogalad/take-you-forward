"""
Check if String is Palindrome or Not
Easy

Company
Given a string s, return true if the string is palindrome, otherwise false.



A string is called palindrome if it reads the same forward and backward.


Example 1

Input : s = "hannah"

Output : true

Explanation : The string when reversed is --> "hannah", which is same as original string , so we return true.

Example 2

Input : s = "aabbaA"

Output : false

Explanation : The string when reversed is --> "Aabbaa", which is not same as original string, So we return false.
"""


class Solution(object):
    @staticmethod
    def is_plaindrome(s: str):
        return Solution._palindrome(s, 0, len(s) - 1)

    @staticmethod
    def _palindrome(s: str, left, right):
        if not left < right:
            return True

        if s[left] != s[right]:
            return False

        return Solution._palindrome(s, left + 1, right - 1)


if __name__ == "__main__":
    result = Solution.is_plaindrome("aabbaA")
    print(result)
