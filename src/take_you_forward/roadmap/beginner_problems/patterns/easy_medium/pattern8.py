"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

********* 5 + 4
 *******  4 + 3
  *****   3 + 2
   ***    2 + 1
    *     1 + 0


Print the pattern in the function given to you.
"""


class Solution(object):
    @staticmethod
    def pattern8(n: int):
        for i in range(n, 0, -1):
            # for space
            for j in range(n - i):
                print(" ", end="")

            # for star
            for k in range(i + (i - 1)):
                print("*", end="")

            print()


if __name__ == "__main__":
    Solution.pattern8(5)
