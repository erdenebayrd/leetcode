class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1
        res = 0
        nums.sort()
        for num in nums:
            if num > k:
                k = num
                res += 1
        return res