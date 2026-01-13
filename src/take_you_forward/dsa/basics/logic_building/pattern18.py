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
    def pattern18(self, n: int):
        for i in range(n):
            for j in range(ord("A") + n - (i + 1), ord("A") + n):
                print(chr(j), end=" ")
            print()


if __name__ == "__main__":
    Solution().pattern18(5)
