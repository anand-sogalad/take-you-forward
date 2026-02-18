"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



1

22

333

4444

55555



Print the pattern in the function given to you.
"""


class Solution(object):
    @staticmethod
    def pattern4(n: int):
        # as many as row needed
        for i in range(1, n + 1):
            for j in range(i):
                print(i, end="")
            print()

    @staticmethod
    def pattern4_sample2(n: int):
        for i in range(1, n + 1):
            print(f"{i}" * i)


if __name__ == "__main__":
    Solution.pattern4(5)
    Solution.pattern4(5)
