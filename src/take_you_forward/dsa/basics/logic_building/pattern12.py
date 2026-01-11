"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
1        1
12      21
123    321
1234  4321
1234554321
"""


class Solution(object):
    def pattern12(self, n: int):
        for i in range(1, n + 1):
            # print number
            for j in range(1, i + 1):
                print(j, end="")

            # print space
            for _ in range((n - i) * 2):
                print(" ", end="")

            # print number
            for j in range(i, 0, -1):
                print(j, end="")
            print()


if __name__ == "__main__":
    Solution().pattern12(5)
