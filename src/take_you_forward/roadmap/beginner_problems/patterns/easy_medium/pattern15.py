"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



ABCDE

ABCD

ABC

AB

A



Print the pattern in the function given to you.
"""


class Solution(object):
    @staticmethod
    def pattern15(n: int):
        for i in range(n, 0, -1):
            ch = ord("A")
            for j in range(i):
                print(chr(ch), end="")
                ch += 1
            print()


if __name__ == "__main__":
    Solution.pattern15(5)
