"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
A
AB
ABC
ABCD
ABCDE
Print the pattern in the function given to you.
"""


class Solution(object):
    def pattern14(self, n: int):
        if 1 <= n <= 26:
            for i in range(n):
                start = ord("A")
                for _ in range(i + 1):
                    print(chr(start), end="")
                    start += 1
                print()


if __name__ == "__main__":
    Solution().pattern14(5)
