class Solution:
    def findLHS(self, nums: List[int]) -> int:
        res = 0
        cnt = defaultdict(int)
        for x in nums:
            cnt[x] += 1
        for key in cnt:
            if key - 1 in cnt:
                res = max(res, cnt[key - 1] + cnt[key])
        return res