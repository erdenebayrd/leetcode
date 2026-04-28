class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # # time: O(N log max(nums))
        # # space: O(1)
        # # method: binary search + right to left iteration

        # n = len(nums)

        # def can(limit: int) -> int:
        #     delta = 0
        #     for i in range(n - 1, -1, -1):
        #         if nums[i] > limit:
        #             delta += nums[i] - limit
        #         else:
        #             delta -= min(delta, limit - nums[i])
        #     return delta == 0

        # low, high = min(nums) - 1, max(nums) + 1
        # while low + 1 < high:
        #     mid = (low + high) // 2
        #     if can(mid):
        #         high = mid
        #     else:
        #         low = mid
        # return high

        # time: O(N)
        # space: O(1)
        # method: math
        n = len(nums)
        total = sum(nums)
        average = total // n + int(total % n > 0)
        currentSum = 0
        for i in range(n):
            currentCount = i + 1
            currentSum += nums[i]
            if nums[i] > average:
                average = max(average, currentSum // currentCount + int(currentSum % currentCount > 0))
        return average