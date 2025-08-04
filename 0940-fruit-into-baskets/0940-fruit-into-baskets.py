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
            while uniqueCount > 2:
                cnt[fruits[le]] -= 1
                if cnt[fruits[le]] == 0:
                    cnt.pop(fruits[le])
                    uniqueCount -= 1
                le += 1
            res = max(res, sum(cnt.values()))
        return res