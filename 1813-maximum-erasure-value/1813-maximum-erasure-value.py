class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # time: O(N)
        # space: O(N)
        # method: sliding window (2 pointers)
        le = 0
        n = len(nums)
        cnt = defaultdict(int) # default value is 0
        cur, res = 0, 0
        for ri in range(n):
            cnt[nums[ri]] += 1
            cur += nums[ri]
            while le < n and cnt[nums[ri]] > 1:
                cur -= nums[le]
                cnt[nums[le]] -= 1
                le += 1
            # ri - le + 1
            res = max(res, cur)
        return res