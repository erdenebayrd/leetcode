class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        res = 0
        n = len(nums)
        sl = SortedList(nums)
        for md in range(n):
            sl.remove(nums[md])
            for le in range(md):
                res += sl.bisect_left(target - nums[le] - nums[md])
        return res