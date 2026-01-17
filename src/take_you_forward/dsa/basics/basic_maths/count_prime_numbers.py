"""
You are given an integer n. You need to find out the number of prime numbers in the range [1, n] (inclusive). Return the number of prime numbers in the range.
A prime number is a number which has no divisors except, 1 and itself.
"""


class Solution(object):
    def count_prime_numbers(self, n) -> int:
        count = 0

        if n >= 2:
            for i in range(2, n + 1):
                for j in range(2, i // 2 + 1):
                    if i % j == 0 and i != j:
                        break
                else:
                    count += 1

        return count


if __name__ == "__main__":
    for i, j in (6, 3), (10, 4):
        assert Solution().count_prime_numbers(i) == j
