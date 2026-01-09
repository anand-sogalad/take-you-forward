"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
1 =
0 1 =
1 0 1
0 1 0 1
1 0 1 0 1
"""


class Solution(object):
    def pattern11(self, n):
        for i in range(n):
            if i % 2 == 0:
                start = 1
            else:
                start = 0

            for _ in range(i + 1):
                print(start, end=" ")
                start = 1 - start
            print()


if __name__ == "__main__":
    Solution().pattern11(10)
