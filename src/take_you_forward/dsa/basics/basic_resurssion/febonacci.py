"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
"""


class Solution(object):
    def febonacci(self, num: int):
        if num == 0:
            return 0
        if num == 1:
            return 1
        return self.febonacci(num - 1) + self.febonacci(num - 2)


if __name__ == "__main__":
    result = Solution().febonacci(6)
    print(result)
