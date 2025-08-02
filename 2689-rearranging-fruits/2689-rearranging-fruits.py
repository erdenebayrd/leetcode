class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt1 = Counter(basket1)
        cnt2 = Counter(basket2)
        cnt = cnt1 + cnt2
        for cost in cnt:
            if cnt[cost] & 1:
                return -1
        res = 0
        extra1 = []
        for x in cnt1:
            y = cnt1[x] - cnt[x] // 2
            if y > 0:
                extra1.extend([x] * y)
        extra2 = []
        for x in cnt2:
            y = cnt2[x] - cnt[x] // 2
            if y > 0:
                extra2.extend([x] * y)
        assert len(extra1) == len(extra2)
        extra = []
        extra.extend(extra1)
        extra.extend(extra2)
        extra.sort()
        m = len(extra) // 2
        x = min(min(basket1), min(basket2))
        res = 0
        for val in extra[:m]:
            res += min(x * 2, val)
        return res