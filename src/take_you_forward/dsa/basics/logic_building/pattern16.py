"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
A
BB
CCC
DDDD
EEEEE
"""


class Solution(object):
    def pattern16(self, n: int):
        ch = ord("A")
        for i in range(ch, ch + n):
            for _ in range(ch, i + 1):
                print(chr(i), end="")
            print()


if __name__ == "__main__":
    Solution().pattern16(5)
