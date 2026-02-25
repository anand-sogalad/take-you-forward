"""
Move Zeros to End
Easy

Hints
Company
Given an integer array nums, move all the 0's to the end of the array. The relative order of the other elements must remain the same.



This must be done in place, without making a copy of the array.
"""


# def move_zeros_to_end(arr: list[int]):
#     for i in range(len(arr)):
#         swapped = False
#         for j in range(len(arr) - 1 - i):
#             if arr[j] == 0:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#         if not swapped:
#             return arr


def move_zeros_to_end(arr: list[int]):
    """Move all zeros to the end while maintaining relative order of non-zero elements.

    Time: O(n), Space: O(1) - in-place
    """
    left = 0

    # Find first zero
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1


if __name__ == "__main__":
    result = move_zeros_to_end([1, 0, 4, 0, 5, 2])
    print(result)
