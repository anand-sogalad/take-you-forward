"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



12345
1234
123
12
1



Print the pattern in the function given to you.
"""


class Solution(object):
    @staticmethod
    def pattern6(n: int):
        for i in range(n, 0, -1):
            for j in range(1, i + 1):
                print(j, end="")
            print()


if __name__ == "__main__":
    Solution.pattern6(5)
