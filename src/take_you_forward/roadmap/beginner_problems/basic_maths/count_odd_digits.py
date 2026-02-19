"""
You are given an integer n. You need to return the number of odd digits present in the number.



The number will have no leading zeroes, except when the number is 0 itself.
"""


class Solution(object):
    @staticmethod
    def count_odd_digits(n: int):

        digits = 0
        while n > 0:
            if n % 10 != 0:
                digits += 1

            n //= 10

        return digits


if __name__ == "__main__":
    result = Solution.count_odd_digits(15)
    print(result)
