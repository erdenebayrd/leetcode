class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # time: O(N ^ 2)
        # space: O(N)
        nums.sort()
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
        mx = max(dp)
        idxs = []
        for i in range(n):
            if dp[i] == mx:
                idxs.append(i)
                break
        for i in range(n - 1, -1, -1):
            if dp[i] + 1 == dp[idxs[-1]] and nums[idxs[-1]] % nums[i] == 0:
                idxs.append(i)
        # print(idxs)
        res = []
        for i in range(len(idxs) - 1, -1, -1):
            res.append(nums[idxs[i]])
        return res