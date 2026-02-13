"""
Pattern 1
Easy

Company
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



*****

*****

*****

*****

*****
"""


class Solution(object):
    @staticmethod
    def pattern1(n: int):
        # n number of rows to be printed
        for i in range(n):
            # each row should have n number of *
            for j in range(n):
                print("*", end="")
            print()

    @staticmethod
    def pattern1_sample2(n: int):
        # n number of rows needed
        for i in range(n):
            print("*" * n)  # in each row n number of * should be printed

    @staticmethod
    def pattern1_sample3(n: int):
        pattern = ("*" * n + "\n") * n
        print(pattern)


if __name__ == "__main__":
    Solution.pattern1(4)
    Solution.pattern1_sample2(5)
    Solution.pattern1_sample3(6)


# time complexity - O(n^2)
# sapce complexity - O(1)
