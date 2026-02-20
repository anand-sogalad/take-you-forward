"""
Check if a Number is Prime or Not
Easy

Company
Given an integer num, return true if it is prime otherwise false.



A prime number is a number that is divisible only by 1 and itself.


Example 1

Input : num = 5

Output : true

Explanation : The factors of 5 are 1 and 5 only.

So it satisfies the prime number condition.

Example 2

Input : num = 15

Output : false

Explanation : The factors of 15 are 1, 3, 5, 15 only.

As the number has factors other than 1 and itself, So it is not a prime number.

Now your turn!

Input : num = 41
"""


class Solution(object):
    @staticmethod
    def is_prime(n: int):
        if n <= 1:
            return False

        return Solution._prime(n, n // 2)

    @staticmethod
    def _prime(n, current):
        if n <= 1:
            return True

        if n % current == 0:
            return False

        return Solution._prime(n, current - 1)


if __name__ == "__main__":
    result = Solution.is_prime(10)
    print(result)
