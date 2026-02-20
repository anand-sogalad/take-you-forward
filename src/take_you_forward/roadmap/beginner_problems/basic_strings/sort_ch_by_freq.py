"""
Sort Characters by Frequency
Easy

Company
You are given a string s. Return the array of unique characters, sorted by highest to lowest occurring characters.



If two or more characters have same frequency then arrange them in alphabetic order.


Example 1

Input : s = "tree"

Output : ['e', 'r', 't' ]

Explanation :

The occurrences of each character are as shown below :

e --> 2

r --> 1

t --> 1.

The r and t have same occurrences , so we arrange them by alphabetic order.

Example 2

Input : s = "raaaajj"

Output : ['a' , 'j', 'r' ]

Explanation :

The occurrences of each character are as shown below :

a --> 4

j --> 2

r --> 1
"""


class Solution(object):
    @staticmethod
    def sort_by_frequency(s: str):
        s_map = {}

        for c in s:
            s_map[c] = s_map.get(c, 0) + 1

        return sorted(s_map.keys(), key=lambda x: (-s_map[x], x))


if __name__ == "__main__":
    result = Solution.sort_by_frequency("anandsogalad")
    print(result)
