"""
Second Highest Occurring Element
Easy

Company
Given an array of n integers, find the second most frequent element in it.

If there are multiple elements that appear second most frequent times, find the smallest of them.

If second most frequent element does not exist return -1.
"""


class Solution(object):
    @staticmethod
    def second_most_occuring_element(arr: list[int]):
        mapping: dict[int, int] = {}

        # create hash map with frequency
        for num in arr:
            mapping[num] = mapping.get(num, 0) + 1

        max_key, max_count, second_key, second_count = 0, 0, 0, 0

        for key, count in mapping.items():
            if count > max_count:
                second_key, second_count = max_key, max_count
                max_key, max_count = key, count
            elif count == max_count:
                max_key = min(max_key, key)
            elif second_key < count < max_count:
                second_key, second_count = key, count
            elif count == second_count:
                second_key = min(second_key, key)

        return second_key if second_count != 0 else -1


if __name__ == "__main__":
    result = Solution.second_most_occuring_element([1, 2, 2, 3, 3, 3])
    print(result)
