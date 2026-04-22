class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        # time: O(N)
        # space: O(N)
        # method: DP

        n = len(nums)
        mod = int(1e9 + 7)
        
        # @cache
        # def solve(index: int, currentSum: int) -> int:
        #     if currentSum > 1:
        #         return 0
        #     if index >= n:
        #         if currentSum == 1:
        #             return 1
        #         return 0
        #     result = solve(index + 1, currentSum + nums[index]) % mod
        #     if currentSum == 1:
        #         result = (result + solve(index + 1, nums[index])) % mod
        #     return result
        # solve.cache_clear()
        # return solve(0, 0)

        # time: O(N)
        # space: O(1)
        # method: combinatoric
        total = sum(nums)
        if total <= 1:
            return total
        left, right = 0, 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                left = i
                break
        for i in range(n - 1, -1, -1):
            if nums[i] == 1:
                right = i
                break
        result = 1
        streak = 1
        for i in range(left, right + 1):
            if nums[i] == 1:
                result = (result * streak) % mod
                streak = 1
            else:
                streak += 1
        return result
            