"""
Given an array of n integers, find the sum of the frequencies of the highest occurring number and lowest occurring number.
"""


class Solution(object):
    def sum_of_highest_lowest(self, nums: list[int]) -> int:
        """
        Time: O(n) - build freq map + find min/max
        Space: O(k) - k = unique elements
        """
        # Build frequency map
        freq: dict[int, int] = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Manually find max and min frequencies
        max_freq = 0
        min_freq = len(nums) + 1  # Start with value larger than any possible frequency

        for count in freq.values():
            if count > max_freq:
                max_freq = count
            if count < min_freq:
                min_freq = count

        return max_freq + min_freq


if __name__ == "__main__":
    for i, j in ([1, 2, 2, 3, 3, 3], 4), ([4, 4, 5, 5, 6], 3):
        assert Solution().sum_of_highest_lowest(i) == j
