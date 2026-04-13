class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        result = n
        for i in range(n):
            if nums[i] == target:
                result = min(result, abs(start - i))
        return result