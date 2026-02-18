"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



A

AB

ABC

ABCD

ABCDE



Print the pattern in the function given to you.
"""


class Solution(object):
    @staticmethod
    def pattern14(n: int):
        for i in range(1, n + 1):
            ch = ord("A")
            for j in range(i):
                print(chr(ch), end="")
                ch += 1
            print()


if __name__ == "__main__":
    Solution.pattern14(5)
