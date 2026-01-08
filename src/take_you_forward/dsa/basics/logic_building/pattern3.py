"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
1
12
123
1234
12345
"""


class Solution(object):
    def pattern3(self, n):
        for i in range(n):
            for j in range(i + 1):
                print(j + 1, end="")
            print()

    def pattern32(self, n):
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end="")
            print()

    def pattern33(self, n):
        for i in range(1, n + 1):
            print("".join([str(j) for j in range(1, i + 1)]))


if __name__ == "__main__":
    Solution().pattern3(10)
    Solution().pattern32(10)
    Solution().pattern33(10)
