"""
Given an array of n integers, find the sum of the frequencies of the highest occurring number and lowest occurring number.


Example 1

Input: arr = [1, 2, 2, 3, 3, 3]

Output: 4

Explanation: The highest frequency is 3 (element 3), and the lowest frequency is 1 (element 1). Their sum is 3 + 1 = 4.

Example 2

Input: arr = [4, 4, 5, 5, 6]

Output: 3

Explanation: The highest frequency is 2 (elements 4 and 5), and the lowest frequency is 1 (element 6). Their sum is 2 + 1 = 3.
"""


class Solution(object):
    @staticmethod
    def highest_lowest_sum(arr: list[int]) -> int:
        freq: dict[int, int] = {}
        for n in arr:
            freq[n] = freq.get(n, 0) + 1

        max, min = 0, len(arr) + 1

        for num, count in freq.items():
            if count > max:
                max = count
            if count < min:
                min = count

        return min + max


if __name__ == "__main__":
    result = Solution.highest_lowest_sum([1, 2, 2, 3, 3, 3])
    print(result)
