"""
Given an integer n. You need to recreate the pattern given below for any value of N.
Let's say for N = 5, the pattern should look like as below:
*
**
***
****
*****
****
***
**
*
"""


class Solution(object):
    def pattern10(self, n):
        # upper
        for i in range(n):
            for _ in range(i + 1):
                print("*", end="")
            print()

        # lower
        for i in range(n - 1):
            for _ in range(n - 1 - i):
                print("*", end="")
            print()


if __name__ == "__main__":
    Solution().pattern10(10)
