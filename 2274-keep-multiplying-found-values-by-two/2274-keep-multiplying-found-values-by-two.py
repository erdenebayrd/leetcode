class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        cnt = Counter(nums)
        while original in cnt:
            original *= 2
        return original