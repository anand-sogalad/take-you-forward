"""
You are given an integer n. You need to return the number of digits in the number.

The number will have no leading zeroes, except when the number is 0 itself.
"""


class Solution(object):
    @staticmethod
    def count_digits(n: int):
        digits = 0
        while n > 0:
            n //= 10
            digits += 1

        return digits


if __name__ == "__main__":
    result = Solution.count_digits(50)
    print(result)
