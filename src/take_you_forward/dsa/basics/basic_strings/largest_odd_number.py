"""
Given a string s, representing a large integer, the task is to return the largest-valued odd integer (as a string) that is a substring of the given string s.

The number returned should not have leading zero's. But the given input string may have leading zero. (If no odd number is found, then return empty string.)
"""


class Solution(object):
    def largest_odd_number(self, s: str):
        s = s.strip("0")
        for i in range(len(s) - 1, -1, -1):
            if int(s[i]) % 2 != 0:
                return s[: i + 1]
        return ""
