"""
You are given an integer n. You need to check if the number is prime or not. Return true if it is a prime number, otherwise return false.

A prime number is a number which has no divisors except 1 and itself.
"""


class Solution(object):
    @staticmethod
    def is_prime(n: int):
        if n <= 1:
            return False

        for i in range(2, n // 2 + 1):
            if n % 2 == 0 and n != i:
                return False

        return True


if __name__ == "__main__":
    result = Solution.is_prime(6)
    print(result)
