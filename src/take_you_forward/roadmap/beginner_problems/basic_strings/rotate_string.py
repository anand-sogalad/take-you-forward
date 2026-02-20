"""
Rotate String
Easy

Company
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
"""


class Solution(object):
    @staticmethod
    def rotate_str(s, goal):
        for i in range(len(s)):
            if s[i:] + s[:i] == goal:
                return True
        return False


if __name__ == "__main__":
    result = Solution.rotate_str("abcde", "cdeab")
    print(result)
