"""
Given an integer n, return the factorial of n.

Factorial of a non-negative integer, is the multiplication of all integers smaller than or equal to n (use 64-bits to return answer).
"""


class Solution(object):
    def factorial(self, n: int):
        if n == 1:
            return 1
        return n * self.factorial(n - 1)
