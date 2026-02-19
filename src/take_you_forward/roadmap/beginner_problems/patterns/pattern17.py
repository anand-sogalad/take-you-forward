"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA


Print the pattern in the function given to you.
"""


class Solution(object):
    @staticmethod
    def pattern17(n):
        for i in range(1, n + 1):
            ch = ord("A")

            # spaces
            for k in range(n - i):
                print(" ", end="")

            # first half
            for j in range(i):
                print(chr(ch), end="")
                ch += 1

            ch -= 1

            # second half
            for k in range(i - 1, 0, -1):
                ch -= 1
                print(chr(ch), end="")
            print()


if __name__ == "__main__":
    Solution.pattern17(5)
