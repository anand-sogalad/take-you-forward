"""
Check if the Array is Sorted I
Easy

Company
Given an array arr of size n, the task is to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order. If the array is sorted then return True, else return False.
"""


class Solution(object):
    @staticmethod
    def is_sorted(arr: list[int]):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True


if __name__ == "__main__":
    result = Solution.is_sorted([1, 2, 3, 4, 5, 3])
    print(result)
