"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
    *      1 + 0
   ***     2 + 1
  *****    3 + 2
 *******   4 + 3
*********  5 + 4


Print the pattern in the function given to you.
"""


class Solution(object):
    @staticmethod
    def pattern7(n: int):
        # total rows
        for i in range(1, n + 1):
            # spaces
            for j in range(n - i):
                print(" ", end="")

            # stars
            for k in range(i + (i - 1)):
                print("*", end="")

            # for nex line
            print()


if __name__ == "__main__":
    Solution.pattern7(5)
