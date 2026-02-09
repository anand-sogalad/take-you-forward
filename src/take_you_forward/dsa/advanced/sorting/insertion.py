"""
Given an array of integers called nums, sort the array in non-decreasing order using the insertion sort algorithm and return the sorted array.

A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.
"""


class Solution:
    def insertion_sort(self, nums):
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
        return nums


if __name__ == "__main__":
    assert Solution().insertion_sort([7, 4, 1, 5, 3]) == [1, 3, 4, 5, 7]
