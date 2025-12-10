class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = int(1e9 + 7)
        pre = defaultdict(int)
        suf = defaultdict(int)
        for x in nums:
            suf[x] += 1
        
        res = 0
        for x in nums:
            suf[x] -= 1
            res += pre[x * 2] * suf[x * 2]
            pre[x] += 1
        return res % mod

