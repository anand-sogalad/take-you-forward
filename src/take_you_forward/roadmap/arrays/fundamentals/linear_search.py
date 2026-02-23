"""
Given an array of integers nums and an integer target, find the smallest index (0 based indexing) where the target appears in the array. If the target is not found in the array, return -1
"""


def linear_search(arr: list[int], target: int):
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1
