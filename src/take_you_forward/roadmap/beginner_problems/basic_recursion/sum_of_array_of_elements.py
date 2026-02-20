"""
Sum of Array Elements
Easy

Company
Given an array nums, find the sum of elements of array using recursion.


Example 1

Input : nums = [1, 2, 3]

Output : 6

Explanation : The sum of elements of array is 1 + 2 + 3 => 6.

Example 2

Input : nums = [5, 8, 1]

Output : 14

Explanation : The sum of elements of array is 5 + 8 + 1 => 14.
"""


class Solution(object):
    @staticmethod
    def array_sum(arr: list[int]) -> int:
        index = 0

        return Solution.sum(arr, index)

    @staticmethod
    def sum(arr: list[int], index):
        if index == len(arr) - 1:
            return arr[index]

        return arr[index] + Solution.sum(arr, index + 1)


if __name__ == "__main__":
    result = Solution.array_sum([5, 8, 1])
    print(result)
