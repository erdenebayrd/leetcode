class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # time: O(N ^ 3)
        # space: O(1)
        # method: brute-force
        # left, middle, right indices

        # 3 pointers/sliding window
        # time: O(N ^ 2)
        # space: O(1)
        # method: sliding window

        def tripleSum(left: int, middle: int, right: int) -> int:
            return nums[left] + nums[middle] + nums[right]

        n = len(nums)
        result = float('inf')
        delta = float('inf')
        nums.sort() # O(N * log N)
        for left in range(n - 2): # O(N ^ 2)
            middle = left + 1
            right = n - 1
            while middle < right:
                threeSum = tripleSum(left, middle, right)
                if abs(threeSum - target) < delta:
                    delta = abs(threeSum - target)
                    result = threeSum
                if threeSum > target:
                    right -= 1
                else: # threeSum <= target:
                    middle += 1
        return result