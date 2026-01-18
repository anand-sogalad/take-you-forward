"""
Given an array nums of n integers, find the most frequent element in it i.e., the element that occurs the maximum number of times. If there are multiple elements that appear a maximum number of times, find the smallest of them.

Please note that this section might seem a bit difficult without prior knowledge on what hashing is, we will soon try to add basics concepts for your ease! If you know the concepts already please go ahead to give a shot to the problem. Cheers!
"""


class Solution(object):
    def height_occuring_number(self, arr: list[int]) -> int:
        freq: dict[int, int] = {}
        for n in arr:
            freq[n] = freq.get(n, 0) + 1

        key, val = 0, 0

        for k, v in freq.items():
            if v >= val:
                if v == val:
                    key = k if k <= key else key
                elif v > val:
                    key, val = k, v

        return key


if __name__ == "__main__":
    for i, j in ([1, 2, 2, 3, 3, 3], 3), ([4, 4, 5, 5, 6], 4):
        assert Solution().height_occuring_number(i) == j
