class Solution:
    def findLHS(self, nums: List[int]) -> int:
        res = 0
        prevKey = int(-2e9)
        nums.append(prevKey)
        nums.sort()
        cnt = Counter(nums)
        for key in cnt:
            # print(key)
            if key - 1 == prevKey:
                res = max(res, cnt[key] + cnt[prevKey])
            prevKey = key
        return res