class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # time: O(N)
        # space: O(N)
        # method: two pointers
        n = len(nums)
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1
        m = len(cnt)
        res = 0
        cnt = defaultdict(int)
        cur = 0
        i, j = 0, 0
        while j < n:
            while j < n and cur < m:
                cnt[nums[j]] += 1
                if cnt[nums[j]] == 1:
                    cur += 1
                j += 1
            # print(i, j)
            while i < n and cur >= m:
                res += n - j + 1
                cnt[nums[i]] -= 1
                if cnt[nums[i]] == 0:
                    cur -= 1
                i += 1
        return res