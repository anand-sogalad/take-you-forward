"""
You are given an integer n. Return the largest digit present in the number.
"""


class Solution(object):
    def largest_digit(self, n: int) -> int:
        largest = 0

        while n > 0:
            largest = max(largest, n % 10)
            n //= 10
        return largest


if __name__ == "__main__":
    for num, res in (25, 5), (99, 9):
        assert Solution().largest_digit(num) == res
