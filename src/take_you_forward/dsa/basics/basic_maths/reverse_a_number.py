"""
You are given an integer n. Return the integer formed by placing the digits of n in reverse order.
"""


class Solution(object):
    def reverse_number(self, n: int):
        if 0 <= n <= 9:
            return n

        result = 0

        while n > 0:
            # get the last digit
            last = n % 10
            result = result * 10 + last

            # remove the last digit
            n //= 10

        return result


if __name__ == "__main__":
    result = Solution().reverse_number(321)
    print(result)
