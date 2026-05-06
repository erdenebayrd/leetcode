class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # time: O(N ^ 2)
        # space: O(1) but sorting use O(N)
        # method: 2 pointers + sorting
        n = len(nums)
        result = 0
        closestDiff = float('inf')
        nums.sort()
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                currentDiff = abs(currentSum - target)
                if currentDiff < closestDiff:
                    closestDiff = currentDiff
                    result = currentSum
                
                if currentSum > target:
                    right -= 1
                else: # currentSum <= target
                    left += 1
        return result