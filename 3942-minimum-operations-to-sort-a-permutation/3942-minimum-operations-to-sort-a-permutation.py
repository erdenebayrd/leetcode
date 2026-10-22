class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # time: O(N)
        # space: O(1)
        # method: simulation

        n = len(nums)
        if n == 1:
            return 0
        count = 0
        index = -1
        for i in range(n):
            if abs(nums[i] - nums[i - 1]) > 1:
                count += 1
                index = i
                if nums[i] != 0 and nums[i - 1] != 0:
                    return -1
        
        if count > 1:
            return -1
        
        if count == 0:
            if nums[0] == n - 1:
                return 1
            return 0
        
        cost_shift_left = index
        cost_shift_right = n - index + 1
        if nums[index] == n - 1:
            cost_shift_left += 1
        if nums[index] == 0:
            cost_shift_right += 1
        cost = min(cost_shift_left, cost_shift_right)
        return cost