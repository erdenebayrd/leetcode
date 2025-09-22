class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        mx = 0
        for key in cnt:
            mx = max(cnt[key], mx)
        res = 0
        for key in cnt:
            if mx == cnt[key]:
                res += mx
        return res