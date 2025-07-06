class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        sl = SortedList([])

        def isOkay(idx: int) -> bool:
            if idx >= n:
                return False
            if len(sl) == 0:
                return True
            return max(sl[-1], nums[idx]) - min(sl[0], nums[idx]) <= 2

        ri = 0
        for le in range(n):
            while isOkay(ri):
                sl.add(nums[ri])
                ri += 1
            res += ri - le
            sl.remove(nums[le])
        return res