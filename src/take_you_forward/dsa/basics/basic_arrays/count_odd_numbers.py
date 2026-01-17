"""
Given an array of n elements. The task is to return the count of the number of odd numbers in the array.
"""


class Solution(object):
    def count_odd_numbers(self, nums: list[int]) -> int:
        counter = 0
        for num in nums:
            if num % 2 != 0:
                counter += 1
        return counter

    def count_odd_numbers1(self, nums: list[int]) -> int:
        return sum(1 for num in nums if num % 2 != 0)


if __name__ == "__main__":
    for i, j in ([1, 2, 3, 4, 5], 3), ([1, 2, 1, 1, 5, 1], 5):
        assert Solution().count_odd_numbers(i) == j
        assert Solution().count_odd_numbers1(i) == j
