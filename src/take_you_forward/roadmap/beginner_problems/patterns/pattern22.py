"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 2 1 2 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 5
5 5 5 5 5 5 5 5 5


Print the pattern in the function given to you.
"""


class Solution:
    # Function to print pattern22
    def pattern22(self, n):
        # Outer loop for the rows
        for i in range(2 * n - 1):
            # Inner loop for the columns
            for j in range(2 * n - 1):
                top = i
                left = j
                right = (2 * n - 2) - j
                bottom = (2 * n - 2) - i

                print((n - min(min(top, bottom), min(left, right))), end=" ")

            # Move to the next row
            print()
