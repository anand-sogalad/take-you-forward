"""
Given an array nums, find the sum of elements of array using recursion.
"""


class Solution(object):
    def sum_array(self, nums):
        return self.sum(nums, 0)

    def sum(self, nums, index):
        if index >= len(nums):
            return 0
        return nums[index] + self.sum(nums, index + 1)
