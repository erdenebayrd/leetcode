class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # time: O(N)
        # space: O(1)
        # method: 2 pointer + critical thinking
        result = 0
        n = len(colors)
        for i in range(n - 1, -1, -1):
            if colors[0] != colors[i]:
                result = i # i - 0
                break
        for i in range(n):
            if colors[i] != colors[n - 1]:
                result = max(result, n - 1 - i)
                break
        return result