class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        # time: O(N)
        # space: O(N)
        cnt = Counter(nums)
        res = -1
        for num in cnt:
            if cnt[num] == 1:
                res = max(res, num)
        return res