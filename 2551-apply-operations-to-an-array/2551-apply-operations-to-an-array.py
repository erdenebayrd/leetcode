class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = []
        for i in range(n):
            if i + 1 < n and nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            if nums[i] > 0:
                arr.append(nums[i])
        while len(arr) < n:
            arr.append(0)
        return arr