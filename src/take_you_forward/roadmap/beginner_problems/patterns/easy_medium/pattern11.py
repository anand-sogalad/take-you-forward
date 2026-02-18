"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



1

0 1

1 0 1

0 1 0 1

1 0 1 0 1



Print the pattern in the function given to you.
"""


class Solution(object):
    @staticmethod
    def pattern11(n: int):

        for i in range(n):
            start = 1 if i % 2 == 0 else 0

            for j in range(i + 1):
                print(start, end="")
                start = 1 - start
            print()


if __name__ == "__main__":
    Solution.pattern11(5)
