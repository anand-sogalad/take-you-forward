"""
Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.
"""


class Solution(object):
    def is_sorted(self, nums):
        return self._is_greater(nums, 1)

    def _is_greater(self, nums, index):
        if index >= len(nums):
            return True

        if nums[index - 1] > nums[index]:
            return False

        return self._is_greater(nums, index + 1)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    result = Solution().is_sorted(nums)
    print(result)
