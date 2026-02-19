"""
Reverse an array
Easy

Company
Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.


Example 1

Input: n=5, arr = [1,2,3,4,5]



Output: [5,4,3,2,1]



Explanation: The reverse of the array [1,2,3,4,5] is [5,4,3,2,1]
"""


class Solution(object):
    @staticmethod
    def reverse_array(arr: list[int]) -> list[int]:
        if len(arr) <= 1:
            return arr

        left, right = 0, len(arr) - 1

        while left <= right:
            arr[left], arr[right] = arr[right], arr[left]

            left += 1
            right -= 1

        return arr


if __name__ == "__main__":
    result = Solution.reverse_array([1, 2, 3, 4, 5, 6, 7, 8, 8, 9])
    print(result)
