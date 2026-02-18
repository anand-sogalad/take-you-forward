"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *


Print the pattern in the function given to you.
"""


class Solution(object):
    @staticmethod
    def pattern9(n: int):

        # uppper part
        for i in range(1, n + 1):
            # spaces
            for j in range(n - i):
                print(" ", end="")
            # stars
            for k in range(i + (i - 1)):
                print("*", end="")

            print()  # new line

        # lower part
        for i in range(n, 0, -1):
            # spaces
            for j in range(n - i):
                print(" ", end="")

            # stars
            for k in range(i + (i - 1)):
                print("*", end="")

            print()


if __name__ == "__main__":
    Solution.pattern9(5)
