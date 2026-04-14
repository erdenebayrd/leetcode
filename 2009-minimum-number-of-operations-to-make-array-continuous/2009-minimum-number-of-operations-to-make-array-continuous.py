class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # time: O(N log N)
        # space: O(N) due to sorting
        # method: sort + sliding window

        n = len(nums)
        nums = sorted(set(nums))
        m = len(nums)
        result = 0
        left = 0
        for right in range(m):
            while nums[right] - nums[left] >= n:
                left += 1
            result = max(result, right - left + 1)
        result = n - result
        return result