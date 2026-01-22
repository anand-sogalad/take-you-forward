"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""


class Solution(object):
    def is_anagram(self, s: str, t: str) -> bool:
        if s == t:
            return True

        if len(s) != len(t):
            return False

        map1, map2 = {}, {}

        for i in s:
            map1[i] = map1.get(i, 0) + 1

        for i in t:
            map2[i] = map2.get(i, 0) + 1

        for key in map1:
            if map1[key] != map2.get(key, 0):
                return False

        return True
