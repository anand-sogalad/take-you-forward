"""
You are given an integer n. Return the integer formed by placing the digits of n in reverse order.
"""


class Solution(object):
    def reverse_number(self, n: int):
        reversed = 0
        while n > 0:
            # reverse a number
            reversed = reversed * 10 + (n % 10)

            # remove the last digit
            n //= 10

        return reversed


if __name__ == "__main__":
    result = Solution().reverse_number(321)
    print(result)
