class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seenNubmersWithIndexes = {}
        for i in range(n):
            if target - nums[i] in seenNubmersWithIndexes:
                return [seenNubmersWithIndexes[target - nums[i]], i]
            seenNubmersWithIndexes[nums[i]] = i