"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



*

**

***

****

*****

****

***

**

*



Print the pattern in the function given to you.
"""


class Solution(object):
    @staticmethod
    def pattern10(n: int):

        # upper part
        for i in range(1, n + 1):
            for j in range(i):
                print("*", end="")
            print()

        # lower
        for i in range(n - 1, 0, -1):
            for j in range(i):
                print("*", end="")
            print()


if __name__ == "__main__":
    Solution.pattern10(5)
