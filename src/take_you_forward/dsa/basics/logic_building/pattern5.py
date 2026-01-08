"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
*****
****
***
**
*
"""


class Solution:
    def pattern5(self, n):
        for i in range(n):
            for _ in range(i, n):
                print("*", end="")
            print()

    def pattern5_2(self, n):
        for i in range(n, 0, -1):
            print("*" * i)


if __name__ == "__main__":
    Solution().pattern5(10)
    Solution().pattern5_2(10)
