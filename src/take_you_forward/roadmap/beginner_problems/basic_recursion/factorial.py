"""
Factorial of a Given Number
Easy

Company
Given an integer n, return the factorial of n.



Factorial of a non-negative integer, is the multiplication of all integers smaller than or equal to n (use 64-bits to return answer).


Example 1

Input : n = 3

Output : 6

Explanation : Factorial = 1 * 2 * 3 => 6

Example 2

Input : n = 5

Output : 120

Explanation : Factorial = 1 * 2 * 3 * 4 * 5 => 120
"""


class Solution(object):
    @staticmethod
    def factorial(n: int):
        if n <= 1:
            return 1

        return n * Solution.factorial(n - 1)


if __name__ == "__main__":
    result = Solution.factorial(5)
    print(result)
