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
        for i in range(2, len(nums), 3):
            cnt += 1
            if i >= idx:
                return cnt
        return (len(nums) + 2) // 3