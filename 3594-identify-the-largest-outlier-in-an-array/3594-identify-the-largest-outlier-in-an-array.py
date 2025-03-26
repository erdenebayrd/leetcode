class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        totalSum = 0
        for item in nums:
            cnt[item] += 1
            totalSum += item
        
        res = -1e3 - 1
        for item in nums:
            cnt[item] -= 1
            x = totalSum - 2 * item
            if cnt[x] > 0:
                res = max(res, x)
            cnt[item] += 1
        return res