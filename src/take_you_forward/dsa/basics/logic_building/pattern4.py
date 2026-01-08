"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
1
22
333
4444
55555
"""


class Solution:
    def pattern4(self, n):
        for i in range(1, n + 1):
            for _ in range(1, i + 1):
                print(i, end="")
            print()

    def pattern4_2(self, n):
        for i in range(1, n + 1):
            print(str(i) * i)


if __name__ == "__main__":
    Solution().pattern4(10)
    Solution().pattern4_2(10)
