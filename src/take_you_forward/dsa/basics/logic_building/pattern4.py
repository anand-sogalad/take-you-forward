"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
1
22
333
4444
55555
"""


class Solution(object):
    def pattern4(self, n):
        for i in range(n):
            for _ in range(i + 1):
                print(i + 1, end="")
            print()

    def pattern42(self, n):
        for i in range(1, n + 1):
            for _ in range(i):
                print(i, end="")
            print()


if __name__ == "__main__":
    Solution().pattern4(10)
    Solution().pattern42(10)
