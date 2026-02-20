"""
Reverse a String I
Easy

Company
Given an input string as an array of characters, write a function that reverses the string.


Example 1

Input : s = ["h", "e", "l", "l", "o"]

Output : ["o", "l", "l", "e", "h"]

Explanation : The given string is s = "hello" and after reversing it becomes s = "olleh".

Example 2

Input : s = ["b", "y", "e" ]

Output : ["e", "y", "b"]

Explanation : The given string is s = "bye" and after reversing it becomes s = "eyb".
"""


class Solution(object):
    @staticmethod
    def reverse_string(arr: list[str]):
        Solution._reverse(arr, 0, len(arr) - 1)
        return arr

    @staticmethod
    def _reverse(arr: list[str], left, right):
        if not left < right:
            return

        arr[left], arr[right] = arr[right], arr[left]

        Solution._reverse(arr, left + 1, right - 1)


if __name__ == "__main__":
    result = Solution.reverse_string(["h", "e", "l", "l", "o"])
    print(result)
