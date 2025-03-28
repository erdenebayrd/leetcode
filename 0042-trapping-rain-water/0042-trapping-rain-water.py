class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxRight = [0] * n
        maxRight[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i])
        
        maxLeft = [0] * n
        maxLeft[0] = height[0]
        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i - 1], height[i])
        
        res = 0
        for i in range(n):
            x = min(maxLeft[i], maxRight[i])
            if x > height[i]:
                res += x - height[i]
        return res