"""
Given an input string as an array of characters, write a function that reverses the string.
"""


class Solution(object):
    def reverse(self, s: list[str]) -> list[str]:
        # if s is empty return rempy s
        if not s:
            return s

        left, right = 0, len(s) - 1
        self._reverse(s, left, right)
        return s

    def _reverse(self, s, left, right):
        if left >= right:
            return

        s[right], s[left] = s[left], s[right]
        self._reverse(s, left + 1, right - 1)


if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    t = Solution().reverse(s)
    assert "".join(s) == "".join(t)
