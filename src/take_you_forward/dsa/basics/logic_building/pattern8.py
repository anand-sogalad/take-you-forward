"""
Given an integer n. You need to recreate the pattern given below for any value of N.
Let's say for N = 5, the pattern should look like as below:
********* i*2 -1
 ******* 4*2 -1
  *****
   ***
    *
"""


class Solution(object):
    def pattern8(self, n):
        for i in range(n):
            # for space
            for _ in range(i):
                print(" ", end="")

            # for star
            for _ in range(n * 2 - (i * 2 + 1)):
                print("*", end="")
            print()

    def pattern82(self, n):
        for i in range(n, 0, -1):
            # for space
            for _ in range(n - i):
                print(" ", end="")

            # for star
            for k in range(i * 2 - 1):
                print("*", end="")
            print()


if __name__ == "__main__":
    Solution().pattern8(10)
    Solution().pattern82(10)
