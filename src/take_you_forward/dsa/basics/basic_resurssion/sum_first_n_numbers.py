"""
Given an integer N, return the sum of first N natural numbers. Try to solve this using recursion.
"""


class Solution(object):
    def sum_of_n_numbers(self, n: int):
        if n == 1:
            return 1
        return n + self.sum_of_n_numbers(n - 1)
