"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
12345
1234
123
12
1
"""


class Solution(object):
    def pattern6(self, n):
        for i in range(n):
            for j in range(n - i):
                print(j + 1, end="")
            print()

    def pattern62(self, n):
        for i in range(n):
            for j in range(1, (n + 1) - i):
                print(j, end="")
            print()

    def pattern63(self, n):
        for i in range(n, 0, -1):
            for j in range(1, i + 1):
                print(j, end="")
            print()

    def pattern64(self, n):
        for i in range(n, 0, -1):
            print("".join([str(j) for j in range(1, i + 1)]))


if __name__ == "__main__":
    Solution().pattern6(10)
    Solution().pattern62(10)
    Solution().pattern63(10)
    Solution().pattern64(10)
