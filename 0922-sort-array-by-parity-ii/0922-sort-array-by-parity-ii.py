class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # time: O(N)
        # space: O(1)
        # method: 2 pointers

        n = len(nums)
        odd = 1
        even = 0
        while odd < n and even < n:
            if nums[odd] % 2 == 1 and nums[even] % 2 == 0:
                odd += 2
                even += 2
            elif nums[odd] % 2 == 0 and nums[even] % 2 == 1:
                nums[odd], nums[even] = nums[even], nums[odd]
                odd += 2
                even += 2
            elif nums[odd] % 2 == 0 and nums[even] % 2 == 0:
                even += 2
            elif nums[odd] % 2 == 1 and nums[even] % 2 == 1:
                odd += 2
        return nums