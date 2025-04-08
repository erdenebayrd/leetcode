class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        idx = -1
        seen = set()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in seen:
                idx = i
                break
            seen.add(nums[i])
        if idx == -1:
            return 0
        cnt = 0
        return idx // 3 + 1