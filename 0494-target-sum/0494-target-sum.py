class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cnt = defaultdict(int) # how many different ways to create keys inside it
        cnt[0] = 1 # initialize value
        for x in nums:
            cur = defaultdict(int)
            for key, val in cnt.items():
                cur[key - x] += val
                cur[key + x] += val
            cnt = cur
        return cnt[target]