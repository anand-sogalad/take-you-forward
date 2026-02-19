"""
Sum of Array Elements
Easy

Company
Given an array arr of size n, the task is to find the sum of all the elements in the array.
"""


class Solution(object):
    @staticmethod
    def sum_of_array(arr: list[int]) -> int:
        sum = 0
        for num in arr:
            sum += num
        return sum


if __name__ == "__main__":
    result = Solution.sum_of_array([5, 4, 3, 2, 6, 7, 8])
    print(result)
