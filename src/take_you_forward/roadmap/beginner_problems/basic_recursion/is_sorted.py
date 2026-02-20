"""
Check if the Array is Sorted II
Easy

Company
Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.


Example 1

Input : nums = [1, 2, 3, 4, 5]

Output : true

Explanation : For all i (1 <= i <= 4) it holds nums[i] <= nums[i+1], hence it is sorted and we return true.

Example 2

Input : nums = [1, 2, 1, 4, 5]

Output : false

Explanation : For i == 2 it does not hold nums[i] <= nums[i+1], hence it is not sorted and we return false.

Now your turn!

Input : nums = [1,9,6,8,5,4,0]
"""


class Solution(object):
    @staticmethod
    def is_sorted(arr: list[int]):
        return Solution._sorted(arr, 1)

    @staticmethod
    def _sorted(arr: list[int], index):
        if index >= len(arr):
            return True

        if not arr[index - 1] <= arr[index]:
            return False

        return Solution._sorted(arr, index + 1)


if __name__ == "__main__":
    result = Solution.is_sorted([1, 9, 6, 8, 5, 4, 0])
    print(result)
