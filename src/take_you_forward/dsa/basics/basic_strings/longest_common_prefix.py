"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


class Solution(object):
    def longest_common_prefix(self, s: list[str]) -> str:
        # get the smallest str
        left, right = 0, len(s) - 1
        smallest = ""

        while left <= right:
            smallest = s[left] if len(s[left]) < len(s[right]) else s[right]
            left += 1
            right -= 1

        # check if each string starts with smallest
        while smallest:
            for i in s:
                if not i.startswith(smallest):
                    smallest = smallest[:-1]
                    break
            else:
                return smallest
        return smallest


if __name__ == "__main__":
    for input, output in (
        (["flowers", "flow", "fly", "flight"], "fl"),
        (["dog", "cat", "animal", "monkey"], ""),
    ):
        assert Solution().longest_common_prefix(input) == output
