"""
You are given a string s. Return the array of unique characters, sorted by highest to lowest occurring characters.

If two or more characters have same frequency then arrange them in alphabetic order.
"""


class Solution(object):
    def sort_string(self, s: str):
        freq: dict[str, int] = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1

        return sorted(freq.keys(), key=lambda x: (-freq[x], x))
