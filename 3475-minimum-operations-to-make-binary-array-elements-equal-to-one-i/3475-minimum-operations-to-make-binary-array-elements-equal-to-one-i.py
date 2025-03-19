class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        def solve(idx: int) -> int:
            if idx + 2 > n - 1:
                if sum(nums[idx:]) != n - idx:
                    return int(1e9)
                return 0
            if nums[idx] == 1:
                return solve(idx + 1)
            for i in range(idx, idx + 3):
                nums[i] ^= 1
            return 1 + solve(idx + 1)
        res = solve(0)
        if res >= int(1e9):
            res = -1
        return res