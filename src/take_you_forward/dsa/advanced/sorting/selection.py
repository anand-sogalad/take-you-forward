"""
Given an array of integers nums, sort the array in non-decreasing order using the selection sort algorithm and return the sorted array.

A sorted array in non-decreasing order is an array where each element is greater than or equal to all previous elements in the array.
"""


class Solution:
    def selection_sort(self, nums):
        for i in range(len(nums) - 1):
            min_idx = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_idx]:
                    min_idx = j

            nums[i], nums[min_idx] = nums[min_idx], nums[i]


if __name__ == "__main__":
    for i, j in ([7, 4, 1, 5, 3], [1, 3, 4, 5, 7]), ([5, 4, 4, 1, 1], [1, 1, 4, 4, 5]):
        assert Solution().selection_sort(i) == j
