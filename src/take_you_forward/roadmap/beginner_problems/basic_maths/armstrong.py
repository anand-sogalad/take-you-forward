"""
You are given an integer n. You need to check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.

An armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.
"""


class Solution(object):
    @staticmethod
    def is_armstrong(n: int):
        armstrong, digits = 0, 0

        # get digits
        copy = n
        while n > 0:
            n //= 10
            digits += 1

        # check armstrong
        n = copy
        while n > 0:
            armstrong += (n % 10) ** digits
            n //= 10
        return copy == armstrong


if __name__ == "__main__":
    result = Solution.is_armstrong(153)
    print(result)
