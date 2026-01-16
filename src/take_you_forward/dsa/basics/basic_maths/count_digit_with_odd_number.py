"""
You are given an integer n. You need to return the number of odd digits present in the number.
The number will have no leading zeroes, except when the number is 0 itself.
"""


class Solution(object):
    def count_odd_number_of_digits(self, n: int):
        count = 0
        while n > 0:
            # get the last digit and check if it even ort odd
            ld = n % 10

            if ld % 2 != 0:
                count += 1

            # continue removing last digit
            n //= 10
        return count


if __name__ == "__main__":
    result = Solution().count_odd_number_of_digits(12345)
    print(result)
