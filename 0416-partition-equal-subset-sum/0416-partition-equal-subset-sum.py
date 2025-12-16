class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1:
            return False

        pre = defaultdict(int)
        for x in nums:
            if x > s // 2:
                continue
            cur = defaultdict(int) | pre
            for key in pre:
                if key + x > s // 2:
                    continue
                cur[key + x] = 1
            cur[x] = 1
            pre |= cur
        return pre[s // 2] == 1