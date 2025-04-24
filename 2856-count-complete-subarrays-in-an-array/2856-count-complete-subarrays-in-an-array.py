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
        left = 0
        for right in range(n):
            cnt[nums[right]] += 1
            if cnt[nums[right]] == 1:
                cur += 1
            while left < n and cur >= m:
                res += n - right
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    cur -= 1
                left += 1
        return res