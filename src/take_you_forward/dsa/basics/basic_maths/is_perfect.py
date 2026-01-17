"""
You are given an integer n. You need to check if the number is a perfect number or not. Return true if it is a perfect number, otherwise, return false.
A perfect number is a number whose proper divisors (excluding the number itself) add up to the number itself.
"""


class Solution(object):
    def is_perfect(self, n: int) -> bool:
        sum = 0
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                sum += i

        return n == sum


if __name__ == "__main__":
    for i, j in (6, True), (4, False):
        assert Solution().is_perfect(i) == j
