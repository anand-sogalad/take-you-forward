"""
You are given an integer n. Return the value of n! or n factorial.

Factorial of a number is the product of all positive integers less than or equal to that number.
"""


class Solution(object):
    @staticmethod
    def factorial(n: int):
        if n <= 1:
            return 1

        return n * Solution.factorial(n - 1)


if __name__ == "__main__":
    result = Solution.factorial(0)
    print(result)
