"""
Given an integer array nums, rotate the array to the left by one.



Note: There is no need to return anything, just modify the given array.
"""


def left_shift(arr: list[int], rotation: int):
    for i in range(rotation):
        temp = arr[0]
        for j in range(0, len(arr) - 1):
            arr[j] = arr[j + 1]
        arr[-1] = temp


def right_shift(arr: list[int], rotation: int):
    for i in range(rotation):
        temp = arr[-1]
        for j in range(len(arr) - 1, 0, -1):
            arr[j] = arr[j - 1]
        arr[0] = temp


left_shift([0, 1, 2, 3, 4, 5], 1)
right_shift([0, 1, 2, 3, 4, 5], 1)
