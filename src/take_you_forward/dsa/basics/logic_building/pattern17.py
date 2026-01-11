"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
    A = 0, 1
   ABA = 1, 2
  ABCBA
 ABCDCBA
ABCDEDCBA
"""


class Solution(object):
    def pattern17(self, n: int):
        for i in range(n):
            # print spaces
            for _ in range(n - (i + 1)):
                print(" ", end="")

            # print numbers
            ch = ord("A")
            for _ in range((i * 2 + 1) // 2):
                print(chr(ch), end="")
                ch += 1

            for _ in range(((i * 2 + 1) // 2) + 1):
                print(chr(ch), end="")
                ch -= 1

            print()


if __name__ == "__main__":
    Solution().pattern17(5)
