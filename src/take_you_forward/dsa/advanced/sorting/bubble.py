"""
Given an array of integers called nums,sort the array in non-decreasing order using the bubble sort algorithm and return the sorted array.

A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.
"""


class Solution:
    def bubble_sort(self, nums):
        for i in range(len(nums) - 1, -1, -1):
            swapped = False
            for j in range(i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            if not swapped:
                return nums


if __name__ == "__main__":
    for i, j in ([7, 4, 1, 5, 3], [1, 3, 4, 5, 7]), ([5, 4, 4, 1, 1], [1, 1, 4, 4, 5]):
        assert Solution().bubble_sort(i) == j
