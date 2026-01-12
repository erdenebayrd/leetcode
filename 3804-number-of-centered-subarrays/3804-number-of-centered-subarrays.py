class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            cnt = defaultdict(int)
            curSum = 0
            for j in range(i, n):
                cnt[nums[j]] += 1
                curSum += nums[j]
                res += int(cnt[curSum] > 0)
        return res