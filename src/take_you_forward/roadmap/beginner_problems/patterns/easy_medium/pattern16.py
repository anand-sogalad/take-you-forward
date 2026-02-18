"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



A

BB

CCC

DDDD

EEEEE



Print the pattern in the function given to you.

"""


class Solution(object):
    @staticmethod
    def pattern16(n: int):
        ch = ord("A")
        for i in range(n):
            for j in range(i + 1):
                print(chr(ch), end="")
            print()
            ch += 1


if __name__ == "__main__":
    Solution.pattern16(5)
