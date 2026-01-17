"""
You are given an integer n. You need to check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.
An armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.
"""


class Solution(object):
    def is_amstrong(self, n: int) -> bool:
        armstrong = 0
        digits = 0

        # get the number of digits
        copy = n
        while n > 0:
            n //= 10
            digits += 1

        # get armstrong value
        n = copy
        while n > 0:
            armstrong += (n % 10) ** digits
            n //= 10

        # result
        return copy == armstrong


if __name__ == "__main__":
    for i, j in (153, True), (12, False):
        assert Solution().is_amstrong(i) == j
