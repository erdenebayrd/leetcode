class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # time: O(N^2)
        # space: O(N)
        # method: brute force
        n = len(nums)
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1
        m = len(cnt)
        res = 0
        for i in range(n):
            cnt = defaultdict(int)
            cur = 0
            for j in range(i, n):
                cnt[nums[j]] += 1
                if cnt[nums[j]] == 1:
                    cur += 1
                if cur >= m:
                    res += 1
        return res