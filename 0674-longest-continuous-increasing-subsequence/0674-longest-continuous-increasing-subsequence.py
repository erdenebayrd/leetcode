class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # time: O(N)
        # space: O(1)
        # method: dp

        n = len(nums)
        result = 1
        current_streak = 1
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                current_streak += 1
            else:
                current_streak = 1
            result = max(result, current_streak)
        return result