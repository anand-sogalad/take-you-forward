"""
Pattern 2
Easy

Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



*

**

***

****

*****


"""


class Solution(object):
    @staticmethod
    def pattern2(n: int):

        # n number of rows needed
        for i in range(1, n + 1):
            # i number of columns needed
            for j in range(i):
                print("*", end="")
            print()

    @staticmethod
    def pattern2_sample2(n: int):
        # n number of rows needed
        for i in range(1, n + 1):
            # number of * needed
            print("*" * i)


if __name__ == "__main__":
    Solution.pattern2(4)
    Solution.pattern2_sample2(5)

# time complexity O(n^2)
# space complexity O(1)
