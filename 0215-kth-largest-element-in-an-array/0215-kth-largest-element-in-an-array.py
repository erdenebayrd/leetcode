class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = defaultdict(int)
        mn = int(1e4)
        mx = -mn
        for num in nums:
            cnt[num] += 1
            mn = min(mn, num)
            mx = max(mx, num)
        for num in range(mx, mn - 1, -1):
            k -= cnt[num]
            if k <= 0:
                return num
        assert False