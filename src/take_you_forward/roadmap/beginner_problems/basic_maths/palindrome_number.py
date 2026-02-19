"""
You are given an integer n. You need to check whether the number is a palindrome number or not. Return true if it's a palindrome number, otherwise return false.

A palindrome number is a number which reads the same both left to right and right to left.
"""


class Solution(object):
    @staticmethod
    def palindrome_number(n: int):
        original, reversed = n, 0

        while n > 0:
            reversed = reversed * 10 + (n % 10)
            n //= 10

        return original == reversed


if __name__ == "__main__":
    result = Solution.palindrome_number(100)
    print(result)
