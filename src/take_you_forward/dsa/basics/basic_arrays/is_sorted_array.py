"""
Given an array arr of size n, the task is to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order. If the array is sorted then return True, else return False.
"""


class Solution(object):
    def is_sorted(self, arr: list[int]) -> bool:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True


if __name__ == "__main__":
    for i, j in ([1, 2, 3, 4, 5], True), ([5, 4, 6, 7, 8], False):
        assert Solution().is_sorted(i) == j
