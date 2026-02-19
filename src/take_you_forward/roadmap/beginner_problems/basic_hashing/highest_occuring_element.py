"""
Highest Occurring Element in an Array
Easy

Company
Given an array nums of n integers, find the most frequent element in it i.e., the element that occurs the maximum number of times. If there are multiple elements that appear a maximum number of times, find the smallest of them.



Please note that this section might seem a bit difficult without prior knowledge on what hashing is, we will soon try to add basics concepts for your ease! If you know the concepts already please go ahead to give a shot to the problem. Cheers!
"""

from typing import Any


class Solution(object):
    @staticmethod
    def highest_occuring_element(arr: list[Any]) -> Any:
        element_map = {}

        # create a map for each element
        for el in arr:
            element_map[el] = element_map.get(el, 0) + 1

        _key, _val = None, 0

        # get the max values key
        for key, val in element_map.items():
            if val > _val or (val == _val and (_key is None or key < _key)):
                _key, _val = key, val

        return _key


if __name__ == "__main__":
    result = Solution.highest_occuring_element([4, 4, 5, 5, 6])
    print(result)
