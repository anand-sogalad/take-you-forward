"""
You are given an integer n. Return the largest digit present in the number.
"""


class Solution(object):
    @staticmethod
    def largest_digit(n: int):

        largest = 0
        while n > 0:
            ld = n % 10
            largest = max(largest, ld)
            n //= 10

        return largest


if __name__ == "__main__":
    result = Solution.largest_digit(1589760)
    print(result)
