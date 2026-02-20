"""
Valid Anagram
Easy

Company
Given two strings s and t, return true if t is an anagram of s, and false otherwise.



An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1

Input : s = "anagram" , t = "nagaram"

Output : true

Explanation :

We can rearrange the characters of string s to get string t as frequency of all characters from both strings is same.

Example 2

Input : s = "dog" , t = "cat"

Output : false

Explanation :

We cannot rearrange the characters of string s to get string t as frequency of all characters from both strings is not same.
"""


class Solution(object):
    @staticmethod
    def is_anagram(s: str, t: str):
        if s == t:
            return True

        if len(s) != len(t):
            return False

        s_map, t_map = {}, {}

        for c in s:
            s_map[c] = s_map.get(c, 0) + 1

        for c in t:
            t_map[c] = t_map.get(c, 0) + 1

        for c in s_map:
            if s_map[c] != t_map.get(c, 0):
                return False

        return True
