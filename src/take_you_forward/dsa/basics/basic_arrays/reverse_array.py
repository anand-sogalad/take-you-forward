"""
Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.
"""


class Solution(object):
    def reverse(self, arr: list[int]) -> list[int]:
        left, right = 0, len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr


if __name__ == "__name__":
    for i, j in (
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2, 1, 1, 5, 1], [1, 5, 1, 1, 2, 1]),
    ):
        assert Solution().reverse(i) == j
