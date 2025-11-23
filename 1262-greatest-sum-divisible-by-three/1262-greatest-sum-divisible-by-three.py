class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        inf = int(1e18)
        
        @cache
        def solve(idx: int, mod: int) -> int:
            if idx >= n:
                if mod == 0:
                    return 0
                return -inf
            res = solve(idx + 1, mod)
            res = max(res, nums[idx] + solve(idx + 1, (mod + nums[idx]) % 3))
            return res
        
        return solve(0, 0)