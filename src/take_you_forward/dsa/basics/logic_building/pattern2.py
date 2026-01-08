"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

*
**
***
****
*****
"""


class Solution(object):
    def pattern2(self, n):
        for i in range(n):
            for _ in range(i + 1):
                print("*", end="")
            print()

    def pattern22(self, n):
        for i in range(n):
            print("*" * (i + 1))

    def pattern23(self, n):
        for i in range(1, n + 1):
            print("*" * i)


if __name__ == "__main__":
    Solution().pattern2(10)
    Solution().pattern22(10)
    Solution().pattern23(10)
