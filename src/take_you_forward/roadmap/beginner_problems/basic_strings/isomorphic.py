"""
Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters in s can be replaced to get t.



All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


Example 1

Input : s = "egg" , t = "add"

Output : true

Explanation :

The 'e' in string s can be replaced with 'a' of string t.

The 'g' in string s can be replaced with 'd' of t.

Hence all characters in s can be replaced to get t.

Example 2

Input : s = "apple" , t = "bbnbm"

Output : false

Explanation :

Strings are matched index by index.

At index 0, 'a' maps to 'b'.

At index 1, 'p' also maps to 'b'.

This is invalid because two different characters (a and p) cannot map to the same character (b) in a one-to-one mapping.

Therefore, no valid mapping exists and the output is false.

Example 3

Input : s = "paper" , t = "title"

Output:

true
"""


class Solution(object):
    @staticmethod
    def is_isomorphic(s: str, t: str):
        s_to_t_mapping = {}
        t_to_s_mapping = {}

        for cs, ct in zip(s, t):
            if cs in s_to_t_mapping:
                if s_to_t_mapping[cs] != ct:
                    return False
            else:
                s_to_t_mapping[cs] = ct

            if ct in t_to_s_mapping:
                if t_to_s_mapping[ct] != cs:
                    return False
            else:
                t_to_s_mapping[ct] = cs
        return True


if __name__ == "__main__":
    result = Solution.is_isomorphic("egg", "add")
    print(result)
