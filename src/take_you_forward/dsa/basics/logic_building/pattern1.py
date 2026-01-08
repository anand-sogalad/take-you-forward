"""
Given an integer n. You need to recreate the pattern given below for any value of N.
Let's say for N = 5, the pattern should look like as below:
*****
*****
*****
*****
*****
"""


class Solution:
    def pattern1(self, n: int):
        for _ in range(n):
            for _ in range(n):
                print("*", end="")
            print()

    def pattern1_2(self, n: int):
        for _ in range(n):
            print("*" * n)


if __name__ == "__main__":
    Solution().pattern1(4)
    Solution().pattern1_2(5)
