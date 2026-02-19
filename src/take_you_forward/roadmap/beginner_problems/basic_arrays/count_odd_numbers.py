"""
Count of odd numbers in array
Easy

Company
Given an array of n elements. The task is to return the count of the number of odd numbers in the array.


Example 1

Input: n=5, array = [1,2,3,4,5]



Output: 3



Explanation: The three odd elements are (1,3,5).
"""


class Solution(object):
    @staticmethod
    def count_odd_numbers(arr: list[int]):
        counter = 0
        for num in arr:
            if num % 2 != 0:
                counter += 1
        return counter


if __name__ == "__main__":
    result = Solution.count_odd_numbers([1, 2, 3, 4, 5])
    print(result)
