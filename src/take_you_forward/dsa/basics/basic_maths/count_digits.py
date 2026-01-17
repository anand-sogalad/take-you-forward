"""
You are given an integer n. You need to return the number of digits in the number.
The number will have no leading zeroes, except when the number is 0 itself.
"""


class Solution(object):
    def count_digits(self, n: int) -> int:
        # if n is in single digit return 1
        if 0 <= n <= 0:
            return 1

        # otherwise calculate digits it by diving by 10
        counter = 0
        while n > 0:
            n //= 10
            counter += 1

        # return the result
        return counter


if __name__ == "__main__":
    assert Solution().count_digits(12345) == 5
