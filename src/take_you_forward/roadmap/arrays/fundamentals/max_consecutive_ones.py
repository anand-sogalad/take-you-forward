"""
Given a binary array nums, return the maximum number of consecutive 1s in the array.



A binary array is an array that contains only 0s and 1s.


Example 1

Input: nums = [1, 1, 0, 0, 1, 1, 1, 0]

Output: 3

Explanation:

The maximum consecutive 1s are present from index 4 to index 6, amounting to 3 1s

Example 2

Input: nums = [0, 0, 0, 0, 0, 0, 0, 0]

Output: 0

Explanation:

No 1s are present in nums, thus we return 0
"""

from typing import Literal


def max_consecutive_ones(arr: list[Literal[0, 1]]) -> int:
    _max = _current_max = 0

    for i in arr:
        if i == 1:
            _current_max += 1
        else:
            _max = max(_max, _current_max)
            _current_max = 0

    return max(_max, _current_max)
