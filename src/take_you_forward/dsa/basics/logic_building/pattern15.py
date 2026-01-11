"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
ABCDE
ABCD
ABC
AB
A
"""


class Solution(object):
    def pattern15(self, n: int):
        if 1 <= n <= 26:
            for i in range(n):
                start = ord("A")
                for _ in range(n - i):
                    print(chr(start), end="")
                    start += 1
                print()


if __name__ == "__main__":
    Solution().pattern15(5)
