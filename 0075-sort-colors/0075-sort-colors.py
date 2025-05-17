class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = [0] * 3
        for num in nums:
            cnt[num] += 1
        idx = 0
        for i in range(3):
            while cnt[i] > 0:
                cnt[i] -= 1
                nums[idx] = i
                idx += 1
        return nums