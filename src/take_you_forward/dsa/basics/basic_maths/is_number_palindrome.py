"""
You are given an integer n. You need to check whether the number is a palindrome number or not. Return true if it's a palindrome number, otherwise return false.
A palindrome number is a number which reads the same both left to right and right to left.
"""


class Solution(object):
    def is_number_palindrome(self, n: int) -> bool:
        # variables to store original and reversed number
        origional = n
        reversed = 0

        while n > 0:
            # reverse a number
            reversed = reversed * 10 + (n % 10)

            # remove last digit
            n //= 10

        return origional == reversed


if __name__ == "__main__":
    for num, res in (121, True), (123, False):
        assert Solution().is_number_palindrome(num) == res
