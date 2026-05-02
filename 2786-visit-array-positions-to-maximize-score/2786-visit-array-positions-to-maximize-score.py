from functools import cache

class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        # time: O(N)
        # space: O(N)
        # method: DP
        n = len(nums)

        @cache
        def solve(index: int, fromOdd: bool) -> int:
            if index >= n:
                return 0
            result = solve(index + 1, fromOdd)
            if nums[index] & 1:
                if fromOdd is True:
                    result = max(result, nums[index] + solve(index + 1, True))
                else: # from even number
                    result = max(result, nums[index] - x + solve(index + 1, True))
            else:
                if fromOdd is True:
                    result = max(result, nums[index] - x + solve(index + 1, False))
                else:
                    result = max(result, nums[index] + solve(index + 1, False))
            return result
        
        return solve(0, (nums[0] & 1) > 0)