"""
Given a string, the task is to reverse it. The string is represented by an array of characters s.
"""


class Solution(object):
    def reverse_string(self, s: list[str]) -> list[str]:
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s


if __name__ == "__main__":
    for i, j in (
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["b", "y", "e"], ["e", "y", "b"]),
    ):
        assert Solution().reverse_string(i) == j
