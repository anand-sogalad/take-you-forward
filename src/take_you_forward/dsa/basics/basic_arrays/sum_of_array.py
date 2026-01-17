"""
Given an array arr of size n, the task is to find the sum of all the elements in the array.
"""


class Solution(object):
    def sum_array_dsa(self, nums: list[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
        return sum

    def sum_array_dsa1(self, nums: list[int]) -> int:
        sum = 0
        for num in nums:
            sum += num
        return sum

    def sum_array_pythonic(self, nums: list[int]) -> int:
        return sum(nums)

    # two pointer, but slower and complex
    def sum_array_efficient(self, nums: list[int]) -> int:
        if len(nums) > 1:
            left, right = 0, len(nums) - 1
            sum = 0
            while left < right:
                sum += nums[left] + nums[right]
                left += 1
                right -= 1
            return sum + nums[left] if left == right else sum
        return nums[0]


if __name__ == "__main__":
    for i, j in ([1, 2, 3, 4, 5], 15), ([1, 2, 1, 1, 5, 1], 11):
        assert Solution().sum_array_dsa(i) == j
        assert Solution().sum_array_dsa1(i) == j
        assert Solution().sum_array_pythonic(i) == j
        assert Solution().sum_array_efficient(i) == j
