"""
Insertion Sorting
Easy

Hints
Company
Given an array of integers called nums, sort the array in non-decreasing order using the insertion sort algorithm and return the sorted array.



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
    def insertion_sort(arr: list[int]):
        """
        Insertion Sort Algorithm

        How it works:
        1. Start from the second element (index 1)
        2. Compare it with elements before it
        3. Shift larger elements one position to the right
        4. Insert the current element in its correct position
        5. Repeat for all elements

        Time Complexity: O(n²) worst case, O(n) best case
        Space Complexity: O(1) - sorts in place

        Example: [7, 4, 1, 5, 3]
        Pass 1: [4, 7, 1, 5, 3] - Insert 4
        Pass 2: [1, 4, 7, 5, 3] - Insert 1
        Pass 3: [1, 4, 5, 7, 3] - Insert 5
        Pass 4: [1, 3, 4, 5, 7] - Insert 3
        """
        # Start from second element
        for i in range(1, len(arr)):
            key = arr[i]  # Element to be inserted
            j = i - 1  # Index of the last element in sorted portion

            # Shift larger elements one position to the right
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1

            # Insert the key at its correct position
            arr[j + 1] = key

        return arr
