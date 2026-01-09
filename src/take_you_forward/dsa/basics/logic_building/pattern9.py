"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
    *
   ***
  *****
 *******
*********
********* n*2 - (i*2+1)
 ******* 5*2 - (1*2+1)
  *****
   ***
    *
"""


class Solution(object):
    def pattern9(self, n):
        # upper
        for i in range(n):
            # for space
            for _ in range(n - i - 1):
                print(" ", end="")

            # for star
            for _ in range(i * 2 + 1):
                print("*", end="")
            print()

        # lower
        for i in range(n):
            # for space
            for _ in range(i):
                print(" ", end="")

            # for star
            for _ in range(n * 2 - (i * 2 + 1)):
                print("*", end="")
            print()


if __name__ == "__main__":
    Solution().pattern9(10)
