class Solution:
    def two_sum_bruteforce(
        self, numbers: list[int], target: int
    ) -> tuple[int, int] | None:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return (i, j)

    # this single pass lookpup method
    #
    def two_sum_one_pass(
        self, numbers: list[int], target: int
    ) -> tuple[int, int] | None:
        seen = {}
        for idx, number in enumerate(numbers):
            if target - number in seen:
                return seen[target - number], idx
            seen[number] = idx

    # this is two pass method
    # should be used only if the given array is sorted already
    def two_sum_two_pass(self, nums: list[int], target: int) -> tuple[int, int] | None:
        left, right = 0, len(nums) - 1
        while left < right:
            current = nums[left] + nums[right]

            if current == target:
                return right, left
            if current < target:
                left += 1
            else:
                right -= 1
