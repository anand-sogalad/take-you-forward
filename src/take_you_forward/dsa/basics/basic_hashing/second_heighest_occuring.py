"""
Given an array of n integers, find the second most frequent element in it.

If there are multiple elements that appear second most frequent times, find the smallest of them.

If second most frequent element does not exist return -1.
"""


class Solution(object):
    def second_heighest(self, nums: list[int]) -> int:
        freq: dict[int, int] = {}

        # Build frequency map
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        # Track top 2 frequencies
        max_elem, second_elem = 0, 0
        max_freq, second_freq = 0, 0

        for elem, count in freq.items():
            if count > max_freq:
                second_elem, second_freq = max_elem, max_freq
                max_elem, max_freq = elem, count
            elif count == max_freq:
                max_elem = min(max_elem, elem)
            elif count > second_freq and count < max_freq:
                second_elem, second_freq = elem, count
            elif count == second_freq:
                second_elem = min(second_elem, elem)

        return second_elem if second_freq != 0 else -1


if __name__ == "__main__":
    for i, j in ([1, 2, 2, 3, 3, 3], 2), ([4, 4, 5, 5, 6, 6, 7, 7], -1):
        assert Solution().second_heighest(i) == j
