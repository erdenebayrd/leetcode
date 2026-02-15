class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # time: O(N ^ 2)
        # space: O(1)
        # method: 3 pointers/sliding window

        # step 1
        # sort an array 

        # step 2
        # 3 pointers
        #               [-2,0,1,3], target = 2
        # left              ^
        # middle              ^
        # right                 ^
        # currentSum = -2 + 1 + 3 = 2 < 2 False, counting left, middle, right whose sum are lower than target
        # if currentSum < target, 
        # result increased by right - middle = 3 - 1 = 2, result = 2
        
        nums.sort() # O(N*LogN)
        n = len(nums)
        result = 0
        for left in range(n - 2):
            middle = left + 1
            right = n - 1
            while middle < right:
                if nums[left] + nums[middle] + nums[right] >= target:
                    right -= 1
                else: # nums[left] + nums[middle] + nums[right] < target:
                    result += right - middle
                    middle += 1

        return result