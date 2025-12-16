class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def solve(idx: int, cur: int) -> int:
            if idx >= n:
                return int(cur == target)
            res = solve(idx + 1, cur - nums[idx])
            res += solve(idx + 1, cur + nums[idx])
            return res
        
        return solve(0, 0)