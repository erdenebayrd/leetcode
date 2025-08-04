class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # time: O(N)
        # space: O(1)
        # method: slinding window
        le = 0
        uniqueCount = 0
        cnt = {}
        res = 0
        for fruit in fruits:
            if fruit not in cnt:
                cnt[fruit] = 0
                uniqueCount += 1
            cnt[fruit] += 1
            while uniqueCount > 2 and le < len(fruits):
                assert fruits[le] in cnt
                cnt[fruits[le]] -= 1
                if cnt[fruits[le]] == 0:
                    del cnt[fruits[le]]
                    uniqueCount -= 1
                le += 1
            cur = 0
            for key in cnt: # at most 2 keys
                cur += cnt[key]
            res = max(res, cur)
        return res