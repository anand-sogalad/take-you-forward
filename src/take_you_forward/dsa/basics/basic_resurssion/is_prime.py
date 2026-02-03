"""
Given an integer num, return true if it is prime otherwise false.



A prime number is a number that is divisible only by 1 and itself.
"""


class Solution(object):
    def is_prime(self, num):
        if num <= 1:
            return False

        return self._divide(num, num // 2)

    def _divide(self, num, n):
        if n <= 1:
            return True

        if num % n == 0:
            return False

        return self._divide(num, n - 1)


if __name__ == "__main__":
    for i in 5, 15, 1, 2, 3, 4:
        print(Solution().is_prime(i))
