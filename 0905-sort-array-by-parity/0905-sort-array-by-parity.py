class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # time: O(N)
        # space: O(1)
        # method: 2 pointers
        n = len(nums)
        left = 0
        for right in range(n):
            if nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums