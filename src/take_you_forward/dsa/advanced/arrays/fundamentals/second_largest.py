"""
Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.
"""


class Solution:
    def secondLargestElement(self, nums):
        if len(nums) < 2:
            return -1

        largest = nums[0]
        second_largest = None
        for i in range(1, len(nums)):
            if nums[i] > largest:
                second_largest = largest
                largest = nums[i]
            elif nums[i] != largest and (second_largest is None or nums[i] > second_largest):
                second_largest = nums[i]
        return second_largest if second_largest is not None else -1
