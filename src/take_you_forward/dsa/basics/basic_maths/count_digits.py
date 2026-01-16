"""
You are given an integer n. You need to return the number of digits in the number.
The number will have no leading zeroes, except when the number is 0 itself.
"""


class Solution(object):
    def count_digit(self, n: int):
        # return 1 if n is between 0 and 9
        if 0 <= n <= 9:
            return 1

        count = 0
        while 0 < n:
            n //= 10
            count += 1

        return count


if __name__ == "__main__":
    result = Solution().count_digit(10)
    print(result)
