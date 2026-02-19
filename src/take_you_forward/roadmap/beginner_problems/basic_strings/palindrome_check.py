"""
Palindrome Check
Easy

Company
You are given a string s. Return true if the string is palindrome, otherwise false.



A string is called palindrome if it reads the same forward and backward.


Example 1

Input : s = "hannah"

Output : true

Explanation :

The given string when read backward is -> "hannah", which is same as when read forward.

Hence answer is true.

Example 2

Input : s = "aabbaaa"

Output : false

Explanation :

The given string when read backward is -> "aaabbaa", which is not same as when read forward.

Hence answer is false.
"""


class Solution(object):
    @staticmethod
    def is_palindrome(s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    result = Solution.is_palindrome("aabbaaa")
    print(result)
