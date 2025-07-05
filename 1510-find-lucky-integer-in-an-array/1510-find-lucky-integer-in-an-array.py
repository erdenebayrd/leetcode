class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        res = -1
        for key in cnt:
            if key == cnt[key]:
                res = max(res, key)
        return res