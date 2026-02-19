"""
Longest Common Prefix
Easy

Company
Write a function to find the longest common prefix string amongst an array of strings.



If there is no common prefix, return an empty string "".


Example 1

Input : str = ["flowers" , "flow" , "fly", "flight" ]

Output : "fl"

Explanation :

All strings given in array contains common prefix "fl".

Example 2

Input : str = ["dog" , "cat" , "animal", "monkey" ]

Output : ""

Explanation :

There is no common prefix among the given strings in array.
"""


class Solution(object):
    @staticmethod
    def longest_common_prefix(arr: list[str]) -> str:
        sw = len(min(arr, key=len))

        for i in range(sw):
            for j in range(1, len(arr)):
                if arr[0][i] != arr[j][i]:
                    return arr[0][:i]


if __name__ == "__main__":
    result = Solution.longest_common_prefix(["flowers", "flow", "fly", "flight"])
    print(result)
