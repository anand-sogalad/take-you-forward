"""
Reverse an array
Easy

Company
Given an array nums of n integers, return reverse of the array.


Example 1

Input : nums = [1, 2, 3, 4, 5]

Output : [5, 4, 3, 2, 1]

Example 2

Input : nums = [1, 3, 3, 3, 5]

Output : [5, 3, 3, 3, 1]

Now your turn!

Input : nums = [1, 2, 1]
"""


class Solution(object):
    @staticmethod
    def reverse_array(arr: list[int]):
        Solution._reverse(arr, 0, len(arr) - 1)
        return arr

    @staticmethod
    def _reverse(arr: list[int], left: int, right: int):
        if not left < right:
            return

        arr[left], arr[right] = arr[right], arr[left]

        Solution._reverse(arr, left + 1, right - 1)


if __name__ == "__main__":
    result = Solution.reverse_array([1, 2, 3, 4, 5])
    print(result)
