"""
You are given an integer n. Return the integer formed by placing the digits of n in reverse order.


Example 1

Input: n = 25

Output: 52

Explanation: Reverse of 25 is 52.
"""


class Solution(object):
    @staticmethod
    def reverse_number(n: int):

        reversed = 0

        while n > 0:
            reversed = reversed * 10 + (n % 10)
            n //= 10

        return reversed


if __name__ == "__main__":
    result = Solution.reverse_number(102)
    print(result)
