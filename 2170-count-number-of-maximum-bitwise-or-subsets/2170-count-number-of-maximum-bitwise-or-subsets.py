class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # time: O(2 ^ N)
        # space: O(N)
        # method: brute force
        n = len(nums)
        s = 0
        for x in nums:
            s |= x

        @cache
        def solve(idx: int, bit: int) -> int:
            if idx >= n:
                if bit == s:
                    return 1
                return 0
            res = solve(idx + 1, bit)
            res += solve(idx + 1, bit | nums[idx])
            return res
        
        return solve(0, 0)