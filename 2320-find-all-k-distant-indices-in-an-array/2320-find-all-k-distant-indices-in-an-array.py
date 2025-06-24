class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        arr = []
        for i in range(n):
            if nums[i] == key:
                arr.append([max(i - k, 0), min(i + k, n - 1)])
        res = {}
        curL = -1
        for l, r in arr:
            curL = max(curL, l)
            for idx in range(curL, r + 1):
                res[idx] = True
            curL = max(curL, r)
        return list(res)