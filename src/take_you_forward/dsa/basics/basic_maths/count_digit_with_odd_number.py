"""
You are given an integer n. You need to return the number of odd digits present in the number.
The number will have no leading zeroes, except when the number is 0 itself.
"""


class Solution(object):
    def count_odd_digits(self, n: int) -> int:
        counter = 0
        while n > 0:
            # increase the counter if the last digit is not even number
            counter = counter + 1 if (n % 10) % 2 != 0 else counter

            # remove last digit from n
            n //= 10

        # return the result
        return counter


if __name__ == "__main__":
    for num, res in (5, 1), (25, 1):
        assert Solution().count_odd_digits(num) == res
