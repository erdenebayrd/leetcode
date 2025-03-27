class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        @cache
        def solve(idx: int) -> bool:
            if idx >= n - 1:
                return True
            res = False
            for i in range(1, nums[idx] + 1):
                res |= solve(idx + i)
                if res is True:
                    return res
            return res
        return solve(0)