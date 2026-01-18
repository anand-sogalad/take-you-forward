"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


class Solution(object):
    def longest_common_prefix(self, s: list[str]) -> str:
        # get the smallest str
        min_len = len(min(s, key=len))

        for i in range(min_len):
            lcp = s[0][i]

            for j in range(1, len(s)):
                if lcp != s[j][i]:
                    return s[0][:i]

        return s[0][:min_len]


if __name__ == "__main__":
    for input, output in (
        (["flowers", "flow", "fly", "flight"], "fl"),
        (["dog", "cat", "animal", "monkey"], ""),
    ):
        assert Solution().longest_common_prefix(input) == output
