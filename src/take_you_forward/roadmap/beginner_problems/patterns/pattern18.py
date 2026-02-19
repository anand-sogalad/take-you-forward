"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



E

D E

C D E

B C D E

A B C D E



Print the pattern in the function given to you.
"""


class Solution(object):
    @staticmethod
    def pattern18(n: int):
        for i in range(n, 0, -1):
            ch = ord("A") + i - 1
            for j in range((n - i) + 1):
                print(chr(ch), end="")
                ch += 1
            print()


if __name__ == "__main__":
    Solution.pattern18(5)
