"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
*****
*   *
*   *
*   *
*****
Print the pattern in the function given to you.
"""


class Solution(object):
    def pattern21(self, n: int):
        for i in range(n):
            for j in range(n):
                if i == 0 or j == 0 or i == n - 1 or j == n - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()


if __name__ == "__main__":
    Solution().pattern21(4)
