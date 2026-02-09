"""
Given an array of integers nums and an integer target, find the smallest index (0 based indexing) where the target appears in the array. If the target is not found in the array, return -1
"""


class Solution:
    def linear_search(self, nums, target):
        for i, n in enumerate(nums):
            if n == target:
                return i
        return -1
