"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
    *
   ***
  *****
 *******
*********
"""


class Solution(object):
    def pattern7(self, n):
        for i in range(n):
            # for spaces
            for _ in range(n - (i + 1)):
                print(" ", end="")
            # for stars
            for _ in range(2 * i + 1):
                print("*", end="")
            print()

    def pattern72(self, n):
        for i in range(n):
            print("".join([" " for _ in range(n - i - 1)]), end="")
            print("".join(["*" for j in range(2 * i + 1)]))

    def pattern73(self, n):
        for i in range(n):
            print((" " * (n - i - 1)) + ("*" * (2 * i + 1)))


if __name__ == "__main__":
    Solution().pattern7(10)
    Solution().pattern72(10)
    Solution().pattern73(10)
