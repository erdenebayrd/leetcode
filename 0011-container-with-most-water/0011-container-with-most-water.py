class Solution:
    def maxArea(self, height: List[int]) -> int:
        # time: O(N)
        # space: O(1)
        # method: 2 pointers
        result = 0
        n = len(height)
        left, right = 0, n - 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            result = max(result, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result