"""
Pattern 3
Easy

Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



1

12

123

1234

12345
"""


class Solution(object):
    @staticmethod
    def pattern3(n: int):

        # n number of rows needed
        for i in range(1, n + 1):
            # i number columns needed in each row
            for j in range(1, i + 1):
                print(j, end="")
            print()

    @staticmethod
    def pattern3_sample2(n: int):
        # n number of rows needed
        for i in range(1, n + 1):
            print("".join([str(j) for j in range(1, i + 1)]))


if __name__ == "__main__":
    Solution.pattern3(5)  # this is better than second approach
    Solution.pattern3_sample2(6)  # this uses more spaces and string operations

# space complexity O(1)
# time complexity O(n^2)
