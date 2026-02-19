"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



*****

****

***

**

*



Print the pattern in the function given to you.
"""


class Solution(object):
    @staticmethod
    def pattern5(n: int):
        for i in range(n, 0, -1):
            for j in range(i):
                print("*", end="")
            print()

    @staticmethod
    def pattern5_sample2(n: int):
        for i in range(n, 0, -1):
            print("*" * i)


if __name__ == "__main__":
    Solution.pattern5(5)
    Solution.pattern5_sample2(5)
