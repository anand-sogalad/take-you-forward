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
    def pattern20(self, n: int):
        # upper
        for i in range(n):
            # stars
            for _ in range(i + 1):
                print("*", end="")

            # spaces
            for _ in range((n - i - 1) * 2):
                print(" ", end="")

            # stars
            for _ in range(i + 1):
                print("*", end="")
            print()

        # lower
        for i in range(1, n):
            # stars
            for _ in range(n - i):
                print("*", end="")

            # spaces
            for j in range(i * 2):
                print(" ", end="")

            # stars
            for _ in range(n-i):
                print("*", end="")
            print()


if __name__ == "__main__":
    Solution().pattern20(5)
