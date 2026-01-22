"""
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
"""


class Solution(object):
    def rotate_string(self, s: str, goal: str) -> bool:
        if s == goal:
            return True

        if len(s) != len(goal):
            return False

        l1, l2 = list(s), list(goal)

        for i in range(len(l1)):
            l1.insert(0, l1.pop())
            if l1 == l2:
                return True
        return False

    def rotate_string1(self, s: str, goal: str) -> bool:
        if s == goal:
            return True

        if len(s) != len(goal):
            return False

        for i in range(len(s)):
            rotated = s[i:] + s[:i]
            if rotated == goal:
                return True
        return False


if __name__ == "__main__":
    for s, goal, result in [
        ("abcde", "cdeab", True),
        ("abcde", "adeac", False),
        ("abcde", "abcde", True),
    ]:
        assert Solution().rotate_string(s, goal) == result
        assert Solution().rotate_string1(s, goal) == result
