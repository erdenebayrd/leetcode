class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # time: O(N)
        # space: O(1) exluding result array
        # method: loop

        n = len(heights)
        result = [n - 1]
        idx = n - 1
        for i in range(n - 2, -1, -1):
            if heights[i] > heights[idx]:
                result.append(i)
                idx = i
        return result[::-1]