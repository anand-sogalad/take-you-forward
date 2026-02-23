"""
Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.
"""


def second_largest(arr: list[int]) -> int:
    largest, second_largest = arr[0], None

    for i in range(1, len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] != largest and (second_largest is None or arr[i] > second_largest):
            second_largest = arr[i]

    return second_largest if second_largest else -1


if __name__ == "__main__":
    result = second_largest([8, 8, 7, 6, 5])
    print(result)
