"""
Bubble Sort
Easy

Hints
Company
Given an array of integers called nums,sort the array in non-decreasing order using the bubble sort algorithm and return the sorted array.



A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.


Example 1

Input: nums = [7, 4, 1, 5, 3]

Output: [1, 3, 4, 5, 7]

Explanation: 1 <= 3 <= 4 <= 5 <= 7.

Thus the array is sorted in non-decreasing order.

Example 2

Input: nums = [5, 4, 4, 1, 1]

Output: [1, 1, 4, 4, 5]

Explanation: 1 <= 1 <= 4 <= 4 <= 5.

Thus the array is sorted in non-decreasing order.
"""


class Solution(object):
    @staticmethod
    def bubble_sort(arr: list[int]):
        for i in range(len(arr) - 1):
            swapped = False
            for j in range(len(arr) - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True

            if not swapped:
                return arr


if __name__ == "__main__":
    result = Solution.bubble_sort([7, 4, 1, 5, 3])
    print(result)
