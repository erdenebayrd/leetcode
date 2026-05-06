class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # time: O(N ^ 2)
        # space: O(1) but sort() function uses O(N) space
        # method: 2 pointers + sorting

        n = len(nums)
        nums.sort()
        result = 0
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                if currentSum >= target:
                    right -= 1
                else: # currentSum < target
                    result += right - left
                    left += 1

        return result