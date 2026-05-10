from functools import cache

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        # time: O(N ^ 2)
        # space: O(N)
        # method: DP
        
        n = len(nums)
        @cache
        def solve(index: int) -> float:
            if index == n - 1:
                return 0
            result = float('-inf')
            for j in range(index + 1, n):
                if -target <= nums[j] - nums[index] <= target:
                    result = max(result, 1 + solve(j))
            return result
        
        result = solve(0)
        if result == float('-inf'):
            result = -1
        return result