"""
You are given an integer n. Return the value of n! or n factorial.
Factorial of a number is the product of all positive integers less than or equal to that number.
"""


class Solution(object):
    def factorial(self, n: int) -> int:
        if n == 0:
            return 1

        facto = 1

        for i in range(1, n + 1):
            facto *= i

        return facto

    def factorial_recurssion(self, n: int):
        if 0 >= n <= 1:
            return 1

        return n * self.factorial_recurssion(n - 1)


if __name__ == "__main__":
    for i, j in (2, 2), (0, 1):
        assert Solution().factorial(i) == j
        assert Solution().factorial_recurssion(i) == j
