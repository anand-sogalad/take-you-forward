"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
"""


class Solution(object):
    def some_of_digits(self, num: int):
        if num < 10:
            return num

        num = sum(list(map(int, str(num))))

        return self.some_of_digits(num)

    def some_of_digits1(self, num: int):
        return self._sum_of_digits(num)

    def _sum_of_digits(self, num: int):
        if num < 10:
            return num

        total = 0
        while num > 0:
            digit = num % 10
            total += digit
            num //= 10

        return self._sum_of_digits(total)


if __name__ == "__main__":
    result = Solution().some_of_digits(529)
    print(result)

    result1 = Solution().some_of_digits1(529)
    print(result1)
