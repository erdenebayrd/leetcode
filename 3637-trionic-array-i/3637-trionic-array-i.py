class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        def findLastIndex(startIndex: int, isIncreasing: bool) -> int:
            for i in range(startIndex, n - 1):
                if (isIncreasing is True and nums[i] >= nums[i + 1]) or (isIncreasing is False and nums[i] <= nums[i + 1]):
                    return i
            return n - 1
        p = findLastIndex(0, True)
        q = findLastIndex(p, False)
        return n - 1 == findLastIndex(q, True) and 0 < p and q < n - 1