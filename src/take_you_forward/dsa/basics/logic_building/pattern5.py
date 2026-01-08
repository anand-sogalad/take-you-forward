"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
*****
****
***
**
*
"""


class Solution(object):
    def pattern5(self, n):
        for i in range(n):
            for _ in range(n - i):
                print("*", end="")
            print()

    def pattern52(self, n):
        for i in range(n):
            print("*" * (n - i))

    def pattern53(self, n):
        for i in range(n, 0, -1):
            print("*" * i)

    def pattern54(self, n):
        for i in range(n):
            for _ in range(i, n):
                print("*", end="")
            print()


if __name__ == "__main__":
    Solution().pattern5(10)
    Solution().pattern52(10)
    Solution().pattern53(10)
    Solution().pattern54(10)
