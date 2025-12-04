class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        res, pre = 0, 0
        cnt[pre] += 1
        for el in nums:
            cur = el + pre
            res += cnt[cur - k]
            pre = cur
            cnt[cur] += 1
        return res