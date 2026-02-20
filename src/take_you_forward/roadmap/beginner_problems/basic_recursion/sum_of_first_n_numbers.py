"""
Sum of First N Numbers
Easy

Company
Given an integer N, return the sum of first N natural numbers. Try to solve this using recursion.


Example 1

Input : N = 4

Output : 10

Explanation : first four natural numbers are 1, 2, 3, 4.

Sum is 1 + 2 + 3 + 4 => 10.

Example 2

Input : N = 2

Output : 3

Explanation : first two natural numbers are 1, 2.

Sum is 1 + 2 => 3.
"""


class Solution(object):
    @staticmethod
    def sum_of_n(n: int):
        if n == 1:
            return 1

        return n + Solution.sum_of_n(n - 1)


if __name__ == "__main__":
    result = Solution.sum_of_n(4)
    print(result)
