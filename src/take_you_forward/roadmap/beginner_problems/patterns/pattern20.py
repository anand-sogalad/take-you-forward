"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *


Print the pattern in the function given to you.
"""


class Solution(object):
    @staticmethod
    def pattern20(n: int):

        for i in range(1, n + 1):
            for j in range(i):
                print("*", end="")

            for k in range((n - i) * 2):
                print(" ", end="")

            for l in range(i):
                print("*", end="")

            print()

        for i in range(n-1, 0, -1):
            for j in range(i):
                print("*", end="")

            for k in range((n - i) * 2):
                print(" ", end="")

            for l in range(i):
                print("*", end="")

            print()


if __name__ == "__main__":
    Solution.pattern20(5)
