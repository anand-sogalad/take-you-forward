"""
Given an array of integers nums, return the value of the largest element in the array
"""


def largest(arr: list[int]):
    max = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]

    return max
