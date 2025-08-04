class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # time: O(N)
        # space: O(1)
        # method: sliding window
        le = 0
        uniqueCount = 0
        cnt = defaultdict(int)
        res = 0
        for fruit in fruits:
            cnt[fruit] += 1
            if cnt[fruit] == 1:
                uniqueCount += 1
            while uniqueCount > 2:
                cnt[fruits[le]] -= 1
                if cnt[fruits[le]] == 0:
                    uniqueCount -= 1
                le += 1
            res = max(res, sum(cnt.values()))
        return res